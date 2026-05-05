def print_board(board, n):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]

    col = [False]*n
    diag1 = [False]*(2*n)
    diag2 = [False]*(2*n)

    solution_count = 0   # 🔹 Count solutions

    def solve(row):
        nonlocal solution_count

        if row == n:
            solution_count += 1
            print(f"Solution {solution_count}:")
            print_board(board, n)
            return

        for c in range(n):
            if not col[c] and not diag1[row+c] and not diag2[row-c+n-1]:

                # Place queen
                board[row][c] = 1
                col[c] = diag1[row+c] = diag2[row-c+n-1] = True

                # Recur
                solve(row+1)

                # Backtrack
                board[row][c] = 0
                col[c] = diag1[row+c] = diag2[row-c+n-1] = False

    solve(0)

    # 🔹 Print total solutions
    if solution_count == 0:
        print("No solution exists")
    elif solution_count == 1:
        print("Total: 1 solution")
    else:
        print(f"Total: {solution_count} solutions")


# 🔹 User Input
n = int(input("Enter number of queens: "))
solve_n_queens(n)
