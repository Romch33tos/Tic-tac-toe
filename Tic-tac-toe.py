from tkinter import Tk, Menu, Frame, Button, DISABLED, NORMAL, font
from tkinter import messagebox as mb

class TicTacToe:
  def __init__(self):
    self.root = Tk()
    self.root.geometry('265x265')
    self.root.resizable(width=False, height=False)
    self.root.title("Крестики-нолики")
    self.root.configure(bg="white")

    self.button_font = font.Font(family="Arial", size=16, weight="bold")

    self.game_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.current_player = 1
    self.move_count = 0
    self.game_over = False

    self.create_menu()
    self.create_game_board()

  def create_menu(self):
    menu_bar = Menu(self.root, bg="white")
    menu_bar.add_command(label="Новая игра", command=self.reset_game)
    self.root.config(menu=menu_bar)

def create_game_board(self):
    self.buttons = []
    board_frames = [Frame(self.root) for _ in range(3)]
   
    for frame in board_frames:
      frame.pack()

    for position in range(9):
      button = Button(
        board_frames[position // 3],
        width=6,
        height=3,
        command=lambda pos=position: self.make_move(pos),
        bg="white",
        font=self.button_font
      )
      button.pack(side="left")
      self.buttons.append(button)

  def make_move(self, position):
    if self.game_board[position] != 0 or self.game_over:
      return

    self.move_count += 1
    self.game_board[position] = self.current_player

    if self.current_player == 1:
      self.buttons[position].configure(
        text="X",
        state=DISABLED,
        disabledforeground="red",
        font=self.button_font  
      )
    else:
      self.buttons[position].configure(
        text="O",
        state=DISABLED,
        disabledforeground="blue",
        font=self.button_font
      )

    self.root.mainloop()

if __name__ == "__main__":
  game = TicTacToe()
