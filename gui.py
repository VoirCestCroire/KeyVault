import tkinter as tk
from tkinter import messagebox
import random
import string
import json
import os

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        
        # Chemin du fichier JSON pour stocker les mots de passe
        self.password_file = "passwords.json"
        self.password_list = self.load_passwords()  # Charger les mots de passe
        
        # Créer une zone de liste pour afficher les mots de passe
        self.password_listbox = tk.Listbox(master)
        self.password_listbox.pack(pady=20)
        self.update_password_listbox()  # Mettre à jour l'affichage

        # Créer un bouton pour générer un mot de passe
        self.generate_button = tk.Button(master, text="Générer un mot de passe", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Créer un bouton pour supprimer un mot de passe sélectionné
        self.delete_button = tk.Button(master, text="Supprimer le mot de passe", command=self.delete_password)
        self.delete_button.pack(pady=10)

        # Créer un bouton pour copier le mot de passe sélectionné
        self.copy_button = tk.Button(master, text="Copier le mot de passe", command=self.copy_password)
        self.copy_button.pack(pady=10)

    def load_passwords(self):
        """Charge les mots de passe à partir d'un fichier JSON."""
        if os.path.exists(self.password_file):
            with open(self.password_file, "r") as file:
                return json.load(file)
        return []

    def save_passwords(self):
        """Sauvegarde les mots de passe dans un fichier JSON."""
        with open(self.password_file, "w") as file:
            json.dump(self.password_list, file)

    def generate_password(self):
        """Génère un mot de passe aléatoire et l'ajoute à la liste."""
        length = 12  # Longueur du mot de passe
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_list.append(password)  # Ajouter à la liste
        self.update_password_listbox()  # Mettre à jour l'affichage
        self.save_passwords()  # Sauvegarder dans le fichier

    def delete_password(self):
        """Supprime le mot de passe sélectionné de la liste."""
        selected_item = self.password_listbox.curselection()
        if selected_item:
            del self.password_list[selected_item[0]]
            self.update_password_listbox()
            self.save_passwords()  # Sauvegarder dans le fichier

    def copy_password(self):
        """Copie le mot de passe sélectionné dans le presse-papiers."""
        selected_item = self.password_listbox.curselection()
        if selected_item:
            password = self.password_list[selected_item[0]]
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            messagebox.showinfo("Info", "Mot de passe copié dans le presse-papiers.")

    def update_password_listbox(self):
        """Met à jour la zone de liste avec les mots de passe actuels."""
        self.password_listbox.delete(0, tk.END)  # Effacer la liste actuelle
        for password in self.password_list:
            self.password_listbox.insert(tk.END, password)  # Réinsérer les mots de passe
