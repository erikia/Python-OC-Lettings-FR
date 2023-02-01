[![Python 3.10.2](https://img.shields.io/badge/python-3.10.2-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Docker](https://img.shields.io/badge/Docker-powered-blue.svg)](https://www.docker.com/)
[![CircleCI](https://img.shields.io/badge/CircleCI-built-brightgreen.svg)](https://circleci.com/)
[![Heroku](https://img.shields.io/badge/Heroku-deployed-purple.svg)](https://heroku.com/)


## Résumé

Site web d'Orange County Lettings

### Status

[![CircleCI](https://circleci.com/gh/erikia/Python-OC-Lettings-FR/tree/master.svg?style=svg)](https://circleci.com/gh/erikia/Python-OC-Lettings-FR/tree/master)

## Quick Access

1. [Informations](#informations)
2. [Développement local](#développement-local)
3. [Déploiement](#déploiement)

## Informations
Ce projet est le livrable du 13ème projet du cours de développement d'application Python d'OpenClassrooms. 
Il s'agit d'une application développée en utilisant le framework Python Django. 

Ce projet utilise les technologies Heroku, CircleCI et Docker pour le déploiement. 
La première étape consiste à lancer les tests du projet et le linting. 
La seconde étape effectue une conteneurisation via Docker. 
La dernière étape permet le déploiement sur Heroku.


## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement
Voici les étapes pour le déploiement d'une application avec Heroku:

Lancer les tests du projet et le linting
Effectuer une conteneurisation via docker
Déployer sur Heroku
Pour se connecter à Heroku, utilisez les commandes suivantes :

- `heroku login`
- `heroku container:login`
- `heroku create <NOMDUPROJET:oc-lettings-26>`

Les variables d'environnement peuvent être déclarées dans un fichier .env pour l'exécution locale ou sur les plateformes CircleCI ou Heroku pour un déploiement en ligne. Pour obtenir le `HEROKU_TOKEN`, tapez la commande suivante :

- `heroku authorizations:create`

Variables dans CircleCI:
| CircleCI variable | Description                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------|
| DOCKER_USERNAME   | Nom d'utilisateur pour le compte Docker                                                          |
| DOCKER_PASSWORD   | Mot de passe pour le compte Docker                                                               |
| CIRCLE_SHA1       | Référence de code (SHA1) pour la version actuelle du code                                        |
| HEROKU_API_KEY    | Clé API Heroku                                                                                   |
| HEROKU_TOKEN      | Token Heroku qui peut être trouver avec la commande précedente                                   |

Variables dans Heroku:
| Heroku variable   | Description                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------|
| PORT              | 8000                                                                                             |

Ces variables sont utilisées dans les étapes suivantes :

docker-build : utilisées pour se connecter à Docker et construire/pousser l'image Docker
heroku-deploy : utilisées pour se connecter à Heroku et déployer le conteneur.

Pour déployer une image Docker avec l'intégration continue il suffit de faire un push pour que Circle CI fasse l'image, il faut la relier à son compte Docker et lancer la commande suivante :

- `docker run -d --name django-heroku -e "PORT=8000" -e "DEBUG=1" -p 8000:8000 $DOCKER_USERNAME/oc_lettings:$CIRCLE_SHA1`

On peut également la construire manuellement avec cette commande : 

- `docker build -t $DOCKER_USERNAME/oc-lettings:$CIRCLE_SHA1`

Aller sur le site en local:  `http://localhost:8000/`

Lien du pipeline actuel:

https://app.circleci.com/pipelines/github/erikia/Python-OC-Lettings-FR?invite=true

Lien vers le site sur Heroku:

https://oc-lettings-26.herokuapp.com/

Lien du Sentry:

https://sentry.io/organizations/k-0/projects/oc-lettings/?project=4504561969332224
