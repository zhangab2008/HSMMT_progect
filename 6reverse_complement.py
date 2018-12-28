import os
import sys
from Bio import SeqIO
from Bio.Seq import Seq

fb=open("larvae.blast","r") #input document
foo=open("larvae_ok.fas","w") #output document
fon=open("larvae_ng.fas","w") #output document

seqListO=[]
seqListN=[]
for line in fb:
    tmp=line.split('\t')
    if int(tmp[9])-int(tmp[8])>0:
        seqListO.append(tmp[0])
    else:
        seqListN.append(tmp[0])

for seq in SeqIO.parse("querySeq.fasta",'fasta'):
    seqName=seq.id
    if seqName.split('-')[0] in seqListO:
        foo.write(">"+seqName+"\n"+str(seq.seq)+"\n")
    elif seqName.split('-')[0] in seqListN:
        fon.write(">"+seqName+"\n"+str(seq.seq.reverse_complement())+"\n")

fb.close()
foo.close()
fon.close()
