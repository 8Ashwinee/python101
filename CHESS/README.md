
# ♟️ Python Chess Game

A desktop chess game built with **Python** and **Pygame**, featuring a graphical 8×8 board, clickable piece selection, candidate-move highlighting, captures, turn indicators, and a game-over prompt.

> **Project status:** Basic playable prototype. This implementation does not enforce every official chess rule. See [Known Limitations](docs/KNOWN_LIMITATIONS.md).

## ✨ Features

- Graphical chessboard in a Pygame window.
- White and Black pieces with alternating turns.
- Click a piece and then a destination square to move.
- Highlights candidate destinations for the selected piece.
- Basic movement patterns for pawns, rooks, knights, bishops, queens, and kings.
- Captured pieces displayed along the side of the board.
- Visual indicator when the current king's square is threatened by a generated move.
- Piece images downloaded from remote URLs and processed with `rembg`.

## 🧰 Built With

- **Python 3** — application logic.
- **Pygame** — graphics, events, and game loop.
- **Requests** — downloads piece images.
- **rembg** — removes image backgrounds.
- **BytesIO** — passes downloaded image bytes to Pygame.

## 📁 Project Structure

```text
python-chess-game/
├── main.py
├── README.md
├── requirements.txt
└── docs/
    ├── ARCHITECTURE.md
    ├── CONTRIBUTING.md
    ├── GAMEPLAY.md
    ├── INSTALLATION.md
    ├── KNOWN_LIMITATIONS.md
    └── TESTING.md
```

Rename your Python script to `main.py`, or use its actual filename in the run command.

## 🚀 Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Install the dependencies:

**Windows PowerShell**
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**macOS / Linux**
```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run the game:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

See [Installation Guide](docs/INSTALLATION.md) for detailed instructions.

## 🎮 How to Play

1. Launch the game.
2. White moves first.
3. Click one of your pieces.
4. Click a highlighted destination square.
5. Capture an opposing piece by moving onto its square when the move generator permits it.
6. Close the game window to exit.

See [Gameplay Guide](docs/GAMEPLAY.md) for controls and details.

## 🧩 How It Works

- Board rendering draws the grid, status strip, and sidebar.
- Piece state is stored in lists of piece types and coordinates.
- Separate functions generate candidate moves for each piece type.
- The selection state tracks the current piece and its candidate moves.
- Captures remove pieces from the active lists.
- The Pygame loop processes events and redraws the screen at up to 60 FPS.

See [Architecture](docs/ARCHITECTURE.md).

## ⚠️ Current Limitations

This is a learning prototype, not a complete chess engine.

- Castling, en passant, and pawn promotion are not implemented.
- Checkmate and stalemate are not detected.
- Moves are not fully validated against check.
- The game ends when a king is captured rather than by checkmate.
- The forfeit control needs correction.
- Piece images require network access at startup.
- Automated tests were not included in the supplied code.

See [Known Limitations](docs/KNOWN_LIMITATIONS.md).

## 🧪 Testing

No automated test suite was supplied with the original script. A manual test plan and recommended movement tests are available in [Testing Guide](docs/TESTING.md).

## 🗺️ Roadmap

- [ ] Verify standard chess starting positions.
- [ ] Fix board and sidebar click-coordinate handling.
- [ ] Improve turn and selection-state handling.
- [ ] Add movement validation tests.
- [ ] Prevent moves that leave a king in check.
- [ ] Implement checkmate and stalemate.
- [ ] Add castling, en passant, and pawn promotion.
- [ ] Cache piece images and handle network failures.
- [ ] Separate the rules engine from the UI.
- [ ] Add automated unit tests.

## 🤝 Contributing

Contributions are welcome. Please see [Contributing Guide](docs/CONTRIBUTING.md).

## 📄 License and Image Credits

No project license was provided with the source code. Choose and add a license only after confirming you have the right to do so.

The script downloads chess-piece images from GeeksforGeeks-hosted URLs. Verify their licensing and reuse permissions before redistributing them.
