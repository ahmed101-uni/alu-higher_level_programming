#!/usr/bin/python3
"""
101-nqueens.py: Solves the N-Queens problem for a given N.

Where N is the number of queens to place on an NxN
chessboard such that no two queens threaten each other.
"""
import sys


class Nqueens:
    """
    A class to solve the N-Queens problem using backtracking.
    """

    def solveNqueens(self, n):
        """
        Solve the N-Queens problem using backtracking.
        This method finds all possible solutions to the
        N-Queens problem and prints them.
        """

        cols = set()
        posDiag = set()
        negDiag = set()

        results = []
        posiResult = set()

        def backtrack(r):
            """
            Helper function to perform backtracking.
            """
            if r == n:
                temp = list(map(lambda i: list(i), posiResult))

                print(temp)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                posiResult.add((r, c))

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                posiResult.remove((r, c))

        backtrack(0)
        return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    q = Nqueens()
    q.solveNqueens(N)
