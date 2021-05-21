# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:41:07 2021

@author: Pierre
"""

# Script pour créer les fichier FFDS avec tout les paramètres des bonds, angles et torsions.


typesN=[45,46,47,48,49,50,51,52,53,54]

with open ("FFDSbond.txt","w") as fillin :
    for k in range (len(typesN)):
        fillin.write("0  "+str(typesN[k])+" 4.6 1.460 \n")
    
    for k in range (len(typesN)):
        fillin.write("58 "+str(typesN[k])+" 6.4 1.016 \n")

force=[111.0,110.7,109.5,109.5,109.0,109.2]

with open ("FFDSangle.txt","w") as fillin :
    for i in range (0,3):
        for k in range (len(typesN)):
            fillin.write("0  "+str(34+i)+" "+str(typesN[k])+" 0.57 "+str(force[i])+" \n")
        for k in range (len(typesN)):
            fillin.write("58  "+str(33+i)+" "+str(typesN[k])+" 0.40 "+str(force[3+i])+" \n")
    for i in range (len(typesN)):
        fillin.write("0  "+str(typesN[i])+" 0  1.1 109.0 \n")
    for i in range (len(typesN)):
        fillin.write("58 "+str(typesN[i])+" 58 0.8 110.0 \n")
    for i in range (len(typesN)):
        fillin.write("58 "+str(typesN[i])+" 0  0.8 111.0 \n")



with open ("FFDStorsion.txt","w") as fillin :
    for k in range (len(typesN)):
        for i in range(k,len(typesN)):
            fillin.write(str(typesN[k])+" 38 38 "+str(typesN[i])+" 4 2.0 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 0  0  58 1 0.12 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 0  0  0  1 0.08 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 38 38 0  4 2.0 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 38 38 58 4 2.0 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 0  0  56 1 0.11 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 34 43 56 1 -0.03 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 35 43 56 1 -0.03 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 34 43 57 1 -0.03 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 35 43 57 1 -0.03 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 42 51 0  4 7.5 \n")
    for k in range(len(typesN)):
        fillin.write(str(typesN[k])+" 38 49 38 4 2.0 \n")
    for k in range(len(typesN)):
        fillin.write("58 0  "+str(typesN[k])+" 58 1 0.12 \n")
    for k in range(len(typesN)):
        fillin.write("58 0  "+str(typesN[k])+" 0  1 0.4 \n")
    for k in range(len(typesN)):
        fillin.write("0  0  "+str(typesN[k])+" 0  1 0.08 \n")