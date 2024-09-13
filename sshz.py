import os
import hcloud
import hcloud.server_types
import hcloud.servers
import readchar

tok_path = os.path.join(os.path.dirname(__file__), "token")
toks: list[str] = []

if not os.path.exists(tok_path):
    print("Input your Hetzner project tokens:")
    toks = []
    tok = input()
    while tok != "":
        toks.append(tok)
        tok = input()

    with open(tok_path, "w") as f:
        f.write("\n".join(toks))

with open(tok_path, "r") as f:
    for tok in f.readlines():
        toks.append(tok.strip())


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def select(*options):
    select_idx = 0

    def render():
        clear()
        for i, opt in enumerate(options):
            if i == select_idx:
                print(f"\033[32m> {opt}\033[0m")
            else:
                print(opt)

    render()
    inp = readchar.readkey()
    while inp != readchar.key.ENTER:
        if inp == readchar.key.UP:
            select_idx = max(0, select_idx - 1)
        elif inp == readchar.key.DOWN:
            select_idx = min(len(options) - 1, select_idx + 1)

        render()
        inp = readchar.readkey()
    clear()
    return select_idx


def main():
    servers: list[hcloud.servers.client.BoundServer] = []
    for tok in toks:
        project = hcloud.Client(tok)
        servers += [x for x in project.servers.get_all()]

    idx = select(*[s.name for s in servers])

    ip = servers[idx].public_net.ipv4.ip
    os.system(f"ssh root@{ip}")
