from typing import List
import os

import click


def session_exists(session_name: str) -> bool:
    result = os.system(f"tmux has-session -t {session_name} 2>/dev/null")
    return result == 0


@click.command()
@click.argument("session_name", default=os.path.basename(os.getcwd()))
@click.option(
    "--windows",
    "-w",
    multiple=True,
    default=["index", "server", "test"],
    help="List of windows to create",
)
def create_tmux_session(session_name: str, windows: List[str]) -> None:
    if session_exists(session_name):
        click.echo(f'🚨 Tmux session with name "{session_name}" already exists.')
    else:
        os.system(f"tmux new-session -s {session_name} -d -n {windows[0]}")

        for window in windows[1:]:
            os.system(f"tmux new-window -t {session_name} -n {window}")

        if "server" in windows:
            os.system(f"tmux select-window -t {session_name}:server")

        os.system(f"tmux attach -t {session_name}")


if __name__ == "__main__":
    create_tmux_session()
