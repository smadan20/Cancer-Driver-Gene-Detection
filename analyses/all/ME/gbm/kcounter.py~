import csv
import numpy as np

KIRC = []
k = 0
kset = []
newkset = []

with open('./subtypes/kirc.txt', 'r') as ins:
    reader = csv.reader(ins, delimiter = "\t")
    for row in reader:
        KIRC.append(row)

kirc_k = open('kirc_k.txt', 'w')

#remove misc space 
print (len(KIRC[0]))
for i in range (0, len(KIRC)):
    del(KIRC[i][23324])
print (len(KIRC[0]))

for x in range (1, len(KIRC[0])): #for each gene in KIRC
    k = 0
    for i in range(1, len(KIRC)):
        if KIRC[i][x] != "N":
            k+=1
    kset.append(k)
    if k > 100:
        print (KIRC[0][x])

for i in kset:
    if i not in newkset:
        newkset.append(i)

print (newkset)

for i in newkset:
    kirc_k.write(str(i))
    kirc_k.write("\n")
kirc_k.close
