fi=open("Trinity_dep_filtered_addGene.fas","r") #input document
fR=open("RBCL.fas","w")#output document
fC=open("COI.fas","w") #output document
fT=open("TRNL.fas","w") #output document
fM=open("MATK.fas","w") #output document
fI=open("ITS.fas","w") #output document

flag="A"
for line in fi:
    if line.startswith('>'):
        if "|" in line:
            gene=line.split("|")[1].split(" ")[0]
            print(gene)
            if gene=="COI":
                fC.write(line)
                flag="C"
            elif gene=="RBCL":
                fR.write(line)
                flag="R"
            elif gene=="TRNL":
                fT.write(line)
                flag="T"
            elif gene=="MATK":
                fM.write(line)
                flag="M"
            elif gene=="ITS":
                fI.write(line)
                flag="I"
            else:
                print("error:"+line)
        else:
            flag="A"
    else:
        if flag=="C":
            fC.write(line)
            flag="A"
        elif flag=="R":
            fR.write(line)
            flag="A"
        elif flag=="T":
            fT.write(line)
            flag="A"
        elif flag=="M":
            fM.write(line)
            flag="A"
        elif flag=="I":
            fI.write(line)
            flag="A"
        elif flag=="A":
            pass
        else:
            print("error:"+flag)

fi.close()
fC.close()
fR.close()
fT.close()
fM.close()
fI.close()

