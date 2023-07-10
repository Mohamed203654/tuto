from math import*
from colorama import Fore, Back, Style
from art import *

print(Fore.GREEN + "TP PYTHON")
print(Back.GREEN + "CONSULTANT JUBA")
print(Style.BRIGHT + "MINI TP")


art = text2art("TP PYTHON")
print(art)
print("ok")
print("okok")


name = input("entrer votre nom ! : ")
print(" Bonjour,je m'appelle " +name)
#----------------------------------------------------------------------------------------------
note_math = float(input(" entrer la note du math : "))
note_Geo = float(input(" entrer la note du  Geo : "))
note_Sciences = float(input(" entrer la note du Sciences : "))
note_Francais = float(input(" entrer la note du Francais : "))

moyenne = (note_math+note_Geo+note_Sciences+note_Francais)/4

print("Ma moyenne génerale est de : " +str(moyenne))
#----------------------------------------------------------------------------------------------

notes = []
matieres = ["Math", "Geo", "Science", "Français"]
for matiere in matieres:
 note = float(input("Quelle est votre note en {}? ".format(matiere)))
 notes.append(note)
# Calculer la moyenne des notes
moyenne = sum(notes) / len(notes)
# Afficher la moyenne
print("Votre moyenne générale est de :", moyenne)

#-------------------------------------------------------------------------------------------
Wallet = float(input("saisir montant Wallet: "))
Prix = float(input("saisir le prix de pc :" ))

if Wallet >= Prix :
 print("tu peux acheter ton pc ")
else:
 print("tu peux pas ")

#------------------------------------------------------------------------------------------------

Liste_animaux = ["Chat","Chien","Lapin","Cheval"]
nvelement = "lion"
Liste_animaux.insert(1,nvelement)
print(Liste_animaux)
print(Liste_animaux[1],Liste_animaux[4])

Liste_animaux.append("elephant")
print(Liste_animaux)
Liste_animaux.remove("lion")
Liste_animaux.remove(Liste_animaux[2])
print(Liste_animaux)

#------------------------------------------------------------------------------------------------------

Liste_client = [2,4,6,8,9,7]
print(Liste_client)

print("vous etes le client " , Liste_client[0] )
print("vous etes le client " , Liste_client[1] )
print("vous etes le client " , Liste_client[2] )
print("vous etes le client " , Liste_client[3] )
print("vous etes le client " , Liste_client[4] )


for element in Liste_client : 
    print("vous etes le client : " ,element)

#----------------------------------------------------------------------------------------------------------------

nbr_abonnees = 2500
nbrgagnes = 0.10
moiss = 24

for mois in range(moiss):
    nbr_abonnees += nbr_abonnees * nbrgagnes

print("le youtuber a ", round(nbr_abonnees), " après 2 ans")









