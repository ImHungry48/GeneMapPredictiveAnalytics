import sys

def createParitions(read, n):
  partition_list = []
  for i in range(0, len(read), n):
    partition_list.append(read[i:i+n])
  return partition_list

def identifyMismatches(read_partitions, text_string):
  mismatch_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}  
  visited_text_substrings = []
  
  # Sliding window for comparing pattern string to text
  for partition_number in range(0, len(read_partitions)):
    partition = read_partitions[partition_number]
    if partition in kmer_index:
      for index in kmer_index[partition]:
        # Check previous indexes as needed
        for prefix_index in range(index, index - 1 - 6*partition_number, -1):
          if (prefix_index >= 0):
            # This is potentially huge every single time since text_string can be enormous.
            # You need to only be isolating the potential partition using its relative position in the sequence.
            visited_text_substring = text_string[prefix_index:]
            if len(pattern) <= len(visited_text_substring) and (visited_text_substring not in visited_text_substrings):
              mismatches_total = getNumMismatches(pattern, visited_text_substring)
              visited_text_substrings.append(visited_text_substring)
              if mismatches_total <= 4:
                mismatch_dict[mismatches_total].append(str(prefix_index))
                # If mismatches are greater than allowable value you should continue to the next read!
                # If you keep working on it the answer isn't going to change.
  return mismatch_dict
  
# Helper function to get number of mismatches
def getNumMismatches(pattern, text_substring):
  mismatches_total = 0
  for index in range(0, len(pattern)):
    if pattern[index] != text_substring[index]:
      mismatches_total += 1
  return mismatches_total
  
# Store command line argument
FASTAFile = sys.argv[1]
FASTQFile = sys.argv[2]
outputFile = sys.argv[3]

# Store keys and matches
kmer_index = {}
matches = {}

# Set k-mer value based on max amount of mismatches
max_m = 4
pattern_length = 30
k_val = int(pattern_length / (max_m + 1)) # len(P) / m = 6

# Create empty strings to hold bases for T and P and matches
text_string = ''
pattern_strings = []

# Open files to read
FASTAFile_object = open(FASTAFile, "r")
FASTQFile_object = open(FASTQFile, "r")

# Read files lines of FASTQ
FASTQ_lines = FASTQFile_object.readlines()

# Get the pattern strings into a list
for index in range(len(FASTQ_lines)):
    if ((index + 1) % 2 == 0 and (index + 1) % 4 != 0):
        current_string = FASTQ_lines[index]
        current_string = current_string.rstrip()
        # Ignore duplicates
        if current_string not in pattern_strings:
          cnt = 0
          for ch in current_string:
              if not ch in 'ACGT':
                cnt += 1
          if cnt == 0:
            pattern_strings.append(current_string)

# Ignore first line of FASTA file
FASTAFile_object.readline()

# Create a single string to move window on based on FASTA contents
while 1:
    char = FASTAFile_object.read(1)
    if not char:
        break
    if char != '\n':
        text_string += char

# Sliding window to build the k-mer index from FASTA contents
for i in range(0, len(text_string)):
  if i >= k_val - 1:
    current_substring = text_string[i - (k_val - 1): i + 1]
    if current_substring in kmer_index:
      kmer_index[current_substring].append(i - (k_val - 1))
    else:
        kmer_index[current_substring] = []
        kmer_index[current_substring].append(i - (k_val - 1))

# Open file to write
outputFile_object = open(outputFile, "w")

# Calculate partition matches
for pattern in pattern_strings:
  # Create the partitions
  read_partitions = createParitions(pattern, k_val)
  
  # Iterate through each partition and check for matches
  # Write output to file
  for index in range(0, len(read_partitions)):
    partition = read_partitions[index]
    if partition in kmer_index:
      outputFile_object.write(str(len(kmer_index[partition])) + " ")
    else:
      outputFile_object.write("0 ")
  
  # Check entire pattern for mismatches
  mismatch_dict = identifyMismatches(read_partitions, text_string)
  mismatch_dict_keys = list(mismatch_dict.keys())
  
  # Write the mismatches found for entire pattern read to output file
  for index in range(0, len(mismatch_dict_keys)):
    key = mismatch_dict_keys[index]
    mismatch_dict[key].sort(key=float)
    outputFile_object.write(str(key) + ":")
    # NOTE: if condition is only for resolving spacing
    if index < len(mismatch_dict_keys) - 1:
      outputFile_object.write(','.join(mismatch_dict[key]) + " ")
    else:
      outputFile_object.write(','.join(mismatch_dict[key]))
  
  # Add new line for next pattern read
  outputFile_object.write('\n')