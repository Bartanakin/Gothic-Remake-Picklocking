# Gothic Remake Picklocking Solver

A Python script to generate a sequence of keys (`W`, `S`, `D`, or `A`) that opens any lock in Gothic Remake.

## What this does

The script reads lock configuration files, explores the available moves, and prints a solution sequence of key presses to open the lock.

## Installation

1. Clone the repository:
   ```powershell
   git clone https://github.com/Bartanakin/Gothic-Remake-Picklocking.git
   cd "Picklocking Gothic Remake"
   ```
2. Install Python if it is not already installed - https://www.python.org/downloads
3. Run the script:
   ```powershell
   python picklocking.py
   ```

## Input setup

The solver uses three input files located next to `picklocking.py`:

### 1. `initial.txt`

Defines the initial configuration of the lock.

- The file contains one line with numbers from `1` to `7`.
- Each number represents the initial position of a plate in the.
- Plates are ordered from left-bottom to right-top.
- `1` means the plate is farthest toward left-bottom.
- `7` means the plate is farthest toward right-top.

If the lock has `n` plates, this line should contain exactly `n` numbers.

### 2. `moves.txt`

Defines how plates react when the picklock moves sideways.

- The file contains `n` lines, one for each plate.
- Each line has exactly `n` characters.
- Characters can be:
  - `F` � Forward
  - `R` � Reversed
  - `N` � Neutral

Each line describes how the plates behave when you press `D` or `A`.

- If a plate slides in the same direction as the original plate, use `F`.
- If it slides in the opposite direction, use `R`.
- If it does not move, use `N`.
- The file should contain `F` on the diagonal (each plate affects itself in the forward direction).

There are always `2 * n` possible moves in the lock system, and some moves may break the picklock (the algorithm will never select them, don't worry).

### 3. `max_depth.txt`

Defines the maximum number of plate slides the solver is allowed to explore.

- This prevents the algorithm from running indefinitely.
- If the solver does not find a winning combination, increase this number and try again.

## Running the solver

Make sure the input files exist and are correctly formatted, then run:

```powershell
python picklocking.py
```

The script will read the lock configuration and output a sequence of key presses that should open the lock.
