
# Gameplay Guide

## Controls

| Action | Input |
|---|---|
| Select a piece | Left-click a piece belonging to the side to move |
| View candidate moves | Select a piece to display destination markers |
| Move a piece | Left-click a candidate destination |
| Exit the game | Close the Pygame window |

## Board Interface

The game uses an 8×8 board inside a 1000×900 window.

- Each board square is intended to be 100×100 pixels.
- The bottom strip displays the current turn and selection prompt.
- The right sidebar displays captured pieces.
- White's selected piece is outlined in red.
- Black's selected piece is outlined in blue.
- Candidate destinations are displayed as small colored circles.

## Moving Pieces

1. Select a piece belonging to the current side.
2. Review its highlighted candidate destinations.
3. Click a destination to attempt the move.
4. The board updates and the turn changes when the move is processed.

The program generates candidate moves separately for each piece type.

## Captures

When a generated move reaches an opposing piece's square, the captured piece is removed from the active piece and location lists and recorded for display.

## Important Note

The displayed destinations are not guaranteed to be legal under all official chess rules. The game does not implement every special move or complete check/checkmate validation.

The interface draws a FORFEIT label, but the supplied click handling does not reliably implement a functional forfeit control.
