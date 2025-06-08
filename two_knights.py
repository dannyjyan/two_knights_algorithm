from collections import deque


def min_knight_capture_with_paths(startA, startB):
    MOVES = [(-2, 1), (-1, 2), (1, 2), (2, 1),
             (2, -1), (1, -2), (-1, -2), (-2, -1)]

    def neighbors(x, y):
        for dx, dy in MOVES:
            yield x + dx, y + dy

    def in_bounds(x, y, N):
        return 0 <= x < N and 0 <= y < N
    
    N = 8 # SIZE OF BOARD


    # visitedA and visitedB just track that we've seen that square
    visitedA = set([tuple(startA)])
    visitedB = set([tuple(startB)])

    # frontier maps current position -> path taken to get here
    frontierA = {tuple(startA): [tuple(startA)]}
    frontierB = {tuple(startB): [tuple(startB)]}

    turn = 0
    while frontierA and frontierB:
        turn += 1

        # 1a. Expand A one move
        nextA = {}
        for (x, y), path in frontierA.items():
            for nx, ny in neighbors(x, y):
                pos = (nx, ny)
                if not in_bounds(nx, ny, N):
                    continue
                if pos not in visitedA:
                    visitedA.add(pos)
                    nextA[pos] = path + [pos]

        # 1b. Check if A has captured B by landing on B's old squares
        for pos, pathA in nextA.items():
            if pos in frontierB:        # B was here at the start of the turn
                pathB = frontierB[pos]   # B's path to pos (no extra move)
                return turn, pathA, pathB

        # 2a. Expand B one move
        nextB = {}
        for (x, y), path in frontierB.items():
            for nx, ny in neighbors(x, y):
                pos = (nx, ny)
                if not in_bounds(nx, ny, N):
                    continue
                if pos not in visitedB:
                    visitedB.add(pos)
                    nextB[pos] = path + [pos]

        
        # 2b. Check if B has captured A by landing on one of A's new squares
        for pos, pathB in nextB.items():
            if pos in nextA:            # A moved here earlier this turn
                pathA = nextA[pos]
                return turn, pathA, pathB

        frontierA, frontierB = nextA, nextB

    return -1, [], []  # should never happen under normal chessboard

# Example
if __name__ == "__main__":
    # Test case 1
    print("Test Case 1:")
    a = [0, 0]
    b = [4, 2]
    turns, pathA, pathB = min_knight_capture_with_paths(a, b)
    print("Turns until capture:", turns)
    print("KnightA starts:", tuple(a), "KnightB starts:", tuple(b))
    for i in range(1, len(pathA)):
        print("KnightA moves: ", pathA[i], end=" ")
        if i < len(pathB):
            print("KnightB moves: ", pathB[i])
        else:
            print("KnightB stays at:", pathB[-1])
    print()

    # Test case 2
    print("Test Case 2:")
    a = [0, 0]
    b = [7, 7]
    turns, pathA, pathB = min_knight_capture_with_paths(a, b)
    print("Turns until capture:", turns)
    print("KnightA starts:", tuple(a), "KnightB starts:", tuple(b))
    for i in range(1, len(pathA)):
        print("KnightA moves: ", pathA[i], end=" ")
        if i < len(pathB):
            print("KnightB moves: ", pathB[i])
        else:
            print("KnightB stays at:", pathB[-1])
    print()

    # Test case 3
    print("Test Case 3:")
    a = [3, 3]
    b = [4, 4]
    turns, pathA, pathB = min_knight_capture_with_paths(a, b)
    print("Turns until capture:", turns)
    print("KnightA starts:", tuple(a), "KnightB starts:", tuple(b))
    for i in range(1, len(pathA)):
        print("KnightA moves: ", pathA[i], end=" ")
        if i < len(pathB):
            print("KnightB moves: ", pathB[i])
        else:
            print("KnightB stays at:", pathB[-1])
    print()

    # Test case 4
    print("Test Case 4:")
    a = [2, 3]
    b = [3, 3]
    turns, pathA, pathB = min_knight_capture_with_paths(a, b)
    print("Turns until capture:", turns)
    print("KnightA starts:", tuple(a), "KnightB starts:", tuple(b))
    for i in range(1, len(pathA)):
        print("KnightA moves: ", pathA[i], end=" ")
        if i < len(pathB):
            print("KnightB moves: ", pathB[i])
        else:
            print("KnightB stays at:", pathB[-1])
    print()



