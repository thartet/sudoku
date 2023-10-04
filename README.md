# Sudoku solver

This code is a python implementation of a sudoku solver. It uses backtracking algorithm to find a solution for a given sudoku grid.

## Sudoku grid

The sudoku grid is represented as a 9x9 two-dimensional list. Empty cells are represented by '0' and filled cells contain the numbers 1 through 9. The one given is an example, you might replace it by the grid that you want to solve.

```python
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
```

## How to use

At first, you have to clone the repository or just download the file solveur.py. Then, you run the file (you might have to change user rights to execute it).

```bash
chmod u+x solveur.py
```
