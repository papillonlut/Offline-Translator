import json

def charger_fichier_traduction(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        return donnees
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return {}
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON dans le fichier {nom_fichier}.")
        return {}

def sauvegarder_fichier_traduction(nom_fichier, donnees):
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

def traduire(mot, langue_source, langue_cible, fichier_traduction):
    if langue_source in fichier_traduction and langue_cible in fichier_traduction[langue_source]:
        traductions = fichier_traduction[langue_source][langue_cible]
        if mot in traductions:
            return traductions[mot]
        else:
            ajout_traduction = input(f"Aucune traduction trouvée pour le mot '{mot}' de {langue_source} vers {langue_cible}. Voulez-vous ajouter une traduction ? (o/n): ")
            if ajout_traduction.lower() == "o":
                nouvelle_traduction = input(f"Entrez la traduction de '{mot}' en {langue_cible} : ")
                fichier_traduction.setdefault(langue_source, {}).setdefault(langue_cible, {})[mot] = nouvelle_traduction
                sauvegarder_fichier_traduction(nom_fichier_traduction, fichier_traduction)
                return f"Traduction ajoutée avec succès : {nouvelle_traduction}"
            else:
                return "Traduction non ajoutée."
    else:
        return f"Aucune traduction disponible de {langue_source} vers {langue_cible}."

# Exemple d'utilisation
nom_fichier_traduction = "trad.json"

# Demander les langues
langue_source = input("Choisissez la langue source : ")
langue_cible = input("Choisissez la langue cible : ")

# Demander le mot
mot_demande = input("Entrez le mot que vous souhaitez traduire : ")

fichier_traduction = charger_fichier_traduction(nom_fichier_traduction)
resultat_traduction = traduire(mot_demande, langue_source, langue_cible, fichier_traduction)

print(resultat_traduction)
