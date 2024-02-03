# Mise à jour d'IP Cloudflare

Ce projet est un script Python qui met à jour automatiquement l'adresse IP d'un enregistrement DNS dans Cloudflare. Il est utile lorsque votre adresse IP publique change fréquemment et que vous avez besoin de maintenir à jour un enregistrement DNS pointant vers votre IP actuelle.

## Fonctionnalités

- Récupère l'adresse IP actuelle
- Récupère la configuration actuelle de Cloudflare
- Compare l'adresse IP actuelle avec celle enregistrée dans Cloudflare
- Si l'adresse IP a changé, met à jour l'enregistrement DNS dans Cloudflare
- Envoie des notifications via Ntfy en cas de changement d'adresse IP ou d'erreur

## Dépendances

- `colorama`: Utilisé pour colorer la sortie du terminal
- `json`: Utilisé pour lire le fichier de configuration

## Utilisation

1. Clonez ce dépôt
2. Installez les dépendances avec `pip install -r requirements.txt`
3. Remplir le fichier `config.json`
4. Exécutez le script avec `python main.py`
5. À vous d'utiliser le script selon vos besoins (En cas de redémarrage, avec `cron` etc...)

## Notifications

Ce script utilise Ntfy pour envoyer des notifications. Les notifications sont envoyées dans les cas suivants :

- Lorsque le script est lancé
- Si la configuration de Cloudflare ne peut pas être récupérée
- Si l'adresse IP actuelle ne peut pas être récupérée
- Si l'adresse IP a changé et que l'enregistrement DNS a été mis à jour
- Si l'adresse IP a changé mais que l'enregistrement DNS n'a pas pu être mis à jour
