# Business Card Generator

## Description
Cette application Web permet de générer des cartes de visite personnalisées sous forme de fichiers PDF et PNG. L'application est construite à l'aide de Flask pour le backend et ReactPy pour le frontend. Elle offre la possibilité de choisir différents thèmes et polices pour personnaliser l'apparence de la carte de visite.

## Fonctionnalités
🖨️ Génération de cartes de visite : Créez des cartes en format PDF et PNG.
👀 Prévisualisation en temps réel : Voyez les changements au fur et à mesure.
🎨 Personnalisation : Choisissez parmi plusieurs thèmes (light, dark, professional, creative) et polices (Arial, Helvetica, Times New Roman, Courier New).
⬇️ Téléchargement direct : Enregistrez vos cartes directement depuis l'application.

## Installation
### Prérequis:
Python 3.7+
pip
Flask
Pillow
FPDF
ReactPy

## Étapes d'installation

### Clonez ce dépôt :
---bash
git clone https://github.com/NicoNoti/Projet_ReactPy-Python-.git
cd Projet_ReactPy-Python-

### Installez les dépendances :
--bash
pip install -r requirements.txt

### Démarrez le serveur Flask :
--bash
    python app.py
    
    Accédez à l'application dans votre navigateur :
    http://127.0.0.1:5000/

## Utilisation
    Remplissez les champs pour le nom, le titre, la société et l'email.
    Choisissez un thème et une police pour personnaliser la carte de visite.
    Cliquez sur "Générer" pour voir la prévisualisation en temps réel.
    Téléchargez la carte de visite en PDF ou PNG en utilisant les boutons de téléchargement.

## Structure du Projet
    app.py : Fichier principal pour exécuter l'application Flask.
    reactpy_app.py : Contient les fonctions pour générer les fichiers PDF et PNG, ainsi que le composant ReactPy pour l'interface utilisateur.
    reactpy_build/ : Dossier contenant les fichiers de construction du frontend ReactPy.
    index.html : Fichier HTML pour le frontend.

## Dépendances
    Flask : Framework Web pour le backend.
    Pillow : Librairie pour manipuler les images.
    FPDF : Librairie pour générer des fichiers PDF.
    ReactPy : Framework pour créer des interfaces utilisateur réactives.
    Contribution
    Les contributions sont les bienvenues. Veuillez ouvrir une issue ou soumettre une pull request pour toute suggestion ou amélioration.

## Contact
📧 Email : nrarivolala@gmail.com
📞 Téléphone : +261 33 71 244 38, +261 34 93 071 39