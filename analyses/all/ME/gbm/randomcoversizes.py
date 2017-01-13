import csv
import numpy
import scipy
import os.path
GBM = [] 
kvalues = [] 
k1arr = []
k2arr = []
count = 0
coverarr = []

with open("gbm_k.txt", "r") as f:
    reader = csv.reader(f, delimiter = "\n")
    for x in reader:
        kvalues.append(int(x[0]))


print (kvalues)

for i in kvalues:
    for j in kvalues:
        k1arr = []
        k2arr = []
        
        if (i != 0) and (j != 0):

            if i != j:
            
                 if (os.path.isfile("./coversizes/" + str(i) + "_" + str(j) + ".txt") == False) and (os.path.isfile("./coversizes/" + str(j) + "_" + str(i) + ".txt") == False):
                    #if the computation hasn't been carried out yet 
                     
                    coverfile = open("./coversizes/" + str(i) + "_" + str(j) + ".txt", "w")

                    #open random sample files for each k value 
                    with open(str(i)+'samples.txt', 'r') as f:
                        reader = csv.reader(f, delimiter = " ")
                        for row in reader:
                            k1arr.append(row)

                    with open(str(j)+'samples.txt', 'r') as f:
                        reader = csv.reader(f, delimiter = " ")
                        for row in reader:
                            k2arr.append(row)

                    #convert arrays to integer arrays 
#                    for a in range (0, len(k1arr)):
#                        for b in range (0, len(k1arr[0])):
#                            k1arr[a][b] = int(k1arr[a][b])

#                    for c in range (0, len(k2arr)):
#                        for d in range (0, len(k2arr[0])):
#                            k2arr[c][d] = int(k2arr[c][d])
                    
                    count = 0
                    for e in range (0, 100):
                        for g in range (0, 100):
                            count+=1
                            coverarr = []
                            for z in k1arr[e]:
                                coverarr.append(z)
                            for y in k2arr[g]:
                                if y not in coverarr:
                                    coverarr.append(y)

                            coverfile.write(str(len(coverarr)))
                            if (count!=10000):
                                coverfile.write(" ")
                            

            if i == j:

                 if (os.path.isfile("./coversizes/" + str(i) + "_" + str(j) + ".txt") == False):
                    #if the computation hasn't been carried out yet                                                                                                                                         

                    coverfile = open("./coversizes/" + str(i) + "_" + str(j) + ".txt", "w")

                    #open random sample files for each k value                                                                                                                                              
                    with open(str(i)+'samples.txt', 'r') as f:
                        reader = csv.reader(f, delimiter = " ")
                        for row in reader:
                            k1arr.append(row)

                    with open(str(j)+'samples.txt', 'r') as f:
                        reader = csv.reader(f, delimiter = " ")
                        for row in reader:
                            k2arr.append(row)

                    #convert arrays to integer arrays                                                                                                                                                      
#                    for a in range (0, len(k1arr)):
#                        for b in range (0, len(k1arr[0])):
#                            k1arr[a][b] = int(k1arr[a][b])

#                    for c in range (0, len(k2arr)):
#                        for d in range (0, len(k2arr[0])):
#                            k2arr[c][d] = int(k2arr[c][d])

                    count=0
                    for e in range (0, 100):
                        for g in range (0, 101):
                            if e != g:
                                count+=1 
                                coverarr = []
                                for z in k1arr[e]:
                                    coverarr.append(z)
                                for y in k2arr[g]:
                                    if y not in coverarr:
                                        coverarr.append(y)
                                coverfile.write(str(len(coverarr)))
                                if (count!=10000):
                                    coverfile.write(" ")

        if ((i == 0) and (j != 0)):

                 if (os.path.isfile("./coversizes/" + str(i) + "_" + str(j) + ".txt") == False) and (os.path.isfile("./coversizes/" + str(j) + "_" + str(i) + ".txt") == False):
                    #if the computation hasn't been carried out yet                                                                                                                                         
                    coverfile = open("./coversizes/" + str(i) + "_" + str(j) + ".txt", "w")

                    #open random sample files for each k value                                                                                                                                             
                    
                    count=0
                    for e in range (0, 100):
                        for g in range (0, 100):
                            count+=1
                            coverfile.write(str(j))
                            if (count!=10000):
                                coverfile.write(" ")

        if ((i != 0) and (j == 0)):

                 if (os.path.isfile("./coversizes/" + str(i) + "_" + str(j) + ".txt") == False) and (os.path.isfile("./coversizes/" + str(j) + "_" + str(i) + ".txt") == False):
                    #if the computation hasn't been carried out yet                                                                                                                                        
                                                                                                                                                                                                            
                    coverfile = open("./coversizes/" + str(i) + "_" + str(j) + ".txt", "w")

                    #open random sample files for each k value                                                                                                                                             

                    count=0
                    for e in range (0, 100):
                        for g in range (0, 100):
                            count+=1
                            coverfile.write(str(i))
                            if (count!=10000):
                                coverfile.write(" ")
