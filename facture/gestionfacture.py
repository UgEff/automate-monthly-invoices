import json
import os
import datetime
import time
import sys




class GestionFacture:
    def __init__(self):
        self.tab_facture={}
        self.dat=datetime.datetime.now()
        self.mois = self.dat.date().month
        self.month_lst={1:"JAN",2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN",7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}
        #Pour travailler sur le repertoire data
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'facture.json'))

    # METHODE POUR AJOUTER UNE FACTURE
    def add_facture(self,name,date,account,rising):
        try:
            self.tab_facture[name] = [date, account, rising]
            self.sav_facture()  # Sauvegarder après ajout
        except Exception as e:
            print(f"Erreur : {e}")


    # METHODE POUR SUPPRIMER UN ELEMENT
    #Pour acceder au dictionnaire self.tab_facture
    def delete_facture(self,facture_id):
        if facture_id in self.tab_facture:
            del self.tab_facture[facture_id]
            self.sav_facture()
            print(f"facture {facture_id} supprimé avec succès")
        else:
            print(f"facture {facture_id} non trouvé")

    # METHODE QUI SAUVEGARDE LA FACTURE
    def sav_facture(self):
        a=self.tab_facture
        #root=os.path.join("data","facture.json")
        #root=os.path.dirname(self.file_path)
        if not os.path.exists(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path),exist_ok=True)
        try:
            with open(self.file_path,"w") as outfile:
                json.dump(a,outfile,indent=4)
        except Exception as e:
            print(f"they are error: {e}")

    # METHODE QUI CHARGE LES FACTURES
    def load_facture(self):
        #root=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'facture.json'))
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path,'r') as file:
                    b=json.load(file)
                self.tab_facture=b
                print(f'element chargé {self.tab_facture}')
                print(f'fichier charge depuis: {self.file_path}')
            except Exception as e:
                print(f"they are error: {e}")
        else:
            print("Fichier non existant")
            print(f'error root: {self.file_path}')
        return self.tab_facture

    # METHODE QUI AFFICHE CHAQUE ELEMENTS AVEC SON CONTENU
    def show_facture(self):
        #initialisation dictionnaire vide
        # mois de facturation
        mois_precedent=12 if self.mois==1 else self.mois+1
        a=self.month_lst[mois_precedent]
        output="\n"
        for key in self.tab_facture:
            output+=f"""
            <p>
                Nom : <strong>{key}</strong><br>
                Date Prelevement : <strong>{self.tab_facture[key][0]}-{a}</strong><br>
                Compte : <strong>{self.tab_facture[key][1]}</strong><br>
                Montant : <strong>{self.tab_facture[key][2]} €</strong><br>
            </p>
            
            <hr style="border: none; border-top: 1px dashed #ddd;">
            """
        return output

    #METHODE QUI RENVOIE LE TOTALE
    def total_facture(self):
        tot=[]
        for key in self.tab_facture:
            tot.append(float(self.tab_facture[key][2]))
        total=sum(tot)
        return total


# creation d'une instance 
#gestion=GestionFacture()
# appel de methode dans l'instance 
#gestion.add_facture()
#gestion.add_facture()
#gestion.sav_facture()
#gestion.delete_facture()
#gestion.load_facture()
#gestion.total_facture()
#gestion.load_facture()
#gestion.show_facture()
#gestion.add_facture()
#gestion.total_facture()


