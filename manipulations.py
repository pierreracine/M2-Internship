# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def numberlines(file):
    with open (file,"r") as toread:
        k = 0
        for ligne in toread :
            k+=1
    return(k)

def linefromfile(file,n):
    with open (file,"r"):
        lines = file.readlines
        line = str(lines[n])
        return(line)
    
def numberitemsline(line):
    items = line.split()
    n = len(items)
    return(n)

def itemline(line,i):
    items = line.split()
    item = items[i]
    return(item)

def itemsline(line,i,j):
    items = line.split()
    listitem = []
    n = len(items)
    for k in range(n):
        if (i<=k<=j):
            item = items[k]
            listitem.append(item)
    return(listitem)