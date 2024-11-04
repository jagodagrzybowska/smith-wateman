import numpy
from Bio import SeqIO

sequences = []
with open('para_sekwencji.fa', 'r') as fastaFile:
    for s in SeqIO.parse(fastaFile, "fasta"):
            sequences.append(str(s.seq))

if len(sequences)!=2:
    print(len(sequences))
    raise ValueError("Liczba sekwencji w pliku powinna wynosic 2")

else:
    match=int(input('Wprowadz wartosc dla match (l. calkowita): '))
    mismatch=int(input('Wprowadz wartosc dla mismatch (l. calkowita): '))
    gap=int(input('Wprowadz wartosc dla gap (l. calkowita): '))

s1=sequences[0]
s2=sequences[1]

m=len(s1)
n=len(s2)
M=numpy.zeros([m+1, n+1], dtype=int)
#print(matrix)
for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[i-1]==s2[j-1]:
            M[i][j]=max(M[i-1][j-1]+match, M[i-1][j]+gap, M[i][j-1]+gap, 0)
        else:
            M[i][j]=max(M[i-1][j-1]+mismatch, M[i-1][j]+gap, M[i][j-1]+gap, 0)

score=0
i=0
j=0
s1_alignment=[]
s2_alignment=[]

for a in range(1, m+1):
    for b in range(1, n+1):
        if score < M[a][b]:
            score = M[a][b]
            i=a
            j=b

while M[i][j]!=0:
    if s1[i-1]==s2[j-1]:
        s1_alignment.insert(0, s1[i-1])
        s2_alignment.insert(0, s2[j-1])
        i-=1
        j-=1
    elif M[i][j]==M[i-1][j]+gap:
        s1_alignment.insert(0, s1[i-1])
        s2_alignment.insert(0, '-')
        i-=1
    elif M[i][j]==M[i][j-1]+gap:
        s1_alignment.insert(0, '-')
        s2_alignment.insert(0, s2[j-1])
        j-=1
    else:
        s1_alignment.insert(0, s1[i-1])
        s2_alignment.insert(0, s2[j-1])
        i-=1
        j-=1

s1_alignment=''.join(s1_alignment)
s2_alignment=''.join(s2_alignment)

with open('sw.txt', 'w') as outFile:
    outFile.write(f's1: {s1_alignment}\n')
    outFile.write(f's2: {s2_alignment}\n')
    outFile.write(f'score: {score}')