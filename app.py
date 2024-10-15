import tkinter as tk
from gui import PasswordGeneratorApp

def main():
    root = tk.Tk()
    root.title("Password Generator")  # Titre de la fenêtre
    app = PasswordGeneratorApp(root)
    root.geometry("400x400")  # Définir la taille de la fenêtre
    root.mainloop()

if __name__ == "__main__":
    main()
