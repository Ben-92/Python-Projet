# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv

####Poids###
xpoids5 = []
ypoids5 = []
xpoids25 = []
ypoids25 = []
xpoids50 = []
ypoids50 = []
xpoids75 = []
ypoids75 = []
xpoids95 = []
ypoids95 = []
xmois_mesures = []
ymois_mesures = []

### Récupération des mesures dans les fichiers à faire
#Ouverture du fichier des normes de poids et stockage dans une liste absisses et une liste ordonnées
with open('./Docs-Projet/python-project-trackbaby/constantes-nourrissons-light/poids-age-garcon-0-60-light.csv', newline='') as csvfile:
    fichierlu = csv.reader(csvfile, delimiter=';')
    for row in fichierlu : 
        if row[0] != 'Month' :
            xpoids5.append(int(row[0]))
            ypoids5.append(float(row[1]))

            xpoids25.append(int(row[0]))
            ypoids25.append(float(row[2]))

            xpoids50.append(int(row[0]))
            ypoids50.append(float(row[3]))

            xpoids75.append(int(row[0]))
            ypoids75.append(float(row[4]))

            xpoids95.append(int(row[0]))
            ypoids95.append(float(row[5]))

#ouverture du fichier des mesures et stockage en 2 listes absisse et ordonnées des mesures de poids
with open('./Docs-Projet/python-project-trackbaby/mesures.csv', newline='') as csvfile:
    ficmesures = csv.reader(csvfile, delimiter=';')
    for row in ficmesures : 
        if row[0] != 'Mois' :
            xmois_mesures.append(int(row[0]))
            ymois_mesures.append(float(row[1]))



### Affichage du graphique du poids
plt.subplot(1, 3, 1)
plt.xlabel('Age en mois')
plt.ylabel('Poids en kg')
plt.plot(xpoids5,ypoids5, color='blue', label = '5% poids')
plt.plot(xpoids25,ypoids25, color='orange', label = '25% poids')
plt.plot(xpoids50,ypoids50, color='green', label = '50% poids')
plt.plot(xpoids75,ypoids75, color='red', label = '75% poids')
plt.plot(xpoids95,ypoids95, color='purple', label = '95% poids')
plt.plot(xmois_mesures,ymois_mesures, marker='o', color='black')
plt.legend()

plt.grid()

####Taille###

xtaille5 = []
ytaille5 = []
xtaille25 = []
ytaille25 = []
xtaille50 = []
ytaille50 = []
xtaille75 = []
ytaille75 = []
xtaille95 = []
ytaille95 = []
xmois_mesuresT = []
ymois_mesuresT = []

### Récupération des mesures dans les fichiers à faire
#Ouverture du fichier des normes de taille et stockage dans une liste absisses et une liste ordonnées
with open('./Docs-Projet/python-project-trackbaby/constantes-nourrissons-light/taille-age-garcon-0-60-light.csv', newline='') as csvfile:
    fichierTlu = csv.reader(csvfile, delimiter=';')
    for row in fichierTlu : 
        if row[0] != 'Month' :
            xtaille5.append(int(row[0]))
            ytaille5.append(float(row[1]))

            xtaille25.append(int(row[0]))
            ytaille25.append(float(row[2]))

            xtaille50.append(int(row[0]))
            ytaille50.append(float(row[3]))

            xtaille75.append(int(row[0]))
            ytaille75.append(float(row[4]))

            xtaille95.append(int(row[0]))
            ytaille95.append(float(row[5]))

#ouverture du fichier des mesures et stockage en 2 listes absisse et ordonnées des mesures de taille
with open('./Docs-Projet/python-project-trackbaby/mesures.csv', newline='') as csvfile:
    ficmesuresT = csv.reader(csvfile, delimiter=';')
    for row in ficmesuresT : 
        if row[0] != 'Mois' :
            xmois_mesuresT.append(int(row[0]))
            ymois_mesuresT.append(float(row[2]))


### Affichage du graphique de la taille

plt.subplot(1, 3, 2)
plt.xlabel('Age en mois')
plt.ylabel('Taille en cm')
plt.plot(xtaille5,ytaille5, color='blue', label = '5% taille')
plt.plot(xtaille25,ytaille25, color='orange', label = '25% taille')
plt.plot(xtaille50,ytaille50, color='green', label = '50% taille')
plt.plot(xtaille75,ytaille75, color='red', label = '75% taille')
plt.plot(xtaille95,ytaille95, color='purple', label = '95% taille')
plt.plot(xmois_mesuresT,ymois_mesuresT, marker='o', color='black')
plt.legend()

plt.grid()

####TaillePérimètre cranien###

xpc5 = []
ypc5 = []
xpc25 = []
ypc25 = []
xpc50 = []
ypc50 = []
xpc75 = []
ypc75 = []
xpc95 = []
ypc95 = []
xmois_mesuresPC = []
ymois_mesuresPC = []

### Récupération des mesures dans les fichiers à faire
#Ouverture du fichier des normes de périmètre cranien et stockage dans une liste absisses et une liste ordonnées
with open('./Docs-Projet/python-project-trackbaby/constantes-nourrissons-light/perim-cra-age-garcon-0-60-light.csv', newline='') as csvfile:
    fichierPClu = csv.reader(csvfile, delimiter=';')
    for row in fichierPClu : 
        if row[0] != 'Month' :
            xpc5.append(int(row[0]))
            ypc5.append(float(row[1]))

            xpc25.append(int(row[0]))
            ypc25.append(float(row[2]))

            xpc50.append(int(row[0]))
            ypc50.append(float(row[3]))

            xpc75.append(int(row[0]))
            ypc75.append(float(row[4]))

            xpc95.append(int(row[0]))
            ypc95.append(float(row[5]))

#ouverture du fichier des mesures et stockage en 2 listes absisse et ordonnées des mesures de périmètre cranien
with open('./Docs-Projet/python-project-trackbaby/mesures.csv', newline='') as csvfile:
    ficmesuresPC = csv.reader(csvfile, delimiter=';')
    for row in ficmesuresPC : 
        if row[0] != 'Mois' :
            xmois_mesuresPC.append(int(row[0]))
            ymois_mesuresPC.append(float(row[3]))


### Affichage du graphique du périmètre cranien
plt.subplot(1, 3, 3)
plt.xlabel('Age en mois')
plt.ylabel('Périmètre cranien en cm')
plt.plot(xpc5,ypc5, color='blue', label = '5% périmètre cranien')
plt.plot(xpc25,ypc25, color='orange', label = '25% périmètre craniene')
plt.plot(xpc50,ypc50, color='green', label = '50% périmètre cranien')
plt.plot(xpc75,ypc75, color='red', label = '75% périmètre cranien')
plt.plot(xpc95,ypc95, color='purple', label = '95% périmètre cranien')
plt.plot(xmois_mesuresPC,ymois_mesuresPC, marker='o', color='black')
plt.legend()

plt.grid()
plt.show()