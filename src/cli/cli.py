from typing import List, Optional
import os

import click


def session_exists(session_name: str) -> bool:
    # "=" forces an exact match; otherwise tmux prefix-matches, so "iv-pro"
    # would resolve to an existing "iv-pro-baby" session.
    result = os.system(f"tmux has-session -t ={session_name} 2>/dev/null")
    return result == 0


def get_next_available_session_name(base_name: str) -> str:
    """Find the next available session name with numeric suffix."""
    if not session_exists(base_name):
        return base_name

    suffix = 1
    while session_exists(f"{base_name}-{suffix}"):
        suffix += 1

    return f"{base_name}-{suffix}"


@click.command()
@click.argument("session_name", default=os.path.basename(os.getcwd()))
@click.option(
    "--windows",
    "-w",
    multiple=True,
    default=["index", "server", "livebook", "test"],
    help="List of windows to create",
)
@click.option(
    "--duplicate",
    "-d",
    is_flag=True,
    help="Create new session with incremented suffix if session exists",
)
@click.option(
    "--split",
    "-s",
    type=str,
    help="Split pane configuration: 'h' for horizontal (left/right), 'v' for vertical (top/bottom)",
)
def create_tmux_session(
    session_name: str,
    windows: List[str],
    duplicate: bool,
    split: Optional[str],
) -> None:
    # Handle duplicate flag - find next available session name
    if duplicate and session_exists(session_name):
        session_name = get_next_available_session_name(session_name)
        click.echo(f'Creating session with name "{session_name}"')
    elif session_exists(session_name):
        click.echo(f'🚨 Tmux session with name "{session_name}" already exists.')
        return

    # Create the session with first window
    os.system(f"tmux new-session -s {session_name} -d -n {windows[0]}")

    # Add additional windows
    for window in windows[1:]:
        os.system(f"tmux new-window -t ={session_name}: -n {window}")

    # Handle split configuration
    if split:
        if split.lower() == 'h':
            # Split horizontally (left/right)
            for window in windows:
                os.system(f"tmux split-window -h -t ={session_name}:{window}")
        elif split.lower() == 'v':
            # Split vertically (top/bottom)
            for window in windows:
                os.system(f"tmux split-window -v -t ={session_name}:{window}")
        else:
            click.echo(f"Invalid split option: '{split}'. Use 'h' for horizontal or 'v' for vertical.")

    # Select server window if it exists
    if "server" in windows:
        os.system(f"tmux select-window -t ={session_name}:server")

    # Attach to the session
    os.system(f"tmux attach -t ={session_name}")


if __name__ == "__main__":
    create_tmux_session()
