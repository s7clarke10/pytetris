# PyTetris 🎮

[![License](https://img.shields.io/github/license/s7clarke10/pytetris)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)

A modern variation on the classic game of **Tetris**, written in Python with [pygame](https://www.pygame.org/).

---

## ✨ Features
- Retro arcade look with bundled pixel font (Press Start 2P).
- Cross‑platform support (Windows, macOS, Linux).
- Clean, reproducible environment managed with [Poetry](https://python-poetry.org/).
- Modular codebase for easy extension and learning.

---

## 🚀 Getting Started

### Prerequisites
- Python **3.11+** installed on your system.
- [pipx](https://pypa.github.io/pipx/) for managing global tools.

### 1. Install pipx
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Restart your terminal so pipx is available.

2. Install Poetry

```bash
pipx install poetry
```

3. Clone the Repository

```bash
git clone https://github.com/s7clarke10/pytetris.git
cd pytetris
```

4. Install Dependencies

```bash
poetry install
```

5. Run the Game

```bash
# Run the packaged script (recommended)
poetry run pytetris_working

# Or run the module directly (equivalent)
poetry run python -m pytetris.pytetris_working
```

## 🎮 Controls

- **Left Arrow:** move piece left
- **Right Arrow:** move piece right
- **Up Arrow:** rotate piece
- **Down Arrow:** move piece down / soft drop
- **Any key (on main menu):** start game
- **Close window / Quit:** exit the game

📂 Project Structure
```text
.
├── .gitignore
├── LICENSE                  # Apache 2.0 license
├── pyproject.toml           # Poetry project configuration (scripts, deps)
├── poetry.lock              # Locked dependency versions
├── README.md
├── scores.txt               # High score persistence used by the game
├── tests/                   # Unit tests
├── venv/                    # Optional local virtualenv (not committed normally)
└── pytetris/                # Main package
	├── __init__.py
	├── pytetris.py          # Alternate implementation / runnable module
	├── pytetris_working.py  # Current working game entrypoint (exports main)
	├── tetris2.py           # Other game logic / experiments
	├── tetrispiece.py       # Piece definitions and utilities
	├── fonts/               # Bundled fonts used by the game
	│   └── PressStart2P-Regular.ttf
	└── images/              # Images and icons
```

🎨 Screenshots
(Add screenshots or GIFs here once the game is running)

🛠️ Development Notes
- Poetry automatically creates and manages a virtual environment for the project.
- To add new dependencies:
```bash
poetry add <package>
```
- To run tests (if added):
```bash
poetry run pytest
```

📜 License
This project is licensed under the Apache 2.0 License — see the LICENSE file for details.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

🙌 Acknowledgements
- pygame for the game framework.
- Press Start 2P font for the retro arcade feel.
- Inspiration from the original Tetris (1984).


