##! /bin/bash                                                                                                                                                                                               

# change to lowercases                                                                                                                                                                                     
#cancers="blca brca crc gbm hnsc kirc laml luad lusc ov ucec"                                                                                                                                               

for ((a=0; a <= 496; a++))
do
        qsub -v SGE_FACILITIES -P unified -l h_vmem=64G,mem_free=10G,h_rt=288000 -b y python coversizetestall.py $a
done