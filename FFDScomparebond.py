# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:12:23 2021

@author: Pierre
"""
"""
# Réécrit le FFDS nouvellement généré en remplaçant les nouvelles valeurs par celles déjà tabulées.

with open ("FFDSbond.txt","r") as toread1, open ("parambond.txt","r") as toread2 :
    lignes1=toread1.readlines()
    lignes2=toread2.readlines()
    for ligne1 in lignes1:
        k=0
        liste1=ligne1.split()
        for ligne2 in lignes2:
            liste2=ligne2.split()
            if (liste1[0]==liste2[0] and liste1[1]==liste2[1])or(liste1[1]==liste2[0] and liste1[0]==liste2[1]):
                k+=1
                print('test',ligne1,ligne2)
                continue
                    
        if k==0:
            with open("FFDSbond2.txt","a") as tofill:
                tofill.write(ligne1)   

with open ("FFDSangle.txt","r") as toread1, open ("paramangle.txt","r") as toread2 :
    lignes1=toread1.readlines()
    lignes2=toread2.readlines()
    for ligne1 in lignes1:
        k=0
        liste1=ligne1.split()
        for ligne2 in lignes2:
            liste2=ligne2.split()
            if ((liste1[0]==liste2[0] and liste1[1]==liste2[1] and liste1[2]==liste2[2]) 
            or (liste1[2]==liste2[0] and liste1[0]==liste2[2] and liste1[1]==liste2[1])):
                k+=1
                print('test',ligne1,ligne2)
                continue
                    
        if k==0:
            with open("FFDSangle2.txt","a") as tofill:
                tofill.write(ligne1)   


with open ("FFDStorsion.txt","r") as toread1, open ("paramtorsion.txt","r") as toread2 :
    lignes1=toread1.readlines()
    lignes2=toread2.readlines()
    for ligne1 in lignes1:
        k=0
        liste1=ligne1.split()
        for ligne2 in lignes2:
            liste2=ligne2.split()
            if ((liste1[0]==liste2[0] and liste1[1]==liste2[1] and liste1[2]==liste2[2] and liste1[3]==liste2[3]) 
            or (liste1[0]==liste2[3] and liste1[1]==liste2[2] and liste1[2]==liste2[1] and liste1[3]==liste2[0])):
                k+=1
                print('test',ligne1,ligne2)
                continue
                    
        if k==0:
            with open("FFDStorsion2.txt","a") as tofill:
                tofill.write(ligne1)
"""
             
#Fonction pour trier un fichier de paramètres de torsion, dans l'ordre des nombres de zéro décroissant par ligne.


with open ("toutestorsions.txt","r") as toread:

     lignes=toread.readlines()
     for ligne in lignes:
         liste=ligne.split()
         if (liste[0]=='0' and liste[1]=='0' and liste[2]=='0' and liste[3]=='0'):
             with open("tritorsion.txt","a") as tofill:
                 tofill.write(ligne)

     for ligne in lignes:
         liste=ligne.split()
         if ((liste[0]=='0' and liste[1]=='0' and liste[2]=='0' and liste[3]!='0')or
             (liste[0]=='0' and liste[1]=='0' and liste[2]!='0' and liste[3]=='0')or
             (liste[0]=='0' and liste[1]!='0' and liste[2]=='0' and liste[3]=='0')or
             (liste[0]!='0' and liste[1]=='0' and liste[2]=='0' and liste[3]=='0')):
              with open("tritorsion.txt","a") as tofill:
                 tofill.write(ligne)
        

     for ligne in lignes:
         liste=ligne.split()
         if ((liste[0]=='0' and liste[1]=='0' and liste[2]!='0' and liste[3]!='0')or
             (liste[0]=='0' and liste[1]!='0' and liste[2]=='0' and liste[3]!='0')or
             (liste[0]=='0' and liste[1]!='0' and liste[2]!='0' and liste[3]=='0')or
             (liste[0]!='0' and liste[1]=='0' and liste[2]=='0' and liste[3]!='0')or
             (liste[0]!='0' and liste[1]=='0' and liste[2]!='0' and liste[3]=='0')or
             (liste[0]!='0' and liste[1]!='0' and liste[2]=='0' and liste[3]=='0')):
             with open("tritorsion.txt","a") as tofill:
                 tofill.write(ligne)
          

     for ligne in lignes:
         liste=ligne.split()
         if ((liste[0]=='0' and liste[1]!='0' and liste[2]!='0' and liste[3]!='0')or
             (liste[0]!='0' and liste[1]=='0' and liste[2]!='0' and liste[3]!='0')or
             (liste[0]!='0' and liste[1]!='0' and liste[2]=='0' and liste[3]!='0')or
             (liste[0]!='0' and liste[1]!='0' and liste[2]!='0' and liste[3]=='0')):
             with open("tritorsion.txt","a") as tofill:
                 tofill.write(ligne)  

     for ligne in lignes:
         liste=ligne.split()
         if (liste[0]!='0' and liste[1]!='0' and liste[2]!='0' and liste[3]!='0'):
             with open("tritorsion.txt","a") as tofill:
                 tofill.write(ligne)
                 