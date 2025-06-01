from board_game import BoardGame

ROWS, COLS = 8, 8

class Breakthrough(BoardGame):
  def __init__(self):
    super().__init__(ROWS, COLS)
    for j in range(self.cols):
      self.board[0][j] = 'B' #peao preto (duas primeiras linhas)
      self.board[1][j] = 'B'
      self.board[self.rows - 2][j] = 'W' #peao branco (duas ultimas linhas)
      self.board[self.rows - 1][j] = 'W'
    self.current = 'W' #peao branco comeca o jogo

  def available_moves(self):
    moves = []
    if self.current == 'W':
      direction = -1 #anda 'para cima'
    else:
      direction = 1 #anda 'para baixo'
    
    #percorre todas as posicoes do tabuleiro
    for i in range(self.rows):
      for j in range(self.cols):
        if self.board[i][j] == self.current:
          ni = i + direction
          if 0 <= ni < self.rows: #verifica se esta dentro dos limites do tabuleiro
            if self.board[ni][j] == ' ':
              moves.append(((i, j), (ni, j))) #para frente
            if j > 0 and self.board[ni][j-1] not in (' ', self.current):
              moves.append(((i, j), (ni, j - 1))) #para diagonal esquerda
            if j < self.cols - 1 and self.board[ni][j + 1] not in (' ', self.current):
              moves.append(((i, j), (ni, j + 1))) #para diagonal direita
    return moves
  
  def make_move(self, move):
    (i1, j1), (i2, j2) = move
    self.board[i2][j2] = self.board[i1][j1]
    self.board[i1][j1] = ' '
    self.current = 'B' if self.current == 'W' else 'W'
  
# um jogador vence quando um dos seus peoes alcança a linha inicial do adversário
  def winner(self):
    for j in range(self.cols):
      if self.board[0][j] == 'W':
        return 'W'
      if self.board[self.rows - 1][j] == 'B':
        return 'B'
    return None

  def game_over(self):
    """O jogo só acaba quando alguém vence"""
    return self.winner() is not None