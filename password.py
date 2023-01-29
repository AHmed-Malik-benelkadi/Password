#!/usr/bin/python
# encoding: utf-8
#  ╔═══════════════════════════════════════╗
#  ║               Passwords               ║
#  ║               Crée par                ║
#  ║          Ahmed Malik Ben elkadi       ║
#  ╚═══════════════════════════════════════╝

# Tous les commentaires seront en français et les noms de variables seront en anglais

# import des modules nécessaire

import hashlib as hash
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

""" numbers, lowercase et uppercase sont des variables globales,
 utilisées pour stocker le nombre de caractères de chaque type dans le mot de pass"""
numbers = ""
lowercase = ""
uppercase = ""


# fonction pour verifier la validité du mot de passe
def check_password(password):
    global numbers, lowercase, uppercase
    for char in password:
        if char.isdigit():  # vérifier si le caractère est un chiffre et l'ajouter à la variable des nombres
            numbers += char
    for char in password:
        if char.islower():  # vérifie si le caractère est une minuscule et l'ajoute à la variable minuscule
            lowercase += char
    for char in password:
        if char.isupper():  # vérifier si le caractère est une majuscule et l'ajouter à la variable uppercase
            uppercase += char
    special = ''.join([x for x in password if not x.isalnum()])
    min_length = 8  # longueur minimale du mot de passe

    # vérifie si le mot de passe répond à toutes les exigences et retourne False si aucune n'est remplie
    if not password or not numbers or not lowercase or not uppercase or not special or len(password) < min_length:  #
        if not password:
            messagebox.showerror("Erreur", "Vous avez laissé la case du mot de passe vide.")
        elif len(password) < min_length:
            messagebox.showerror("Erreur", "Le mot de passe doit comporter au moins 8 caractères.")
        elif not numbers:
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins un chiffre.")
        elif not lowercase:
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins une lettre minuscule.")
        elif not uppercase:
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins une lettre majuscule.")
        elif not special:
            messagebox.showerror("Error", "Le mot de passe doit contenir au moins un caractère spécial.")
        return False
    else:
        return True


def add_password():
    # Obtenir les valeurs des entrées : noms d'utilisateur et mot de passe
    username = username_entry.get()
    password = password_entry.get()
    # Vérifier si le mot de passe est valide
    if check_password(password):
        print("\nMot de passe accepté !\n")

        # Hachez le mot de passe
        hashed_password = hash.sha256(password.encode())

        # Vérifier si le nom d'utilisateur existe déjà dans le dictionnaire des utilisateurs.
        if username in users:
            # Si le mot de passe haché existe déjà pour l'utilisateur, afficher un message d'erreur.
            if hashed_password.hexdigest() in users[username]:
                messagebox.showerror("Erreur", "Ce mot de passe a déjà été enregistré pour cet utilisateur.")
                return False
            # Si le mot de passe haché n'existe pas pour l'utilisateur, ajoutez-le à la liste.
            else:
                users[username].append(hashed_password.hexdigest())
                # Enregistrer le dictionnaire mis à jour dans le fichier json
                with open("src/users.json", "w") as file:
                    json.dump(users, file, separators=(',', ': '), indent=4)

                messagebox.showinfo("Succès ", "Mot de passe ajouté avec succès pour l'utilisateur " + username + "!")
        # Si le nom d'utilisateur n'existe pas dans le dictionnaire, créez une nouvelle entrée.
        else:
            users[username] = [hashed_password.hexdigest()]
            with open("src/users.json", "w") as file:
                json.dump(users, file, separators=(',', ': '), indent=4)
            messagebox.showinfo("Succès ", "Mot de passe ajouté avec succès pour l'utilisateur " + username + "!")


def check_password_complexity(password):
    global numbers, lowercase, uppercase
    i = 0
    # Vérifier les chiffres dans le mot de passe
    while i < len(password):
        if password[i].isdigit():
            numbers += password[i]
        i += 1

    for char in password:
        if char.islower():
            lowercase += char

    for char in password:
        if char.isupper():
            uppercase += char

    special = ''.join([x for x in password if not x.isalnum()])

    min_length = 8
    # Initialiser une variable pour stocker le niveau de complexité du mot de passe
    complexity_level = 0

    if len(password) >= min_length:
        complexity_level += 1

    if numbers:
        complexity_level += 1

    if lowercase:
        complexity_level += 1

    if uppercase:
        complexity_level += 1

    if special:
        complexity_level += 1
    # return le niveau de complexité du mot de passe
    return complexity_level


def update_password_strength(event):
    password = password_entry.get()
    complexity = check_password_complexity(password)
    password_strength.config(value=complexity)


try:
    with open('src/users.json', 'r') as f:
        users = json.load(f)
except:
    users = {}

""" --------------------------------GUI interface graphique ---------------------------------"""

window = tk.Tk()
window.title("Password ")
window.configure(background="azure")
window.geometry("520x280")
window.minsize(280, 160)
window.iconbitmap("src/key_password_lock_800.ico")

label_title = tk.Label(window, text="Bienvenue ! ", font=("Courrier", 30), background="azure",
                           fg='black')
label_title.pack(pady=10)
username_label = tk.Label(window, text="Entrez votre nom d'utilisateur: ")
username_label.pack(pady=10)
username_entry = tk.Entry(window)
username_entry.pack(pady=5)
password_label = tk.Label(window, text=" Entrer votre mot de passe :")
password_label.pack(pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

password_entry.bind("<KeyRelease>", update_password_strength)
password_strength = ttk.Progressbar(window, orient="horizontal", length=200, maximum=5, value=0, )
password_strength.pack(pady=5)

add_button = tk.Button(window, text="AJOUTER", command=add_password, background="azure")
add_button.pack(pady=10)

window.mainloop()

