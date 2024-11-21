
# Gestion de Factures Automatisée

## Description
**Gestion de Factures Automatisée** est une application Python conçue pour faciliter la gestion des factures. Elle permet l'ajout, la suppression, la sauvegarde, le chargement, et le calcul du total des factures. L'application propose aussi un formatage des détails des factures en HTML pour l'envoi par email. Une interface web locale sera ajoutée pour faciliter la saisie et la modification des factures. Des fonctionnalités d'automatisation avancées avec Apache Airflow et un scheduling flexible sont prévues pour automatiser l'envoi des emails.

## Fonctionnalités
- Ajout de nouvelles factures avec des détails tels que le nom, la date de prélèvement, le compte associé et le montant.
- Suppression des factures existantes.
- Sauvegarde des factures dans un fichier JSON.
- Chargement des factures depuis un fichier JSON existant.
- Calcul du montant total de toutes les factures.
- Formatage en HTML pour un affichage élégant ou un envoi par email.
- Affichage du mois suivant pour les dates de prélèvement, avec une gestion du passage de décembre à janvier.
- Interface locale pour une saisie et modification plus intuitive des factures.

## Structure du projet
```
gestion-factures/
├── data/                     # Répertoire pour stocker les fichiers de données
│   └── facture.json          # Fichier JSON pour la sauvegarde des factures
├── facture/                  # Répertoire pour les classes de |gestion des factures
│   ├── facture.py            # Classe représentant une facture individuelle
│   └── gestionfacture.py     # Classe pour la gestion des collections de factures
├── email/                    # Répertoire pour les services d'email
│   ├── email_service.py      # Classe pour la gestion et l'envoi des emails
│   └── send_email.py         # Script pour tester l'envoi d'emails
├── web_interface/            # Répertoire pour l'interface web Flask
│   ├── app.py                # Application principale Flask
│   ├── templates/            # Dossier pour les modèles HTML
│   │   ├── home.html         # Page pour afficher les factures
│   │   ├── add.html          # Page pour ajouter une facture
│   │   └── delete.html       # Page de confirmation de suppression (optionnel)
│   └── static/               # Dossier pour les fichiers statiques (CSS, JS)
│       └── styles.css        # Fichier CSS pour styliser l'interface (optionnel)
├── scheduler/                # Répertoire pour l'automatisation et le scheduling
│   └── scheduler.py          # Script pour planifier l'envoi automatique d'emails
├── main.py                   # Script principal pour démarrer le projet
├── README.md                 # Document de présentation du projet
└── requirements.txt          # Fichier pour les dépendances 

```

- **Envoyer un email** :
   Creer un fichier .env contenant vos infos smtp
   Lancez le script `test_email.py` pour envoyer un email contenant les détails des factures.

## Roadmap
Le projet est en constante évolution et inclura bientôt :
- **Automatisation avec Apache Airflow** : Planifier et orchestrer l'envoi automatique des emails.
- **Scheduling avancé** : Mettre en place un système flexible pour l'envoi automatique des emails.
- **.exe** : Creation d'un exe afin de faciliter le lancement en local afin de faire les modifications


## Licence
Ce projet est sous licence **MIT**. Vous êtes libre de le modifier et de l'utiliser, mais vous devez mentionner l'auteur original.

## Auteur
**Idir (UgEff)**
