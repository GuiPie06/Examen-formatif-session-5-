import tkinter as tk
from tkinter import ttk


class Produit:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


@property
def name(self):
    return self.__name


@name.setter
def name(self, nom):
    if not isinstance(nom, str):
        raise ValueError("Le nom n'est pas un string")
    self.__name = nom











class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des Produits")
        self.geometry("700x600")


        self.creer_widgets()



    def creer_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        content = tk.Frame(self)
        content.grid(row=0, column=0, sticky="new")
        content.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)
        content.columnconfigure(1, weight=1)



        self.labelframe_ajouter = tk.LabelFrame(content, text="Ajouter un produit")
        self.labelframe_ajouter.grid(row=0, column=0, sticky="ew")

        self.labelframe_ajouter.rowconfigure(0, weight=1)
        self.labelframe_ajouter.rowconfigure(1, weight=1)
        self.labelframe_ajouter.rowconfigure(2, weight=1)
        self.labelframe_ajouter.columnconfigure(0, weight=1)
        self.labelframe_ajouter.columnconfigure(1, weight=2)
        self.labelframe_ajouter.columnconfigure(2, weight=1)

        self.label_produit = tk.Label(self.labelframe_ajouter, text="Produit:")
        self.label_produit.grid(row=0, column=0, sticky="ew")
        self.entry_produit = tk.Entry(self.labelframe_ajouter)
        self.entry_produit.grid(row=0, column=1, sticky="ew")

        self.label_quantite = tk.Label(self.labelframe_ajouter, text="Quantité:")
        self.label_quantite.grid(row=1, column=0, sticky="ew")
        self.entry_quantite = tk.Entry(self.labelframe_ajouter)
        self.entry_quantite.grid(row=1, column=1, sticky="ew")

        self.label_prix = tk.Label(self.labelframe_ajouter, text="Quantité:")
        self.label_prix.grid(row=2, column=0, sticky="ew")
        self.entry_prix = tk.Entry(self.labelframe_ajouter)
        self.entry_prix.grid(row=2, column=1, sticky="ew")

        self.bouton_ajouter = tk.Button(self.labelframe_ajouter, text="Ajouter un Produit")
        self.bouton_ajouter.grid(row=1, column=2, sticky="ew")




        self.labelframe_gestion = tk.LabelFrame(content, text="Gestion des produits")
        self.labelframe_gestion.grid(row=1, column=0, sticky="ew")

        self.bouton_supprimer = tk.Button(self.labelframe_gestion, text="Supprimer Produit")
        self.bouton_supprimer.grid(row=0, column=0, sticky="", columnspan=2)

        self.bouton_modifier = tk.Button(self.labelframe_gestion, text="Modifier Produit")
        self.bouton_modifier.grid(row=0, column=2, sticky="", columnspan=2)

        self.bouton_sauvgarder_csv = tk.Button(self.labelframe_gestion, text="Sauvgarder CSV")
        self.bouton_sauvgarder_csv.grid(row=1, column=0, sticky="")

        self.bouton_sauvgarder_json = tk.Button(self.labelframe_gestion, text="Sauvgarder JSON")
        self.bouton_sauvgarder_json.grid(row=1, column=1, sticky="")

        self.bouton_importer_csv = tk.Button(self.labelframe_gestion, text="Importer CSV")
        self.bouton_importer_csv.grid(row=1, column=2, sticky="")

        self.bouton_importer_json = tk.Button(self.labelframe_gestion, text="Importer JSON")
        self.bouton_importer_json.grid(row=1, column=3, sticky="")


        self.frame_tableau = tk.Frame(content)
        self.frame_tableau.grid(row=2, column=0, sticky="nsew")

        self.tree = ttk.Treeview(self.frame_tableau, columns=("produit", "quantite", "prix"), show="headings")
        self.tree.heading("produit", text="Produit")
        self.tree.heading("quantite", text="Quantité")
        self.tree.heading("prix", text="Prix")

        self.tree.column("produit", width=220)
        self.tree.column("quantite", width=220)
        self.tree.column("prix", width=220)

        self.tree.grid(column=0, row=0, sticky="nsew")




if __name__ == "__main__":
    App().mainloop()