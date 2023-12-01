import sys

def match(s,chr,lst):
    l = []
    counter = 0
    for i in lst:
        part_s = s[i:i+len(chr)]
        if len(part_s) >= len(chr):
            if part_s == chr:
                l.append(i)
        counter += 1
    return l

fasta = sys.argv[1]
outfile = sys.argv[3]
fastq = sys.argv[2]
f = open(fasta,"r")
out = open(outfile,"w")
fastq = open(fastq,"r")
first_line = f.readline() #Ignore the first line ; Not a sequence 
read_fastq = fastq.readlines()
s= ""
k_mer = 6
dict = {}
matches_set = []
match_dict = {}
base = ['A','G','C','T']
while 1:
    # read by character
    char = f.read(1)         
    if not char:
        break
    if char != '\n' and char in base:
        s+= char
for i in range(0,len(s)):
    window = s[i:i+k_mer]
    if len(window) == k_mer:
        if window in dict:
            dict[window].append(i)

        else:
            dict[window] = []
            dict[window].append(i)
seq = ""
lines_sequence = [] #To get all the sequences for the P
for i in range(1,len(read_fastq),4):
    if read_fastq[i].rstrip() not in lines_sequence:
        lines_sequence.append(read_fastq[i].rstrip())


for line in lines_sequence: # Traversing through each line 
        windows = line[0:6] 
        if windows in dict:
            lst = dict[windows]
            matches = match(s,line,lst)
            if line in match_dict:
                if len(matches) > 0:
                    for i in matches:
                     match_dict[line].append(str(i))
            else : 
                if len(matches) > 0:
                 match_dict[line] = []
                 for i in matches:
                     match_dict[line].append(str(i))
                matches_set.append(line)
matches_set = list(set(matches_set))
keys = []
max_len = 0
max_key = []

for key,value in dict.items():
    if max_len < len(value):
            max_len = len(value)
for key in dict.keys():
    if len(dict[key]) == max_len:
        max_key.append(key)
max_key.sort()
out.write(','.join(max_key)+"\n")
c = 0
for i in match_dict.values():
    for j in i:
        c +=1
out.write(str(c)+"\n")
out.writelines('')
for keys in match_dict:
    out.writelines(keys + "\n")
    values = match_dict[keys]
    out.write(','.join(values)+"\n")
f.close()
fastq.close()
out.close()





            
