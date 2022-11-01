import json 
import random
from select import select


order = "random"


# Menu

while(1):
    print("1 - Commencer")
    print("2 - Configurer")

    menuSelect = int(input())

    match menuSelect:
        case 1:
            break
        case 2:
            while(1):
                print("Configuration actuel : {}".format(order))
                print("1 - Aléatoire")
                print("2 - Traduire un mot anglais")
                print("3 - Traduire un mot français")
                print("9 - Revenir en arrière")

                subMenuSelect = int(input())

                match subMenuSelect:
                    case 1:
                        order = "random"
                    case 2:
                        order = "en"
                    case 3:
                        order = "fr"
                    case 9:
                        break

# Ouverture du fichier json
with open("fren.json", 'r') as file:

    # Transformation json vers dict
    dict = json.load(file)
    lenDict = (len(dict))

    while(1):
        print("\n=== Appuyer sur x pour quitter ===\n")
        # Choix aléatoire d'un mot dans le dict
        randNum = random.randint(1, (lenDict))
        words = dict[str(randNum)]
        
        # Choix aléatoire de l'ordre
        if (random.randint(0,1) and order == "random") or order == "en":
            lang = "en"
            question = list(words.keys())[1]
            answer = list(words.keys())[0]
        else:
            lang = "fr"
            question = list(words.keys())[0]
            answer = list(words.keys())[1]

        # Affiche la question
        print(lang + " : " + words[str(question)])


        userChoice = input("Entrer la réponse : ")

        if userChoice == "x":
            break
        if userChoice == "h":
            print("h : Help")
            print("x : quitter")

        if (words[str(answer)]).lower() == userChoice.lower():
            print("GG")
        else:
            print("La bonne réponse est  : {}".format(words[str(answer)]))