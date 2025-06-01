import time
from colorama import Fore, Style, init

# Reinitialize colorama after reset
init(autoreset=True)

from minimax import minimax_with_hef
from breakthrough import Breakthrough, COLS

from helper_functions import print_board

# heuristica para breakthrough
def evaluate_breakthrough(board, player):
    opponent = 'B' if player == 'W' else 'W'
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            piece = board[i][j]
            if piece == player:
                # incentiva avançar no tabuleiro
                score += (ROWS - i) if player == 'W' else i
                score += 10
            elif piece == opponent:
                score -= 10
    return score

# ia minimax para breakthrough
def best_move(game, depth=3):
    player = game.current
    best_val = float('-inf') if player == 'W' else float('inf')
    best_action = None

    for move in game.available_moves():
        new_game = game.copy()
        new_game.make_move(move)
        val = minimax_with_hef(
            new_game,
            depth - 1,
            maximizing=(player == 'B'),
            player=player,
            evaluate_fn=evaluate_breakthrough
        )
        if (player == 'W' and val > best_val) or (player == 'B' and val < best_val):
            best_val = val
            best_action = move

    return best_action

Breakthrough.print_board = lambda self: print_board(self.board, COLS)

# CLI
def get_input_coord(text):
    while True:
        try:
            i, j = map(int, input(text).strip().split())
            return (i, j)
        except:
            print("Formato inválido. Use: linha coluna (ex: 4 2)")

def play():
    game = Breakthrough()
    human = input("Escolha seu lado (W ou B): ").strip().upper()
    assert human in ['W', 'B']
    ai = 'B' if human == 'W' else 'W'

    print("=== Breakthrough ===")
    game.print_board()

    while not game.game_over():
        print(f"\nTurno: {game.current}")
        if game.current == human:
            while True:
                origem = get_input_coord("Origem (linha coluna): ")
                destino = get_input_coord("Destino (linha coluna): ")
                move = (origem, destino)
                if move in game.available_moves():
                    game.make_move(move)
                    break
                else:
                    print("Movimento inválido.")
        else:
            print("IA pensando...")
            move = best_move(game, depth=3)
            print(f"IA jogou: {move}")
            game.make_move(move)
            time.sleep(0.5)

        game.print_board()

    winner = game.winner()
    if winner == human:
        print(Fore.GREEN + "Você venceu!")
    elif winner == ai:
        print(Fore.RED + "A IA venceu.")
    else:
        print(Fore.CYAN + "Empate.")

if __name__ == "__main__":
    play()
