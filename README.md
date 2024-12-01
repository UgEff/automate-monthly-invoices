
# 🧾 Gestion de Factures Automatisée

## 📖 Description
**Gestion de Factures Automatisée** est une application Python conçue pour faciliter la gestion des factures. Elle permet l'ajout, la suppression, la sauvegarde, le chargement, et le calcul du total des factures. 

✨ **Fonctionnalités clés** :
- Formatage des factures en HTML pour un affichage ou un envoi par email. 📧
- Interface web locale pour faciliter la saisie et la modification des factures. 💻
- Automatisation avancée avec **Apache Airflow** pour planifier et orchestrer l'envoi des emails. ⏰

---

## ✨ Fonctionnalités
- ➕ **Ajout** de nouvelles factures avec des détails (nom, date de prélèvement, compte associé, montant).
- ❌ **Suppression** des factures existantes.
- 💾 **Sauvegarde** des factures dans un fichier JSON.
- 📂 **Chargement** des factures depuis un fichier JSON existant.
- 🧮 **Calcul** du montant total de toutes les factures.
- 🖋️ **Formatage en HTML** pour un affichage élégant ou un envoi par email.
- 📅 Gestion des **dates de prélèvement** avec affichage du mois suivant.
- 🌐 Interface locale pour une saisie intuitive des factures.
- 🤖 **Orchestration avec Apache Airflow** :
  - Automatisation de l'envoi des emails via des DAGs.
  - Logs détaillés pour suivre les exécutions.
  - Planification flexible (quotidienne, mensuelle...).

---

## 📂 Structure du projet

```
gestion-factures/
├── airflow/                  # Configuration pour Apache Airflow
│   ├── dags/                 # Répertoire contenant les DAGs
│   │   └── facture_dag.py    # DAG pour automatiser l'envoi des emails
│   ├── logs/                 # Logs générés par Apache Airflow
│   ├── plugins/              # Plugins personnalisés (si nécessaire)
│   ├── airflow.cfg           # Fichier de configuration d'Airflow
│   └── airflow.db            # Base de données SQLite pour Airflow
├── data/                     # Répertoire pour stocker les fichiers de données
│   └── facture.json          # Fichier JSON pour la sauvegarde des factures
├── facture/                  # Classes pour la gestion des factures
│   ├── facture.py            # Classe représentant une facture individuelle
│   └── gestionfacture.py     # Classe pour la gestion des collections de factures
├── email_module/             # Services pour l'envoi d'emails
│   ├── email_service.py      # Gestion et envoi des emails
│   └── send_email.py         # Script pour tester l'envoi d'emails
├── web_interface/            # Interface web Flask
│   ├── app.py                # Application principale Flask
│   ├── templates/            # Modèles HTML
│   │   ├── home.html         # Page pour afficher les factures
│   │   ├── add.html          # Page pour ajouter une facture
│   │   └── delete.html       # Page de confirmation de suppression
│   └── static/               # Fichiers statiques (CSS, JS)
│       └── styles.css        # Style CSS pour l'interface
├── scheduler/                # Automatisation et scheduling
│   └── scheduler.py          # Planification des envois automatiques
├── main.py                   # Script principal pour démarrer le projet
├── README.md                 # Documentation du projet
└── requirements.txt          # Dépendances nécessaires
```

---

## 🚀 Automatisation avec Apache Airflow

🔧 **Apache Airflow** est utilisé pour automatiser et orchestrer les envois d'emails liés aux factures. 

### 🛠️ **Principales configurations** :
1. **DAG principal (`facture_dag.py`)** :
   - Automatise l'envoi des emails avec des workflows organisés.
   - Planification flexible (ex. quotidienne, mensuelle).
   - Logs détaillés pour chaque exécution.

2. **Configuration Docker** :
   - Airflow est déployé dans des conteneurs Docker.
   - L'interface web est disponible sur [http://localhost:8080].

### 📝 **Exemple de planification avec Airflow** :
```python
with DAG(
    "facture_dag",
    default_args=default_args,
    description="DAG pour l'envoi automatique des emails liés aux factures",
    schedule_interval="@monthly",
    start_date=datetime(2024, 12, 1),
    catchup=False,
) as dag:
    t1 = PythonOperator(
        task_id="envoie_email_factures",
        python_callable=process_and_send_email,
    )
```

### 🌟 **Avantages d'Airflow** :
- 🔄 Automatisation des tâches répétitives.
- 📊 Logs détaillés pour chaque exécution.
- 🛠️ Planification flexible adaptée aux besoins.


## 📜 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de le modifier et de l'utiliser, mais vous devez mentionner l'auteur original.

---

## ✍️ Auteur

👨‍💻 **Idir (UgEff)**  
💌 Contactez-moi pour toute question ou suggestion !

