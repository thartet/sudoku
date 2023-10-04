grid = [
    [0,0,4,0,3,0,5,0,0],
    [0,6,5,4,9,1,2,7,0],
    [8,9,1,7,2,0,0,6,0],
    [5,0,0,9,0,2,0,8,0],
    [0,0,3,0,6,0,7,0,2],
    [4,0,0,1,7,0,0,5,6],
    [0,3,0,0,0,0,8,9,0],
    [1,0,9,0,0,7,0,2,5],
    [0,5,8,6,0,0,0,0,7]
]

# Solve the grid
def solve(gr):
    # We find the next empty cell until there is no empty cell
    find = find_empty(gr)
    if not find:
        return True
    else:
        row, col = find

    # We try every number from 1 to 9 in the empty cell and then solve the grid
    for i in range(1,10):
        if valid(gr, i, (row, col)):
            gr[row][col] = i

            if solve(gr):
                return True
            
            # If the value is not working, we reset the cell (backtracking)
            gr[row][col] = 0

    return False

# Check if the number is valid
def valid(gr, num, pos):
    # Check row
    for i in range(len(gr[0])):
        if gr[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(gr)):
        if gr[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    # The box is a 3x3 square so we define the box_x and box_y
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # We check every cell in the box and check if the value is good or not
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if gr[i][j] == num and (i,j) != pos:
                return False

    return True

# Print the grid
def print_grid(gr):
    for i in range(len(gr)):
        # We print a line every 3 rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(gr[0])):
            # We print a line every 3 columns
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # We print the last number of the row
            if j == 8:
                print(gr[i][j])
            else:
                print(str(gr[i][j]) + " ", end="")


# Find the next empty cell
def find_empty(gr):
    for i in range(len(gr)):
        for j in range(len(gr[0])):
            if gr[i][j] == 0:
                return (i, j)  # row, col

    return None

#Main function
def main():
    print("Original Grid :")
    print_grid(grid)
    solve(grid)
    print("\nSolution")
    print_grid(grid)

# If the file is executed, we execute the main function
if __name__ == "__main__":
    main()
else:
    print("[-] Error : The function main() did not execute.")