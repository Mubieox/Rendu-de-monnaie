def retrait():
    LB={50:15,20:15,10:15,5:15}
    LBR={5:0,10:0,20:0,50:0}
    NB=int(input("Combien voulez vous retirer ? (il faut un nombre divisible par 5) : "))
    assert NB%5==0, "Il fallait mettre un nombre divisible par 5."
    C=int(input("Voulez vous le moins de billets possible : tapez 1 ou équilibrée : tapez 2 ? : "))
    assert C==1 or C==2, "Vous n'avez pas rentré 1 ou 2."
    total=sum(v*nb for v,nb in LB.items())
    if  NB>total:
        print("Plus assez de billets.")
        return False
    if C==1:
        while sum(LBR[v]*v for v in (5,10,20,50))<NB:
            R=NB-sum(LBR[v]*v for v in (5,10,20,50))
            if LB[50]>0 and R>50:
                LBR[50]+=1
                LB[50]-=1
            elif LB[20]>0 and R>20:
                LBR[20]+=1
                LB[20]-=1
            elif LB[10]>0 and R>10:
                LBR[10]+=1
                LB[10]-=1
            else:
                LBR[5]+=1
                LB[5]-=1
    else:
        while NB!=0 and (LB[50]>=1 or LB[20]>=1 or LB[10]>=1 or LB[5]>=1):
            if NB>=50 and LBR[50]<=LBR[5] and LB[50]>=1:
                LBR[50]+=1
                LB[50]-=1
                NB-=50
            elif NB>=20 and LBR[20]<=LBR[5] and LB[20]>=1:
                LBR[20]+=1
                LB[20]-=1
                NB-=20
            elif NB>=10 and LBR[10]<=LBR[5] and LB[10]>=1:
                LBR[10]+=1
                LB[10]-=1
                NB-=10
            else:
                LBR[5]+=1
                LB[5]-=1
                NB-=5    
    print(f"Vous avez retiré : {LBR}, (valeur du billet, nombre).")
    return True
retrait()
