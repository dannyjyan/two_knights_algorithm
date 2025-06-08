# Movement of Knights Algorithm

This program implements an knights moving algorithm that returns the path and lowest number of turns it takes for two knights to be on the same square. It runs in O(N^2) time, where N is the dimensions of the board.

## How to run it

1. Save the Python file to your computer
2. Run this command:
   ```
   python two_knights.py
   ```

# Pseudocode of Algorithm.
```
function min_knight_capture_with_paths(startA, startB):
    MOVES = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

    function in_bounds(x,y):
        return 0 ≤ x < N  AND  0 ≤ y < N

    # Prevent revisits
    visitedA = { startA }
    visitedB = { startB }

    # frontierX maps current square and path taken
    frontierA = { startA : [ startA ]}
    frontierB = { startB : [ startB ]}

    turn = 0

    while frontierA and frontierB:
        turn += 1

        # 1a. KnightA moves
        nextA = {}
        for each path in frontierA: 
            for nx, ny in neighbors(x, y): 
                pos = (nx, ny)
                if not in bounds:
                    skip
                if pos not in visitedA:
                    visitedA.add(pos)
                    nextA[pos] = path + [pos]

        # 1b. Check if KnightA captured KnightB
        for each pos in nextA.keys() do
            if pos in frontierB.keys() then
                return turn, nextA[pos], frontierB[pos]

        # 2a. KnightB moves
        nextB = {}
        for (x, y), path in frontierB.items():
            for nx, ny in neighbors(x, y):
                pos = (nx, ny)
                if not in bounds:
                    skip
                if pos not in visitedB:
                    visitedB.add(pos)
                    nextB[pos] = path + [pos]

        
        # 2b. Check if KnightB captured KnightA
        for pos, pathB in nextB.items():
            if pos in nextA:            # A moved here earlier this turn
                return turn, nextA[pos] , pathB

        frontierA, frontierB = nextA, nextB

    return -1, [], []  # no capture possible
```

# Big O analysis (Step Count/Dominant Terms)
The time complexity is O(N^2), where N is the size of the chessboard.
Each square can be visited once by each knight, and each knight checks up to 8 squares every move
Thus, the complexity would be 8*2*n^2 = 16n^2, which is in O(n^2).

The space complexity is also O(N^2), since we hold up to n^2 moves per knight.

