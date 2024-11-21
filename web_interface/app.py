from flask import Flask , render_template, request, redirect, url_for
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from facture.gestionfacture import GestionFacture
from  facture.gestionfacture import GestionFacture


app=Flask(__name__)
#instancier
instance=GestionFacture()

elements=instance.show_facture()
sav_factur=instance.sav_facture
total=instance.total_facture()





@app.route("/")
def show_facture():
    tab_facture = instance.load_facture()
    if not tab_facture:
        print("Aucune facture n'est affiché")
    else:
        print(f"contenu des factures: {tab_facture}")
    return  render_template("home.html",posts=tab_facture)


@app.route("/addfactures", methods=['GET', 'POST'])
def add_facture():
    if request.method == 'POST':
        # Récupérer les données du formulaire avec les bons noms
        name = request.form['name']
        date = request.form['date']
        account = request.form['account']
        rising = request.form['rising']
        
        # Appeler la méthode pour ajouter une facture
        instance.add_facture(name, date, account, rising)
        
        # Rediriger vers la page d'accueil après l'ajout
        return redirect(url_for('show_facture'))
    
    return render_template("add.html")


@app.route("/deletefacture/<facture_id>", methods=['GET', 'POST'])
def delete_facture(facture_id):
    if request.method == 'POST':
        instance.delete_facture(facture_id)
        return redirect(url_for('show_facture'))
    return render_template("delete.html", facture_id=facture_id)