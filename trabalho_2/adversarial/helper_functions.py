import os
from colorama import Fore, Style, init
init(autoreset=True)

# Helper: clean screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Helper: color cell content
def colorize(cell):
    if cell == 'W':
        return Fore.BLUE + 'W' + Style.RESET_ALL
    elif cell == 'B':
        return Fore.RED + 'B' + Style.RESET_ALL
    else:
        return ' '

def print_board(board, cols):
    clear_screen()
    # Imprime cada linha do tabuleiro com seu número
    for i, row in enumerate(board):
        print(f"{i} |" + '|'.join(colorize(cell) for cell in row) + '|')
    # Imprime os números das colunas
    print('  ' + ' '.join(map(str, range(cols))))
