import csv
import numpy as np
samples = [] 
patients = []
samplenames = [] 
frequencies = {} 
GBM = []
count = 0 


with open("gbm_k.txt", "r") as f:
     k = [int(x) for x in f.readlines()]
print(k)



with open("gbm.txt", "r") as f:
     samplenames = [row[0:15] for row in f.readlines()]
del samplenames[0]

with open("gbm.txt", "r") as f:
     reader = csv.reader(f, delimiter="\t")
     for row in reader:
          count = 0
          for i in row:  
               if i == "C" or i == "M" or i =="B":
                    count +=1 
               frequencies[str(row[0])] = count


elements = []
weights = []
sum = 0  
for x in frequencies:
     weights.append(frequencies[x])
for i in weights:
     sum +=i
weights = np.asarray(weights)
weights = weights/sum     
for i in frequencies.keys():
     elements.append(i)

##GENERATE RANDOM SAMPLES 
files = []
for i in k:
    file = open(str(i)+ 'samples.txt', 'w')
    files.append(file) 


for i in range (0, len(k)):
    for b in range (0, 101):
        sample = np.random.choice(elements, k[i], p=weights, replace = False)
        for z in range(0, len(sample)):
                files[i].write(str(sample[z]))
                if z != len(sample)-1:
                    files[i].write(" ")
        files[i].write("\n")
        sample = []


##look at/open a particular file 
with open(str(k[k.index(50)]) + "samples.txt", "r") as f:
     reader = csv.reader(f, delimiter = " ")
     for row in reader:
          for i in row:
               samples.append((i))



##calculate number of unique samples in the random draws 
for i in samples: 
     if i not in patients:
          patients.append(i)


##calculate how many times each patient was picked 
#for x in patients:
#     count = 0 
#     for i in samples:
#          if i == x:
#               count +=1
#     print("Patient", x, "picked", count, "times.")
