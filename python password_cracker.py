import tkinter as tk
from tkinter import filedialog

import hashlib
import random


class PasswordCracker(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Password Cracker")

        # Create the hash entry field.
        self.hash_entry = tk.Entry(self)
        self.hash_entry.pack()

        # Create the wordlist entry field.
        self.wordlist_entry = tk.Entry(self)
        self.wordlist_entry.pack()

        # Create the crack button.
        self.crack_button = tk.Button(self, text="Crack", command=self.crack)
        self.crack_button.pack()

        # Create the status label.
        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def crack(self):
        # Get the hash from the entry field.
        hash = self.hash_entry.get()

        # Get the wordlist from the entry field.
        wordlist = self.wordlist_entry.get()

        # Create a list of passwords from the wordlist.
        passwords = open(wordlist, "r").readlines()

        # Start cracking the password.
        for password in passwords:
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash:
                self.status_label.config(text="Password cracked:", fg="green")
                self.status_label.config(text=password, fg="black")
                return

        # The password could not be cracked.
        self.status_label.config(text="Password could not be cracked.", fg="red")


if __name__ == "__main__":
    # Create the password cracker GUI.
    password_cracker = PasswordCracker()
    password_cracker.mainloop()

