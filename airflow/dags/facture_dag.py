from airflow import DAG
from airflow.operators.python import PythonOperator
import textwrap
from datetime import datetime , timedelta

import os
import sys

# Ajouter le répertoire racine du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from email_module.email_service import EmailService
from email_module.send_email import process_and_send_email
from facture.gestionfacture import GestionFacture

from dotenv import load_dotenv
# Charger les variables d'environnement manuellement
load_dotenv()




default_args={
    "email":["g.didir08@gmail.com"],
    "email_on_retry": False,
    "email_on_failure": True,
    "retries": 2,  
    "retry_delay": timedelta(minutes=5)  
}
# --------------- Definition des call
init_facture=GestionFacture()



with DAG (
    "facture_dag",
    default_args=default_args,
    description="DAG qui gere l'envoie des email automatique",
    schedule="@monthly",
    start_date=datetime(2024,12,1),
    catchup=False,
) as dag:



    t1 = PythonOperator(
        task_id="Envoie_de_mail_automatique",
        python_callable=process_and_send_email,
    )
