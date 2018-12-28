fi=open("Trinity_dep_filtered.fas","r") #input document
fg=open("seq.blast","r") #input document
fo=open("Trinity_dep_filtered_addGene.fas","w") #output document

seqs=fi.read()
for line in fg:
    seqs=seqs.replace(line.split("	")[0]+" ",line.split("	")[0]+"|"+line.split("	")[1].split('_')[0]+" ")

fo.write(seqs)
fi.close()
fo.close()
fg.close()

fi=open("Trinity_dep_filtered_addGene.fas","r")
fo=open("noGene.fas","w") #output document
flag=0
for line in fi:
    if line.startswith('>'):
        if "|" not in line:
            flag=1
            fo.write(line)
        else:
            flag=0
    else:
        if flag==1:
            fo.write(line)
            flag=0
fi.close()
fo.close()

