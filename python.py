import tkinter as tk
from tkinter import ttk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry("1920x1080")
        
        # Création de l'en-tête avec fond noir
        self.header_frame = ttk.Frame(self, style='Header.TFrame')
        self.header_frame.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        # Configurer la colonne 0 pour s'étendre sur toute la largeur
        self.grid_columnconfigure(0, weight=1)

        # Logo à gauche de l'en-tête
        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = ttk.Label(self.header_frame, image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Cellule vide pour étendre l'en-tête
        self.empty_label = ttk.Label(self.header_frame)
        self.empty_label.grid(row=0, column=1, padx=10, pady=10)
        # Configurer la colonne 1 pour s'étendre sur toute la largeur
        self.header_frame.columnconfigure(1, weight=1)

        # Boutons à droite de l'en-tête
        self.home_button = ttk.Button(self.header_frame, text="Accueil", command=self.open_home)
        self.home_button.grid(row=0, column=2, padx=10, pady=10)

        self.encrypt_button = ttk.Button(self.header_frame, text="Cryptage", command=self.open_encrypt)
        self.encrypt_button.grid(row=0, column=3, padx=10, pady=10)

        self.decrypt_button = ttk.Button(self.header_frame, text="Décryptage", command=self.open_decrypt)
        self.decrypt_button.grid(row=0, column=4, padx=10, pady=10)

        # Styles
        self.style = ttk.Style()
        self.style.configure('Header.TFrame', background='black')

        # Frame pour afficher les pages
        self.page_frame = ttk.Frame(self)
        self.page_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Page d'accueil par défaut
        self.open_home()
        
    def open_home(self):
        self.clear_page_frame()
        
        # Section sous l'en-tête avec fond gris
        home_section = ttk.Frame(self.page_frame, style='Gray.TFrame')
        home_section.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Deux zones de texte empilées verticalement
        text1 = ttk.Label(home_section, text="Zone de texte 1", font=("Helvetica", 16))
        text1.pack(pady=10)
        
        text2 = ttk.Label(home_section, text="Zone de texte 2", font=("Helvetica", 16))
        text2.pack(pady=10)
        
    def open_encrypt(self):
        self.clear_page_frame()

        # Logo au milieu de la page
        encrypt_logo = ttk.Label(self.page_frame, image=self.logo)
        encrypt_logo.pack(padx=20, pady=20)

    def open_decrypt(self):
        self.clear_page_frame()

        # Logo au milieu de la page
        decrypt_logo = ttk.Label(self.page_frame, image=self.logo)
        decrypt_logo.pack(padx=20, pady=20)

    def clear_page_frame(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
