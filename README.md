# Orienteering-Startlist-Screen
A lightweight cross-platform application to display orienteering start lists in a web browser.
By importing a start list in IOF XML v3 format, the program hosts the data on a local web server.
Users can then view and monitor start lists via any browser on the same network.
It supports multiple parallel starts and runs on both Windows and Linux.

---
## Development - Setup
### 1. Requirements
- Python 3.13 (check with `python --version` or `py -3.13 --version`)
- Poetry (`py -3.13 -m pip install poetry`) (check with `poetry --version`)

### 2. Clone the repository
```shell
git clone git@github.com:lenz-exe/orienteering-startlist-screen.git
cd orienteering-startlist-screen
```

### 3. Install virtual environment and dependencies
(Optional) Ensure Poetry uses the correct Python version:
```shell
poetry env use 3.13
```
Install all dependencies:
```shell
poetry install
```

### 4. `main.py`
You can start the application from PyCharm or directly via:
```shell
poetry run ./src/orienteering_startlist_screen/main.py
```

___

## Development - Commands
Generate Python files (`*_ui.py`) from Qt `.ui` files:
```shell
poetry run generate-ui
```

Generate Python files (`*_rc.py`) from Qt `.qrc` resource files:
```shell
poetry run generate-rcc
```

Generate the `.spec` file for PyInstaller:
```shell
poetry run build-spec
```

Build the binary via PyInstaller:
```shell
poetry run build-bin
```

Build the Windows installer (requires Inno Setup Compiler, Windows only):
```shell
poetry run build-win-installer
```

Run code quality checks (`ruff`, `mypy`, `pytest`):
```shell
poetry run check
```

Simulate CI/CD linting and testing:
```shell
poetry run check-ci
```


## Development - Tailwind CSS (Minimal)
If you modify index.html and need to regenerate app.css using TailwindCSS.

Install dependencies:
```bash
npm install -D tailwindcss @tailwindcss/cli
```
Input file: `assets/tailwind/input.css`
```css
@import "tailwindcss";
```
Generate the new CSS file:
```bash
npx @tailwindcss/cli \
  -i ./assets/tailwind/input.css \
  -o ./src/orienteering_startlist_screen/utils/static/css/app.css \
  --minify
```
