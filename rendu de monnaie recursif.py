montant=int(input("Saisir le montant souhaité : "))

billets=[50,20,10,5]
coupure={}

def rendu(montant,billets,coupure):
    if montant==0:
        return coupure
    else:
        coupure[billets[0]]=montant//billets[0]
        coupure=rendu(montant%billets[0],billets[1:],coupure)
    return coupure

print(rendu(montant,billets,coupure))

billets=[50,20,10,5]
coupure=[0,0,0,0]

def rendu_bis(montant,billets,coupure,i=0):
    if montant==0:
        return coupure
    else:
        coupure[i]=montant//billets[i]
        coupure=rendu_bis(montant%billets[i],billets,coupure,i+1)
    return coupure

coupure=rendu_bis(montant,billets,coupure)

print("Voici la répartition des billets :")
for i in range(len(billets)):
    print("Billet(s) de ",billets[i],": ",coupure[i])