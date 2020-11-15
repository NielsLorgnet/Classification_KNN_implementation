# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:18:09 2020

@author: Niels
"""
import numpy as np
# Check the readme file for information about the code. The accuracy using random forest on Rstudio as a comparison is 0.87.
# Lire le readme pour ce qui est des heuristiques possibles et de la version ci-dessous
# x en paramètre est le nombre de voisins proches à regarder autour de chaque point à classer
def k_nn(x):
    
    # On ouvre tout d'abord le fichier contenant le dataset, que l'on stocke sous forme
    # de liste de listes, avec une liste par individu
    places = []    
    with open('data.csv', 'r') as filehandle:
        places = [current_place.rstrip() for current_place in filehandle.readlines()]
    dataset=[]
    for i in range(len(places)):
        dataset.append(places[i].split(";"))
    
    
    # On ouvre ensuite le fichier contenant les données test, que l'on stocke sous forme
    # de liste de listes, avec une liste par individu
    places = []    
    with open('data_eval.csv', 'r') as filehandle:
        places = [current_place.rstrip() for current_place in filehandle.readlines()]
    unknown=[]
    for i in range(len(places)):
        unknown.append(places[i].split(";"))
    classe=[]
    for i in range (10):  # nombre de classes: ici 10
        classe.append(0)
      
    for i in range(len(unknown)):
        for c in range (10): 
            classe[c]=0
        distance=[] # Liste qui contiendra la distance et la classe de chaque point 
        # par rapport au point étudié 
        for j in range (len(dataset)):
            distance.append((dataset[j][4],np.sqrt((float(unknown[i][0])-float(dataset[j][0]))**2 +(float(unknown[i][1])-float(dataset[j][1]))**2+(float(unknown[i][2])-float(dataset[j][2]))**2+(float(unknown[i][3])-float(dataset[j][3]))**2)))
        # On trie la liste afin de regarder les points les plus proches derrière
        distance.sort(key=lambda distance:distance[1])
        for l in range(x):
            if distance[l][0]=="A":
                classe[0]+=1    #*(1/distance[l][1]) Si on veut ponderer par la distance
            if distance[l][0]=="B":
                classe[1]+=1
            if distance [l][0]=="C":
                classe[2]+=1
            if distance [l][0]=="D":
                classe[3]+=1
            if distance [l][0]=="E":
                classe[4]+=1
            if distance [l][0]=="F":
                classe[5]+=1
            if distance [l][0]=="G":
                classe[6]+=1
            if distance [l][0]=="H":
                classe[7]+=1
            if distance [l][0]=="I":
                classe[8]+=1
            if distance [l][0]=="J":
                classe[9]+=1
        
        temp=max(classe)
        temp2=0
        for c in classe :
            if c==temp:
                temp2+=1
        # Si deux classes reviennent autant autour de l'individu à classer,
        # on choisit la classe du point le plus proche de l'individu à classer
        if(temp2>1):
            value=""
            if distance[0][0]=="A":
                value="A"
            elif distance[0][0]=="B":
                value="B"
            elif distance[0][0]=="C":
                value="C"
            elif distance[0][0]=="D":
                value="D"
            elif distance[0][0]=="E":
                value="E"
            elif distance[0][0]=="F":
                value="F"
            elif distance[0][0]=="G":
                value="G"
            elif distance[0][0]=="H":
                value="H"
            elif distance[0][0]=="I":
                value="I"
            elif distance[0][0]=="J":
                value="J"            
            unknown[i].append(value)
        # Sinon, on choisit la classe la plus représentée parmi les points les plus proches
        else:
            a=(classe.index(max(classe)))+1
            value=""
            if a==1:
                value="A"
            elif a==2:
                value="B"
            elif a==3:
                value="C"
            elif a==4:
                value="D"
            elif a==5:
                value="E"
            elif a==6:
                value="F"
            elif a==7:
                value="G"
            elif a==8:
                value="H"
            elif a==9:
                value="I"
            elif a==10:
                value="J"
            unknown[i].append(value)
           
        
    """ Si certains points n'ont pas de classe attribuée, on attribue A:
    for u in unknown:
        if u[4]=="":
            u[4]="A"
    """
    
    fichier= open('result_final.txt', 'w') 
    for u in unknown:
        fichier.write(u[len(u)-1]+"\n")
    fichier.close()        
    # Le fichier result_final contiendra les classes de chaque individu dont on souhaite
    # déterminer la classe  
    
    """  Au cas où l'on souhaiterait connaître la précision de l'algorithme, on execute
         le code ci-dessous. Chaque liste contenue dans unknown aura comme 4ème valeur 
         la classe de l'individu et comme 5ème valeur la classe prédite par le modèle.
    """
    
           
    compteur=0
    for i in range(len(unknown)):
        if unknown[i][5]==unknown[i][4]:
            compteur+=1
    compteur=compteur*100/len(unknown)
    print (compteur)
    
    
k_nn(11)
# En utilisant ce dataset et cette implémentation, la meilleure valeur pour x est 11
