import tkinter as tk
from tkinter import ttk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry("600x400")
        
        # Logo
        self.logo = tk.PhotoImage(file="logo.png")  # Assurez-vous d'avoir un fichier logo.png dans le même dossier que votre script
        self.logo_label = ttk.Label(self, image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # En-tête
        self.header_label = ttk.Label(self, text="Mon Application", font=("Helvetica", 16, "bold"))
        self.header_label.grid(row=0, column=1, padx=10, pady=10)
        
        # Frame pour afficher les pages
        self.page_frame = ttk.Frame(self)
        self.page_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Boutons de navigation
        self.home_button = ttk.Button(self, text="Accueil", command=self.open_home)
        self.home_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        
        self.encrypt_button = ttk.Button(self, text="Cryptage", command=self.open_encrypt)
        self.encrypt_button.grid(row=0, column=3, padx=10, pady=10, sticky="e")
        
        self.decrypt_button = ttk.Button(self, text="Décryptage", command=self.open_decrypt)
        self.decrypt_button.grid(row=0, column=4, padx=10, pady=10, sticky="e")
        
        # Page d'accueil par défaut
        self.open_home()
        
    def open_home(self):
        self.clear_page_frame()
        home_label = ttk.Label(self.page_frame, text="Bienvenu sur notre logiciel de cryptage et de décryptage")
        home_label.pack()
        
    def open_encrypt(self):
        self.clear_page_frame()
        encrypt_label = ttk.Label(self.page_frame, text="Page de cryptage")
        encrypt_label.pack()
        
    def open_decrypt(self):
        self.clear_page_frame()
        decrypt_label = ttk.Label(self.page_frame, text="Page de décryptage")
        decrypt_label.pack()
        
    def clear_page_frame(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()