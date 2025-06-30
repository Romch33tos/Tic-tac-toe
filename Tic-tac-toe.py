from tkinter import Tk, Menu, Frame, Button, DISABLED, NORMAL, font
from tkinter import messagebox as mb

class TicTacToe:
  def __init__(self):
    self.root = Tk()
    self.root.geometry('265x265')
    self.root.resizable(width=False, height=False)
    self.root.title("Крестики-нолики")
    self.root.configure(bg="white")

    self.root.mainloop()

if __name__ == "__main__":
  game = TicTacToe()
