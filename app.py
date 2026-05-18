import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# quantité vendue par région
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')

# quantité vendue par produit
figure2 = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
figure2.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

# chiffre d affaires par produit
print(données.columns.tolist())
print(données.head().to_string()) # methode 'head()' permet l'affichage des 5 premieres lignes du dataframe, 'to_string()' pour afficher toutes les colonnes

ca = données['qte'] * données['prix'] # création d'une nouvelle colonne 'ca' pour le chiffre d'affaires en multipliant la quantité vendue par le prix unitaire
données['ca'] = ca # ajout de la colonne 'ca' au dataframe
figure3 = px.pie(données, values='ca', names='produit', title='chiffre d affaires par produit') # création du graphique pour le chiffre d'affaires par produit en utilisant la nouvelle colonne 'ca' comme valeurs et 'produit' comme noms
figure3.write_html('ca-par-produit.html') # enregistrement du graphique dans un fichier HTML

print('ca-par-produit.html généré avec succès !') # affichage du message de confirmation pour indiquer que le fichier HTML a été généré avec succès

# données