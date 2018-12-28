markerList="COI|ITS|matk|rbcL|trnL"
fi=open("seqFile.txt","r") #input document(the ID list of the samples)
fo=open("merge.csv","w") #output document
fo.write("sample,COI,ITS,MATK,RBCL,TRNL\n")
for line in fi:
    sample=line.strip()
    content=sample+","
    for marker in markerList.split('|'):
        result=[]
        fs=open(marker+".blast","r") #input document
        for res in fs:
            if res.startswith(sample+"_"):
                result.append(res)
        if len(result)==0:
            content=content+"NA,"
            continue
        tmpV=0.0
        tmpP=0
        for i in range(0,len(result)):
            v=float(result[i].split('\t')[2])
            if v>tmpV:
                tmpV=v
                tmpP=i
        if tmpV<98:
            content=content+"NA,"
            continue
        else:
            #print(result[tmpP].split("\t")[3])
            coverage=(int(result[tmpP].split("\t")[7])-int(result[tmpP].split("\t")[6]))/int(result[tmpP].split("\t")[3])
            content=content+result[tmpP].split("\t")[1]+"|"+result[tmpP].split("\t")[2]+"%|"+str(coverage*100).split('.')[0]+"."+str(coverage*100).split('.')[1][:3]+"%,"
        fs.close()
    fo.write(content[:-1])
    fo.write("\n")
fi.close()
fo.close()
