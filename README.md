# tmux-wrangler

A simple CLI tool to quickly create and manage tmux sessions with predefined window layouts.

## Features

- Automatically creates tmux sessions with customizable window names
- Defaults to using the current directory name as the session name
- Prevents duplicate sessions with the same name
- Automatically attaches to the created session
- Configurable window list via command-line options

## Installation

### Using Poetry

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tmux-wrangler.git
cd tmux-wrangler
```

2. Install dependencies with Poetry:
```bash
poetry install
```

3. Run the tool:
```bash
poetry run tmuxw
```

### Using PyInstaller (for standalone binary)

Build a standalone executable:
```bash
poetry run pyinstaller --onefile src/cli/cli.py -n tmuxw
```

The binary will be available in the `dist/` directory.

## Usage

### Basic Usage

Create a tmux session with the default window layout (index, server, livebook, test):
```bash
tmuxw
```

This will create a session named after your current directory.

### Custom Session Name

Specify a custom session name:
```bash
tmuxw my-project
```

### Custom Window Layout

Define your own window names using the `-w` or `--windows` option:
```bash
tmuxw my-project -w editor -w terminal -w logs -w debug
```

## Default Behavior

- **Session Name**: Uses the current directory name if not specified
- **Default Windows**: `index`, `server`, `livebook`, `test`
- **Active Window**: Automatically switches to the `server` window if it exists
- **Auto-attach**: Automatically attaches to the session after creation

## Development

### Running Tests
```bash
poetry run test
```

### Linting and Formatting
```bash
# Run linter
poetry run lint

# Fix linting issues
poetry run lint_fix

# Run type checking
poetry run type_check
```

## Requirements

- Python 3.12+
- tmux installed on your system
- Click (Python package)

## Future Features

- [ ] Add charm/TUI interface
- [ ] Support for split panes
- [ ] Session templates/profiles
- [ ] Window-specific commands on creation

## License

MIT License

## Author

Nirmit Dalal
