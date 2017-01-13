import csv
import os.path
import argparse

GBM = []
GBM_sig = [] 
sig_genes = []
colholder = []
samplesholder = [] 
k1 = 0
k2 = 0
coversize = 0
coverarr = []
pvalue = 0
count = 0 
dict = {}



##ARGUMENT PARSER: ENABLE PARALLEL COMPUTATION ON CLUSTER                                                                                                                                                  
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='i', type=int, nargs='+', help='an integer for the accumulator')
args = parser.parse_args()
###args.integers[0] is the variable which will be used to refer to the slice of genes being tested at a time###   




#OPEN DATA FILES
with open("gbm.txt", "r") as ins:
    reader = csv.reader(ins, delimiter = "\t")
    for row in reader:
        GBM.append(row)

with open("all_genes.txt", "r") as f:
    all_genes = [str(x) for x in  f.readline().strip().split(" ")]
 
with open("../splitgenes/geneset" + str(args.integers[0]) + ".txt", "r") as g:
    sig_genes = [str(y) for y in  g.readline().strip().split(" ")]


results = open("/panfs/pan1/pancan_me/gbm/gbm_results" + str(args.integers[0]) + ".txt", "w")

print(sig_genes)





#LOAD K1, K2 COVERSIZES
with open("gbm_k.txt", "r") as g:
    kvalues = [int(x) for x in g.readlines()]
del kvalues[kvalues.index(0)]

for x in kvalues:
    for a in kvalues:

        if (x != a):

            if (os.path.isfile("./coversizes/" + str(x) + "_" + str(a) + ".txt") == True):
                pairfile = "./coversizes/" + str(x) + "_" + str(a) + ".txt"
            elif (os.path.isfile("./coversizes/" + str(a) + "_" + str(x) + ".txt") == True):
                pairfile = "./coversizes/" + str(a) + "_" + str(x) + ".txt"
            with open (pairfile, "r") as file:
                holder =[int(x) for x in  file.readline().strip().split(" ")]
                dict[str(x) + "_" + str(a)] = holder
                holder = []

        elif (x == a):

            pairfile = "./coversizes/" + str(x) + "_" + str(a) + ".txt"
            with open (pairfile, "r") as file:
                holder =[int(x) for x in  file.readline().strip().split(" ")]
                dict[str(x) + "_" + str(a)] = holder
                holder = []
                         

#DELETE MISC SPACE                                                                                                                                                                                         
for i in range (0, len(GBM)):
    del(GBM[i][len(GBM[0])-1])



#CUT DOWN ARRAY TO ONLY GENES OF INTEREST                                                                                                                                                                  
for i in range (0, len(GBM)):
    samplesholder.append(GBM[i][0])
GBM_sig.append(samplesholder)
samplesholder = [] 

for i in range (1, len(GBM[0])):
    if GBM[0][i] in sig_genes:
          for j in range (0, len(GBM)):
              colholder.append(GBM[j][i])
          GBM_sig.append(colholder)
          colholder = []




#RESHAPE GBM ARRAY TO MATCH SIG_GENES ARRAY (ROWS X COLS = SAMPLES X GENES) 
GBMnew = [] 
for i in range (0, len(GBM)):
    samplesholder.append(GBM[i][0])
GBMnew.append(samplesholder)
samplesholder = []

for i in range (1, len(GBM[0])):
    if GBM[0][i] in all_genes:
          for j in range (0, len(GBM)):
              colholder.append(GBM[j][i])
          GBMnew.append(colholder)
          colholder = []




##COMPUTATION                                                                                                                                                                                             
for i in range(1, len(GBM_sig)):

        for j in range(1, len(GBMnew)): #every possible gene pair                                                                                                                                   

                count += 1
                k1, k2= 0, 0
                coversize = 0 
                pvalue = 0
                coverarr = [] 

                for z in range(1, len(GBM_sig[0])):                                                                                                                                                                      
                    if GBM_sig[i][z] == "C" or GBM_sig[i][z] == "B" or GBM_sig[i][z] == "M":                                                                                                              
                        k1+=1  # number of mutated samples for gene i                                                                                                                                                                                     
                    if GBMnew[j][z] == "C" or GBMnew[j][z] == "B" or GBMnew[j][z] == "M":                                                                                                              
                        k2+=1  # number of mutated samples for gene j
      
                    if (GBM_sig[i][z] == "C" or GBM_sig[i][z] == "B" or GBM_sig[i][z] == "M") or (GBMnew[j][z] == "C" or GBMnew[j][z] == "B" or GBMnew[j][z] == "M"):
                        coversize += 1 # number of mutated samples for gene i or j
                
                if (k1 ==0) or (k2 ==0):
                    
                    results.write(str(GBM_sig[i][0]) + "\t")
                    results.write(str(GBMnew[j][0]) + "\t")
                    results.write("1.0" + "\t" + "1.0" + "\t") 
                    results.write(str(float(coversize)/float(279)) + "\t") 
                    results.write(str(k1) + "\t" + str(k2)) 
                    results.write("\n")

                elif (k1 != 0) and (k2 != 0):

                    try:
                        coverarr = dict[str(k1) + "_" + str(k2)]
                    except KeyError:
                        coverarr = dict[str(k2) + "_" + str(k1)]


                    #MUTUALLY EXCLUSIVE PVALUE. 
                    for item in coverarr:
                        if int(item) >= coversize:
                            pvalue += 1
                    pvalue = float(pvalue)/10000
 
                    results.write(str(GBM_sig[i][0]) + "\t")
                    results.write(str(GBMnew[j][0]) + "\t")
                    results.write(str(pvalue) + "\t")

                    #CO-OCCURRING PVALUE. 
                    pvalue = 0 
                    for item in coverarr:
                        if int(item) <= coversize:
                            pvalue +=1
                    pvalue = float(pvalue/10000) 
                    
                    results.write(str(pvalue) + "\t") 
                    results.write(str(float(coversize)/float(279)) + "\t")
                    results.write(str(k1) + "\t" + str(k2))
                    results.write("\n") 
               
                    
print(count) 
results.close() 
