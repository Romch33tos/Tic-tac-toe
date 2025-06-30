from tkinter import Tk, Menu, Frame, Button, DISABLED, NORMAL, font
from tkinter import messagebox as mb

class TicTacToe:
  def __init__(self):
    self.root = Tk()
    self.root.geometry('265x265')
    self.root.resizable(width=False, height=False)
    self.root.title("Крестики-нолики")
    self.root.configure(bg="white")

   self.create_menu()

  def create_menu(self):
    menu_bar = Menu(self.root, bg="white")
    menu_bar.add_command(label="Новая игра", command=self.reset_game)
    self.root.config(menu=menu_bar)

    self.root.mainloop()

if __name__ == "__main__":
  game = TicTacToe()
