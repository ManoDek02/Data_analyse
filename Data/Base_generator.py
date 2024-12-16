import random
import pandas as pd
from faker import Faker

# Bibliothèque pour générer des données aléatoires
fake = Faker()

sexes = ["Masculin", "Féminin"]
niveaux_activite = ["Sédentaire", "Modéré", "Actif"]
etats_civils = ["Célibataire", "Marié", "Divorcé", "Veuf"]
professions = ["Ingénieur", "Médecin", "Enseignant", "Artiste", "Comptable"]
niveaux_education = ["Aucun", "Bac", "Licence", "Master", "Doctorat"]

# Liste pour stocker les données
base_de_donnees = []
noms_utilises = set()  # Ensemble pour stocker les noms déjà générés

# Génération des individus
while len(base_de_donnees) < 500:
    sexe = random.choice(sexes)
    nom = fake.name()
    
    # Vérifier si le nom a déjà été utilisé
    if nom not in noms_utilises:
        noms_utilises.add(nom)  # Ajouter le nom à l'ensemble
        individu = {
            "ID": len(base_de_donnees) + 1,
            "Nom": nom,
            "Âge": random.randint(18, 70),
            "Sexe": sexe,
            "Poids": random.randint(50, 100),
            "Taille": random.randint(150, 190),
            "Niveau d'activité": random.choice(niveaux_activite),
            "Consommation de fruits et légumes": random.randint(1, 7),
            "Tabagisme": random.choice(["Oui", "Non"]),
            "Consommation d'alcool": random.randint(0, 10),
            "Adresse": fake.address(),
            "Ville": fake.city(),
            "État/Province": fake.state(),
            "Code postal": fake.zipcode(),
            "État civil": random.choice(etats_civils),
            "Profession": random.choice(professions),
            "Niveau d'éducation": random.choice(niveaux_education),
            "Médicaments": random.choice(["Oui", "Non"]),
            "Antécédents médicaux": fake.text(max_nb_chars=50)
        }
        base_de_donnees.append(individu)


df = pd.DataFrame(base_de_donnees)

# df.to_excel('base_de_donnees.xlsx', index=False, engine='openpyxl')