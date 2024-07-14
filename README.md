# tmux-wrangler

A python cli tool to manage tmux sessions, windows, and panes.

## Installation

To install tmux-wrangler, clone this repository and run the installation script:

```bash
git clone https://github.com/yourusername/tmux-wrangler.git
cd tmux-wrangler
bin/run build
bin/run install
```

## Usage

To see the available commands and options, run:

```bash
tmuxw --help
```

## Most Common Commands

### Create a new session with index, server, and test windows

```bash
tmuxw
```

### Create a new session with app1, app2, and app3 windows

```bash
tmuxw -w app1 -w app2 -w app3
```

### Create a new session with name mysession, and app1, app2, and app3 windows

```bash
tmuxw mysession -w app1 -w app2 -w app3
```

Future Features

- [ ] Add charm
- [ ] Support for split panes
