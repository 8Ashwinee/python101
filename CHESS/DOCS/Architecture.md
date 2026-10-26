
# Architecture and Code Reference

## Overview

The program is implemented as a single Python script using Pygame. It initializes the window and image assets, stores board state, generates candidate moves, renders the position, and processes user input in a main loop.

## Dependencies

| Dependency | Purpose |
|---|---|
| `pygame` | Window, graphics, image rendering, events, and frame timing |
| `requests` | Downloads piece images |
| `rembg` | Removes image backgrounds |
| `io.BytesIO` | Provides an in-memory stream for downloaded image data |

## State Variables

| Variable | Purpose |
|---|---|
| `WIDTH`, `HEIGHT` | Window dimensions: 1000 × 900 |
| `white_pieces`, `black_pieces` | Piece-type lists for each side |
| `white_locations`, `black_locations` | Coordinates corresponding to each piece |
| `captured_pieces_white`, `captured_pieces_black` | Captured pieces recorded for display |
| `turn_step` | Encodes the turn and selection phase |
| `selection` | Index of the selected piece; `100` represents no selection |
| `valid_moves` | Candidate destinations for the selected piece |
| `white_options`, `black_options` | Generated candidates for each piece |
| `winner` | Winner label shown by the interface |
| `game_over` | Controls the game-over UI state |
| `counter` | Controls flashing king-threat highlighting |

### State Consistency

Piece types and their coordinates are stored in parallel lists. Their indexes must remain aligned. When a piece is captured, its entry must be removed from both lists.

## Main Functions

### `draw_board()`

Draws the board, grid lines, bottom status strip, sidebar border, turn prompt, and forfeit label.

### `draw_pieces()`

Draws active pieces at their stored coordinates and outlines the selected piece.

### `check_options(pieces, locations, turn)`

Dispatches move generation to the function associated with each piece type.

### `check_king(position, color)`

Generates adjacent-square candidates that are in bounds and not occupied by friendly pieces.

### `check_queen(position, color)`

Combines the bishop and rook candidate lists.

### `check_bishop(position, color)`

Generates diagonal sliding candidates until reaching a board boundary or blocking piece.

### `check_rook(position, color)`

Generates horizontal and vertical sliding candidates until reaching a boundary or blocking piece.

### `check_pawn(position, color)`

Generates forward movement and diagonal capture candidates.

### `check_knight(position, color)`

Generates L-shaped movement candidates that are in bounds and not occupied by friendly pieces.

### `check_valid_moves()`

Returns the candidate moves associated with the currently selected piece.

### `draw_valid(moves)`

Draws markers on candidate destination squares.

### `draw_captured()`

Displays captured pieces in the sidebar.

### `draw_check()`

Attempts to highlight a king when the opponent's generated candidate moves reach its square. This is not a complete check-validation engine.

### `draw_game_over()`

Draws the winner message and restart prompt.

## Main Game Loop

The main loop:

1. Limits frame updates using the Pygame clock.
2. Clears the screen and draws the board.
3. Draws active and captured pieces.
4. Draws king-threat feedback and candidate moves.
5. Processes mouse and keyboard events.
6. Updates piece positions and captures.
7. Refreshes the display.

## Design Limitations

The rules, UI, networking, and event handling are coupled in one script. Parallel lists can become inconsistent if they are updated incorrectly.

A future refactor could separate the application into:

- `main.py` — application entry point.
- `game_state.py` — board and turn state.
- `chess_rules.py` — move generation and legal-move validation.
- `renderer.py` — drawing and visual effects.
- `assets.py` — image loading and caching.
- `tests/` — automated rule and state tests.
