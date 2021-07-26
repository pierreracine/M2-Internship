# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:47:25 2021

@author: pierr
"""
import sys
import manipulations as m

file1 = sys.argv[1]
file2 = sys.argv[2]

with open (file1,'r') as toread:
    lines = toread.readlines()

headerline= lines[0].split()    #read header line
natoms = int(headerline[0])    #number of atoms

# Looking for lines to duplicate (or not=otherlines)

oxygenlines = []
fluorlines = []
otherlines = []
for i in range(1,natoms+1):
    z = m.itemline(lines[i],1)
    if z=='O':
        oxygenlines.append(i)
    elif z=='F':
        fluorlines.append(i)
    else :
        otherlines.append(i)    
    
# Information to keep for the duplication of oxygen

coordo = []
linkedatomso = []
for i in range(len(oxygenlines)):
    nlineo = oxygenlines[i]
    line = lines[nlineo].strip()
    x = m.itemline(line,2)
    y = m.itemline(line,3)
    z = m.itemline(line,4)
    coord = [x,y,z]
    coordo.append(coord)
    latoms = []
    for k in range(6,8):
        latoms.append(m.itemline(line,k))
    linkedatomso.append(latoms)

# Information to keep for the duplication of fluoride

coordf = []
for i in range(len(fluorlines)):
    nlinef = fluorlines[i]
    line = lines[nlinef]
    x = m.itemline(line,2)
    y = m.itemline(line,3)
    z = m.itemline(line,4)
    coordf.append([x,y,z])
    
# Writting new input file
# First, we modify the atoms already in the input file

with open (file2,'w') as fillin:
    casefluor = 0
    caseoxygen = 0
    for i in range(1,natoms+1):
        for k in range(len(oxygenlines)):
            if oxygenlines[k]==i:
                caseoxygen+=1
                x = coordo[k][0]
                y = coordo[k][1]
                z = coordo[k][2]
                text ='  O   '+x+"  "+y+"  "+z+"  -8  "
                l = linkedatomso[k]
                for j in range(2):
                    text = text+l[j]+'  '
                text = text+str(natoms+len(fluorlines)+caseoxygen)+"\n"
                fillin.write(text)

        for k in range(len(fluorlines)):
            if fluorlines[k]==i:
                casefluor+=1
                x = coordf[k][0]
                y = coordf[k][1]
                z = coordf[k][2]
                fluor = natoms+casefluor
                text = '  F   '+x+"  "+y+"  "+z+"  -4  "+ str(fluor) +"\n"
                fillin.write(text)
        for k in range(len(otherlines)):
            if otherlines[k]==i:
                text = '  '
                line=lines[i].strip().split()
                for j in range(1,5):
                    text = text+line[j]+'  '
                text += '-17  '
                for j in range(6,len(line)):
                    text = text+line[j]+'  '
                fillin.write(text)
                fillin.write("\n")
    
# Then we add the new duplicates for oxygen and fluoride

    for k in range(len(fluorlines)):
        x = coordf[k][0]
        y = coordf[k][1]
        z = coordf[k][2]
        text ='F  '+x+"  "+y+"  "+z+"  -3  "+str(fluorlines[k])+"\n"
        fillin.write(text)
    for k in range(len(oxygenlines)):
        x = coordo[k][0]
        y = coordo[k][1]
        z = coordo[k][2]
        text ='O  '+x+"  "+y+"  "+z+"  -7  "+str(oxygenlines[k])+"\n"
        fillin.write(text)
