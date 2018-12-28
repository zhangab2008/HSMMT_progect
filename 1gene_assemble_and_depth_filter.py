import os
import sys

######################################
def seqInOne():
    inFile="Trinity.fasta"
    outFile="Trinity.fas"
    fi=open(inFile,"r") # Opens file for reading
    fo=open(outFile,"w")

    flag=0
    content=""
    for line in fi:
        if line.startswith('>'):
            content=content+"\n"+line
            flag=1
        else:
            if flag==1:
                content=content+line.strip()

    fo.write(content[1:]+"\n")

    fi.close()
    fo.close()

#######################################
def depth():
    fs=open("Trinity.fas","r")
    fi=open("reads.depth","r")
    fo=open("Trinity_dep_filtered.fas","w")

    gene=""
    geneCount=0
    depSum=0
    seqContent=fs.read()
    for line in fi:
        if len(gene)==0:
            gene=line.split('	')[0]
            geneCount=1
            depSum=int(line.split('	')[2].strip())
        else:
            if line.split('	')[0]==gene:
                geneCount=geneCount+1
                depSum=depSum+int(line.split('	')[2].strip())
            else:
                depth=int(depSum/geneCount)
                tmp=seqContent.split(gene)[1].split('\n')
                seqLen=tmp[0].split(' ')[1]
                seq=tmp[1]
                if depth>=1000:
                    fo.write(">"+gene+" "+seqLen+" dep="+str(depth)+"\n"+seq+"\n")
                gene=line.split('	')[0]
                geneCount=1
                depSum=int(line.split('	')[2].strip())

    fs.close()
    fi.close()
    fo.close()

#######################################################
if __name__ == '__main__':
    fi=open("seqFile.txt","r") #seqFile.txt is the list of the name of samples
    fout=open("Trinity_dep_filtered.fas","w")

    for line in fi:
        if len(line.strip())==0:
            continue
        fileName=line.strip()
        command="$TRINITY_PATH/Trinity --seqType fq --left "+fileName+"_R1.fq --right "+fileName+"_R2.fq --CPU 20 --JM 56G --output "+fileName+"_trinity_out_dir"
        print(command)
        ret=os.system(command)
        if ret==0:
            pass
        else:
            print("Error:ret="+str(ret)+",command="+command)
            sys.exit(1)

        os.chdir("./"+fileName+"_trinity_out_dir")

        command="$TRINITY_PATH/util/align_and_estimate_abundance.pl --transcripts Trinity.fasta --seqType fq --left ../"+fileName+"_R1.fq --right ../"+fileName+"_R2.fq --est_method RSEM --aln_method bowtie --trinity_mode --prep_reference"
        print(command)
        ret=os.system(command)
        if ret==0:
            pass
        else:
            print("Error:ret="+str(ret)+",command="+command)
            sys.exit(1)

        command="samtools sort bowtie.bam -o sorted.bam"
        print(command)
        ret=os.system(command)
        if ret==0:
            pass
        else:
            print("Error:ret="+str(ret)+",command="+command)
            sys.exit(1)

        command="samtools depth sorted.bam > reads.depth"
        print(command)
        ret=os.system(command)
        if ret==0:
            pass
        else:
            print("Error:ret="+str(ret)+",command="+command)
            sys.exit(1)

        seqInOne()
        depth()

        command="mv -f Trinity_dep_filtered.fas ../"+fileName+"_Trinity_dep_filtered.fas"
        ret=os.system(command)
        if ret==0:
            pass
        else:
            print("Error:ret="+str(ret)+",command="+command)
            sys.exit(1)
        command="mv -f reads.depth ../"+fileName+"_reads.depth"
        ret=os.system(command)
        if ret==0:
            pass
        else:
            print("Error:ret="+str(ret)+",command="+command)
            sys.exit(1)

        os.chdir("/mnt/a9c63a67-c4eb-436b-a2c5-f44c96c8ff62/RNAseq/ZXM/network/")#current working path

        fdep=open(fileName+"_Trinity_dep_filtered.fas","r")
        for line in fdep:
            if line.startswith('>'):
                fout.write(line.replace(">",">"+fileName+"_"))
            else:
                fout.write(line)
        fdep.close()

    fi.close()
    fout.close()





