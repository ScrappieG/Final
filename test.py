from sudoku_generator import SudokuGenerator
'''

This is a temporary file for making sure that the background program is running correctly

'''
def main():
    '''
    This initialized the Sudoku generator row length will always be 9, removed cells will
    81 - (The difficulty they choose)

    Note: Board is initialized to have 0 in every space

    '''
    sudoku = SudokuGenerator(row_length=9, removed_cells=30)

    # fills each 3x3 box on the diagnol starting at (0,0), (3,3) and (6,6)
    sudoku.fill_diagonal()

    sudoku.print_board() # prints the board

    # fills the remaining squares and return a bool indicating whether its solvable
    solvable = sudoku.fill_remaining(row=0,col=3)

    sudoku.print_board()

    print(f'This is solvable, {solvable}')

    # Generate sodoku is the function we will be using

    return



if __name__ == '__main__':
    main()