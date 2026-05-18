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

# ca = données['qte'] * données['prix'] # création d'une nouvelle colonne 'ca' pour le chiffre d'affaires en multipliant la quantité vendue par le prix unitaire
# données['ca'] = ca # ajout de la colonne 'ca' au dataframe
# figure3 = px.pie(données, values='ca', names='produit', title='chiffre d affaires par produit') # création du graphique pour le chiffre d'affaires par produit en utilisant la nouvelle colonne 'ca' comme valeurs et 'produit' comme noms
# figure3.write_html('ca-par-produit.html') # enregistrement du graphique dans un fichier HTML
# print('ca-par-produit.html généré avec succès !') # affichage du message de confirmation pour indiquer que le fichier HTML a été généré avec succès


# tests manipulation dataframe

dim = données.shape # dimensions du dataframe
print(dim[0]) # nombre de lignes: 39
print(dim[1]) # nombre de colonnes: 5

typesDatas = données.dtypes
print(typesDatas) # affichage des types de données de chaque colonne du dataframe

# numpyArray = données.values # affichage des valeurs du dataframe sous forme de tableau numpy
# print(numpyArray)

# données[['qte', 'prix']] = données[['qte', 'prix']].apply(pd.to_numeric) # conversion des colonnes 'qte' et 'prix' en types numériques pour permettre les calculs
qtePrixDatas = données[['qte', 'prix']] # sélection des colonnes 'qte' et 'prix' du dataframe pour les afficher séparément
print(qtePrixDatas) # affichage des données des colonnes 'qte' et 'prix' 

# création d'une nouvelle colonne 'chiffre_affaires' ds notre dataframe
données['chiffre_affaires'] = données['qte'] * données['prix'] # création en multipliant les colonnes 'qte' et 'prix' pour calculer le chiffre d'affaires
print(données) # affichage du dataframe avec la nouvelle colonne 'chiffre_affaires' pour vérifier que les calculs ont été effectués correctement

# dataSortByProducts = données.sort_values(['produit'])
# print(dataSortByProducts)

figure3 = données.groupby('produit')['chiffre_affaires'].sum().reset_index() # regroupement des données par produit, calcul du chiffre d'affaires total pour chaque produit, et réinitialisation de l'index pour obtenir un DataFrame propre
# print(figure3) # affichage du DataFrame regroupé pour vérifier les calculs du chiffre d'affaires par produit
figure3 = px.bar(figure3, x='produit', y='chiffre_affaires', title='chiffre d affaires par produit') # création du graphique à barres pour afficher le chiffre d'affaires par produit en utilisant le DataFrame regroupé
figure3.write_html('chiffre-d-affaires-par-produit.html') # enregistrement du graphique dans un fichier HTML
print('chiffre-d-affaires-par-produit.html généré avec succès !') # affichage du message de confirmation pour indiquer que le fichier HTML a été généré avec succès
