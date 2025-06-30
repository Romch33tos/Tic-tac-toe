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
    self.root.mainloop()

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

    self.check_game_result()
    self.switch_player()

  def switch_player(self):
    self.current_player = 3 - self.current_player  

  def check_game_result(self):
    winning_lines = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],  
      [0, 3, 6], [1, 4, 7], [2, 5, 8],  
      [0, 4, 8], [2, 4, 6]            
    ]

    for line in winning_lines:
      first, second, third = line
      if (self.game_board[first] == self.game_board[second] ==
        self.game_board[third] != 0):
        self.end_game(self.game_board[first])
        return

    if self.move_count == 9:
      self.end_game(0)

  def end_game(self, winner):
    self.game_over = True
    if winner == 1:
      message = "Крестики победили!"
    elif winner == 2:
      message = "Нолики победили!"
    else:
      message = "У вас ничья!"
   
    mb.showinfo(title="Конец игры!", message=message)
    self.disable_all_buttons()

  def disable_all_buttons(self):
    for button in self.buttons:
      button.configure(state=DISABLED)

  def reset_game(self):
    confirm = mb.askyesno(
      title="Новая игра",
      message="Вы действительно хотите начать заново?"
    )
   
    if confirm:
      self.game_board = [0] * 9
      self.current_player = 1
      self.move_count = 0
      self.game_over = False
     
      for position, button in enumerate(self.buttons):
        button.configure(
          state=NORMAL,
          text="",
          command=lambda pos=position: self.make_move(pos),
          font=self.button_font
        )

if __name__ == "__main__":
  game = TicTacToe()
