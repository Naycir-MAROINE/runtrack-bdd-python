import mysql.connector
from tkinter import Tk, ttk, Label, Button, messagebox, Entry

class GestionStock:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock")

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="store"
        )
        self.cursor = self.conn.cursor()

        self.label = Label(root, text="Gestion de Stock")
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        self.tree = ttk.Treeview(root, columns=("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"))
        self.tree.grid(row=1, column=0, columnspan=4, pady=10)
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Nom")
        self.tree.heading("#2", text="Description")
        self.tree.heading("#3", text="Prix")
        self.tree.heading("#4", text="Quantité")
        self.tree.heading("#5", text="Catégorie")

        self.btn_ajouter = Button(root, text="Ajouter", command=self.ajouter_produit)
        self.btn_ajouter.grid(row=2, column=0, padx=10)

        self.btn_supprimer = Button(root, text="Supprimer", command=self.supprimer_produit)
        self.btn_supprimer.grid(row=2, column=1, padx=10)

        self.btn_modifier = Button(root, text="Modifier", command=self.modifier_produit)
        self.btn_modifier.grid(row=2, column=2, padx=10)

        self.remplir_tableau()
        self.root.mainloop()

    def remplir_tableau(self):
        self.cursor.execute("SELECT * FROM product")
        produits = self.cursor.fetchall()

        for produit in produits:
            self.tree.insert("", "end", values=produit)

    def ajouter_produit(self):
        # Fenêtre de dialogue pour saisir les détails du nouveau produit
        popup = Tk()
        popup.title("Ajouter un Produit")

        # Labels et Entry pour chaque attribut du produit
        label_nom = Label(popup, text="Nom:")
        label_nom.grid(row=0, column=0)
        entry_nom = Entry(popup)
        entry_nom.grid(row=0, column=1)

        label_description = Label(popup, text="Description:")
        label_description.grid(row=1, column=0)
        entry_description = Entry(popup)
        entry_description.grid(row=1, column=1)

        label_prix = Label(popup, text="Prix:")
        label_prix.grid(row=2, column=0)
        entry_prix = Entry(popup)
        entry_prix.grid(row=2, column=1)

        label_quantite = Label(popup, text="Quantité:")
        label_quantite.grid(row=3, column=0)
        entry_quantite = Entry(popup)
        entry_quantite.grid(row=3, column=1)

        label_categorie = Label(popup, text="Catégorie:")
        label_categorie.grid(row=4, column=0)
        entry_categorie = Entry(popup)
        entry_categorie.grid(row=4, column=1)

        # Fonction pour ajouter le produit à la base de données
        def ajouter():
            nom = entry_nom.get()
            description = entry_description.get()
            prix = entry_prix.get()
            quantite = entry_quantite.get()
            categorie = entry_categorie.get()

            # Ajouter le produit à la base de données
            self.cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                                (nom, description, prix, quantite, categorie))
            self.conn.commit()

            # Rafraîchir le tableau et fermer la fenêtre de dialogue
            self.tree.delete(*self.tree.get_children())
            self.remplir_tableau()
            popup.destroy()

        # Bouton pour ajouter le produit
        btn_ajouter = Button(popup, text="Ajouter", command=ajouter)
        btn_ajouter.grid(row=5, column=0, columnspan=2, pady=10)

        popup.mainloop()

    def supprimer_produit(self):
        selected_item = self.tree.selection()
        if selected_item:
            id_produit =self.tree.item(selected_item,"values")[0]
            id_produit = int(id_produit)
            self.cursor.execute("DELETE FROM product WHERE id = %s", (id_produit,))
            self.conn.commit()
            self.tree.delete(selected_item)

    def modifier_produit(self):
        selected_item = self.tree.selection()
        if selected_item:
            id_produit = self.tree.item(selected_item,"values")[0]
            id_produit = int(id_produit)
            #popup = Tk()
            #popup.title("Modifier un Produit")
            self.cursor.execute("SELECT * FROM product WHERE id = %s", (id_produit,))
            produit = self.cursor.fetchone()
            popup = Tk()
            popup.title("Modifier un Produit")
           

            # Labels et Entry pour chaque attribut du produit
            label_nom = Label(popup, text="Nom:")
            label_nom.grid(row=0, column=0)
            entry_nom = Entry(popup)
            entry_nom.grid(row=0, column=1)
            entry_nom.insert(0, produit[1])  # Remplir avec le nom du produit sélectionné

            label_description = Label(popup, text="Description:")
            label_description.grid(row=1, column=0)
            entry_description = Entry(popup)
            entry_description.grid(row=1, column=1)
            entry_description.insert(0, produit[2])  # Remplir avec la description du produit sélectionné

            label_prix = Label(popup, text="Prix:")
            label_prix.grid(row=2, column=0)
            entry_prix = Entry(popup)
            entry_prix.grid(row=2, column=1)
            entry_prix.insert(0, produit[3])  # Remplir avec le prix du produit sélectionné

            label_quantite = Label(popup, text="Quantité:")
            label_quantite.grid(row=3, column=0)
            entry_quantite = Entry(popup)
            entry_quantite.grid(row=3, column=1)
            entry_quantite.insert(0, produit[4])  # Remplir avec la quantité du produit sélectionné

            label_categorie = Label(popup, text="Catégorie:")
            label_categorie.grid(row=4, column=0)
            entry_categorie = Entry(popup)
            entry_categorie.grid(row=4, column=1)
            entry_categorie.insert(0, produit[5])  # Remplir avec la catégorie du produit sélectionné

            # Fonction pour modifier le produit dans la base de données
            def modifier():
                nom = entry_nom.get()
                description = entry_description.get()
                prix = entry_prix.get()
                quantite = entry_quantite.get()
                categorie = entry_categorie.get()

                # Modifier le produit dans la base de données
                self.cursor.execute("UPDATE product SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s WHERE id=%s",
                                    (nom, description, prix, quantite, categorie, id_produit))
                self.conn.commit()

                # Rafraîchir le tableau et fermer la fenêtre de dialogue
                self.tree.delete(*self.tree.get_children())
                self.remplir_tableau()
                popup.destroy()

            # Bouton pour modifier le produit
            btn_modifier = Button(popup, text="Modifier", command=modifier)
            btn_modifier.grid(row=5, column=0, columnspan=2, pady=10)

            popup.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = GestionStock(root)

