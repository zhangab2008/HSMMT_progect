fi=open("TRNL.fas","r") #input document
fo=open("TRNL_depth.fas","w") #output document

flag=0
for line in fi:
    if line.startswith('>'):
        length=int(line.split('len=')[1].split(' ')[0])
        if length<200 or length>800: #enter length threshold
            flag=0
            pass
        else:
            fo.write(line)
            flag=1
    else:
        if flag==1:
            fo.write(line[20:-20]+"\n")
            flag=0

fi.close()
fo.close()
