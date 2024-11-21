


class Facture:
    def __init__(self,name,date,account,rising):
        self.name=name
        self.date=date
        self.account=account
        self.rising=rising

    # comme show_facture est une methode de class il est important d'ajouter self comme
    # comme argument pour acceder au attribue de la class Facture
    def show_facture(self):
        print(f'This is the information about your bill:\n'
                f'Nom: {self.name}\n'
                f'Date Prelevement: {self.date}\n'
                f'Compte : {self.account}\n'
                f'Montant : {self.rising} €')
        
# initialisation d'une facture
facture1 = Facture("Orange", "04", "Caisse d'epargne", 9.90)
#appel de la methode
facture1.show_facture()
