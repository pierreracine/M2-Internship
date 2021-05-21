# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:19:44 2021

@author: Pierre
"""


#Script pour écrire les paramétres de torsions sous la forme déjà supportée par deMon2k

with open("tritorsion.txt","r") as toread, open ("torsion.txt","w") as tofill :
    lignes=toread.readlines()
    for ligne in lignes :
        liste=ligne.split()
        
        if liste[4]=='1':
            tofill.write("torsion "+liste[0]+"  "+liste[1]+"  "+liste[2]+"  "+liste[3]+"  "+
                         "0.0 0.0 1 0.0 0.0 2 "+liste[5]+" 0.0 3 \n")
            continue
        if liste[4]=='4':
            tofill.write("torsion "+liste[0]+"  "+liste[1]+"  "+liste[2]+"  "+liste[3]+"  "+
                         "0.0 0.0 1 "+liste[5]+" 180 2 0.0 0.0 3 \n")
            continue
        if liste[4]=='5':
            tofill.write("torsion "+liste[0]+"  "+liste[1]+"  "+liste[2]+"  "+liste[3]+"  "+
                         liste[6]+" 180 1 "+liste[5]+" 180 2 0.0 0.0 3 \n")
            continue