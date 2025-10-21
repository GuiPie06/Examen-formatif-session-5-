import json, csv
import tkinter as tk
from logging import exception
from tkinter import ttk, messagebox, filedialog
import re

FIELDS = ("produit", "quantite", "prix")

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
        self.rows = []



    def creer_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        content = tk.Frame(self)
        content.grid(row=0, column=0, sticky="new", padx= 10)
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)
        content.rowconfigure(2, weight=1)



        self.labelframe_ajouter = tk.LabelFrame(content, text="Ajouter un produit")
        self.labelframe_ajouter.grid(row=0, column=0, sticky="ew",padx= 10, pady= 10)

        self.labelframe_ajouter.rowconfigure(0, weight=0)
        self.labelframe_ajouter.rowconfigure(1, weight=0)
        self.labelframe_ajouter.rowconfigure(2, weight=0)
        self.labelframe_ajouter.columnconfigure(0, weight=0)
        self.labelframe_ajouter.columnconfigure(1, weight=2)
        self.labelframe_ajouter.columnconfigure(2, weight=0)

        self.label_produit = tk.Label(self.labelframe_ajouter, text="Produit:")
        self.label_produit.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        self.entry_produit = tk.Entry(self.labelframe_ajouter)
        self.entry_produit.grid(row=0, column=1, sticky="ew")

        self.label_quantite = tk.Label(self.labelframe_ajouter, text="Quantité:")
        self.label_quantite.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        self.entry_quantite = tk.Entry(self.labelframe_ajouter)
        self.entry_quantite.grid(row=1, column=1, sticky="ew")

        self.label_prix = tk.Label(self.labelframe_ajouter, text="Quantité:")
        self.label_prix.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        self.entry_prix = tk.Entry(self.labelframe_ajouter)
        self.entry_prix.grid(row=2, column=1, sticky="ew")

        self.bouton_ajouter = tk.Button(self.labelframe_ajouter, text="Ajouter un Produit", command=self.ajouter)
        self.bouton_ajouter.grid(row=1, column=2, sticky="ew", padx=10)




        self.labelframe_gestion = tk.LabelFrame(content, text="Gestion des produits")
        self.labelframe_gestion.grid(row=1, column=0, sticky="ew",padx= 10, pady= 10)

        self.labelframe_gestion.rowconfigure(0, weight=1)
        self.labelframe_gestion.rowconfigure(1, weight=1)
        self.labelframe_gestion.columnconfigure(0, weight=1)
        self.labelframe_gestion.columnconfigure(1, weight=1)
        self.labelframe_gestion.columnconfigure(2, weight=1)
        self.labelframe_gestion.columnconfigure(3, weight=1)

        self.bouton_supprimer = tk.Button(self.labelframe_gestion, text="Supprimer Produit", command=self.supprimer)
        self.bouton_supprimer.grid(row=0, column=0, sticky="", columnspan=2, pady=10)

        self.bouton_modifier = tk.Button(self.labelframe_gestion, text="Modifier Produit", command= self.modifier)
        self.bouton_modifier.grid(row=0, column=2, sticky="", columnspan=2, pady=10)

        self.bouton_sauvgarder_csv = tk.Button(self.labelframe_gestion, text="Sauvgarder CSV")
        self.bouton_sauvgarder_csv.grid(row=1, column=0, sticky="", pady=(10,20))

        self.bouton_sauvgarder_json = tk.Button(self.labelframe_gestion, text="Sauvgarder JSON", command=self.exporterJson)
        self.bouton_sauvgarder_json.grid(row=1, column=1, sticky="", pady=(10,20))

        self.bouton_importer_csv = tk.Button(self.labelframe_gestion, text="Importer CSV")
        self.bouton_importer_csv.grid(row=1, column=2, sticky="", pady=(10,20))

        self.bouton_importer_json = tk.Button(self.labelframe_gestion, text="Importer JSON", command= self.importerJson)
        self.bouton_importer_json.grid(row=1, column=3, sticky="", pady=(10,20))


        self.frame_tableau = tk.Frame(content)
        self.frame_tableau.grid(row=2, column=0, sticky="nsew", padx= 10, pady= 10)

        self.frame_tableau.columnconfigure(0, weight=1)
        self.frame_tableau.rowconfigure(1, weight=1)

        self.tree = ttk.Treeview(self.frame_tableau, columns=("produit", "quantite", "prix"), show="headings")
        self.tree.heading("produit", text="Produit")
        self.tree.heading("quantite", text="Quantité")
        self.tree.heading("prix", text="Prix")

        self.tree.column("produit", width=220)
        self.tree.column("quantite", width=220)
        self.tree.column("prix", width=220)

        self.tree.grid(column=0, row=0, sticky="nsew")


    def ajouter(self):
        produit = self.entry_produit.get()
        quantite = self.entry_quantite.get()
        prix = self.entry_prix.get()
        if not produit:
            messagebox.showwarning("Validation", "Le nom est requis.")
            return
        if quantite and not quantite.isdigit():
            messagebox.showerror("Validation", "Âge doit être un entier.")
            return
        if prix and not prix.isdigit():
            messagebox.showerror("Validation", "Âge doit être un entier.")
            return

        self.tree.insert("", "end", values=(produit, quantite, prix))
        self.rows.append({
            "Produit": produit,
            "Quantité": quantite,
            "Prix": prix
        })
        self.entry_produit.delete(0, "end")
        self.entry_quantite.delete(0, "end")
        self.entry_prix.delete(0, "end")



    def supprimer(self):
        selected_item = self.tree.selection()  # Récupère l'élement sélectionné
        if selected_item:
            self.tree.delete(selected_item)  # Supprime l'élement
        else:
            messagebox.showwarning("Avertissement", "Aucun élement selectionné.")


    def modifier(self):
        selected_item = self.tree.selection()
        if selected_item:
            produit = self.tree.item("produit", selected_item[0])
            quantite = self.tree.item("quantite", selected_item[0])
            prix = self.tree.item("prix", selected_item[0])

            self.entry_produit.delete(0, "end")
            self.entry_produit.insert(0, produit)

            self.entry_quantite.delete(0, "end")
            self.entry_quantite.insert(0, quantite)

            self.entry_prix.delete(0, "end")
            self.entry_prix.insert(0, prix)

            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Avertissement", "Aucun élement selectionné.")

    def exporterJson(self):
        if not self.rows:
            messagebox.showinfo("export json", "Rien à  exporter")
            return
        path = filedialog.asksaveasfilename(title="Exporter Json",defaultextension=".json", filetypes=[("Json", "*.json"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.rows, f, indent=4)
            messagebox.showinfo("export json", "Exporter JSON exported.")
        except exception as e:
            messagebox.showerror("echec export json", str(e))


    def importerJson(self):
        path = filedialog.askopenfilename(title="Importer Json", filetypes=[("Json", "*.json"), ("All files", "*.*")])
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("le json doit contenir unr liste d'objet")
            self.rows = []
            for r in data:
                if isinstance(r, dict):
                    ligne ={}
                    for k in FIELDS:
                        ligne[k] = r.get(k,"")
                    self.rows.append(ligne)
            # self.refresh()
            messagebox.showinfo("importer json", "Importer JSON imported.")
        except exception as e:
            messagebox.showerror("echec importer json", str(e))



if __name__ == "__main__":
    App().mainloop()