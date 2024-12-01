import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from email_module.email_service import EmailService
from  facture.gestionfacture import GestionFacture
from dotenv import load_dotenv

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'facture.json'))

# Charger les variables d'environnement manuellement

def process_and_send_email():
    load_dotenv()
    instance=GestionFacture()

    # load_facture
    tab_facture = instance.load_facture()
    print(f"load_facture {tab_facture}")

    # show_elements
    elements=instance.show_facture()
    print(f"{elements}")

    # total_facture
    total_facture = round(instance.total_facture(),2)
    print(f"Le total de vos factures est de: {total_facture} €")



    body_email = f"""
        <html>
            <body style="font-family: 'Courier New', Courier, monospace; background-color: #f5f5f5; padding: 20px;">
                <div style="max-width: 400px; margin: auto; background-color: #fff; border: 1px solid #ddd; padding: 15px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                    <h2 style="text-align: center; border-bottom: 2px dashed #333; padding-bottom: 10px;">Récapitulatif des Factures</h2>
                    <div style="border-bottom: 1px dashed #333; margin-bottom: 10px;">
                        {elements}
                    </div>
                    <p style="text-align: right; font-size: 16px;">Total : <strong>{total_facture} €</strong></p>
                    <hr style="border: none; border-top: 1px dashed #333;">
                    <p style="text-align: center; font-size: 12px; color: #555;">Email envoyé automatiquement ne pas répondre</p>
                </div>
            </body>
        </html>
    """



    # Create an instance of the EmailService class

    service_email = EmailService(
        subject="TEST FACTURE",
        body=body_email,
        sender=None,
        recipient=None,
        password=None,
        smtp_server=None,
        port=None,
    )

    try:
        service_email.send_email()
        print(f"Email envoyé avec succès")
    except Exception as e:
        print(f"Erreur lors de l'envoie de mail: {e}")


