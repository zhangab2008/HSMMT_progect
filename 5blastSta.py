fi=open("ITSJ67S8SP7014-Alignment.xml","r") #input document
fs=open("ITS_depth.fas","r") #input document
fo=open("ITS_depth_blast.fas","w") #output document
fe=open("ITS_nomatch.fas","w") #output document

results=fi.read().split("<Iteration>")[1:]

content=[]
nomatch=[]
seqs=fs.read()
for result in results:
    query=result.split("<Iteration_query-def>")[1].split('<')[0]
    queryLen=int(result.split("<Iteration_query-len>")[1].split('<')[0])
    hits=result.split("<Hit>")[1:]
    flag=0
    for hit in hits:
        accession=hit.split("<Hit_accession>")[1].split('<')[0]
        taxa=hit.split("<Hit_def>")[1].split('<')[0]
        identity=int(hit.split("<Hsp_identity>")[1].split("<")[0])
        hitFrom=int(hit.split("<Hsp_query-from>")[1].split("<")[0])
        hitTo=int(hit.split("<Hsp_query-to>")[1].split("<")[0])
        coverage=float((hitTo-hitFrom)/queryLen)
        identitication=float(identity/(hitTo-hitFrom))
        if coverage>0.795 and identitication>0.975:
            flag=1
            break
            
    if flag==1:
        content.append(query)
    else:
        nomatch.append(query)

for seq in content:
    if seq in seqs:
        fo.write(">"+seq+"\n"+seqs.split(seq)[1].split("\n")[1]+"\n")
for seq in nomatch:
    if seq in seqs:
        fe.write(">"+seq+"\n"+seqs.split(seq)[1].split("\n")[1]+"\n")

fi.close()
fo.close()
fe.close()
fs.close()

