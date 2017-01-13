import csv
import numpy as np

GBM = []
k = 0
kset = []
newkset = []

with open('./subtypes/gbm.txt', 'r') as ins:
    reader = csv.reader(ins, delimiter = "\t")
    for row in reader:
        GBM.append(row)

gbm_k = open('gbm_k.txt', 'w')

#remove misc space 
print (len(GBM[0]))
for i in range (0, len(GBM)):
    del(GBM[i][23324])
print (len(GBM[0]))

for x in range (1, len(GBM[0])): #for each gene in GBM
    k = 0
    for i in range(1, len(GBM)):
        if GBM[i][x] != "N":
            k+=1
    kset.append(k)
    if k > 100:
        print (GBM[0][x])

for i in kset:
    if i not in newkset:
        newkset.append(i)

print (newkset)

for i in newkset:
    gbm_k.write(str(i))
    gbm_k.write("\n")
gbm_k.close
