import time

from colorama import Fore, Style, init
init(autoreset=True)

from breakthrough import Breakthrough
from mcts import mcts
from helper_functions import print_board

def get_input_coord(text):
    while True:
        try:
            i, j = map(int, input(text).strip().split())
            return (i, j)
        except:
            print("Formato inválido. Use: linha coluna (ex: 4 2)")

def play():
    '''
    Função principal para jogar o jogo
    '''
    game = Breakthrough()
    human = input("Escolha seu lado (W ou B): ").strip().upper()
    assert human in ['W', 'B']
    ai = 'B' if human == 'W' else 'W'

    print("=== Breakthrough ===")
    while not game.game_over():
        print_board(game.board, game.cols)
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
            move = mcts(game, iterations=200)
            print(f"IA jogou: {move}")
            game.make_move(move)
            time.sleep(0.5)

    print_board(game.board, game.cols)
    winner = game.winner()
    if winner == human:
        print(Fore.GREEN + "Você venceu!")
    elif winner == ai:
        print(Fore.RED + "A IA venceu.")
    else:
        print(Fore.CYAN + "Empate.")

if __name__ == "__main__":
    play()