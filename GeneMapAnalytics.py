import sys
import Bio as bp
from Bio import SeqIO, Align
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import json

# ––––––––––––––––––––– Is this still needed? ––––––––––––––––––––– #

# Parses the OMIM genemap2.txt database to seperate each line into a 2D array
def parse_omim(omim):
    reads = []
    while True:
        line = omim.readline().strip()
        if (len(line) == 0):
            break
        segmented_line = line.split('\t')
        while("" in segmented_line):
            segmented_line.remove("")
        reads.append(segmented_line)
    return reads

# Goes through the array, removing all of the reads that have a gene sequence that's longer than max_len
def filter_results(parsed_omim, max_len):
    reads = []
    for entry in parsed_omim:
        start = entry[1]
        end = entry[2]
        if (int(end) - int(start) < max_len):
            reads.append(entry)
    return reads

# Prints out the names of the genes from a filtered_omim array, these kind of describe what the gene is for
def print_gene_names(filtered_omim):
  for element in filtered_omim:
    print(element[7])

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #


# –––––––––––––––––––––—— New Code: Matching –––––––––––––––––––––—— #

# Approximate matching algorithm between two genomes
def approximate_match(good_genome, patient_genome):

  
  # If we can use the biopython code:
  aligner = Align.PairwiseAligner()
  # aligner.mode = 'global' #Default mode is global, can switch over to local alignment mode when needed 
  score = aligner.score(good_genome, patient_genome) 
  # pairwise2.align.
  
  pass


# Get the good genome from a hardcoded file
def get_good_genes():
  # Get the good genome from our database
  # Need to find the file again and put in the repository
  # and import from hardcoded file
  filename = "" #TODO: Replace with actual filename
  filename = open(filename, "r")
  
  return FastqGeneralIterator(filename)


# Gets the patient genome from a given filename
def get_patient_genes(filename):
  open_file = open(filename, "r")
  # Assuming Fastq format:
  
  # Quality-based filtering form:
  # genome = SeqIO.parse(open_file, "fastq")
  # Filtering on quality scores?
  
  
  # Fast form if we find that the above takes too long:
  # Operates on tuples of (title, sequence, quality) rather than SeqRecord objects
  # genome = SeqIO.QualityIO.FastqGeneralIterator(open_file)


# Runs the different analyses on the patient genome
# Returns a dictionary of the results
def run_analysis(patient_genome, good_genome):
  # First do 
  pass

# Converts the results dictionary to a JSON string to be sent to the frontend
def send_json(results):
  return json.dumps(results)

def main():
  filename = sys.args[1]
  
  good_genome = get_good_genes()
  patient_genome = get_patient_genes(filename)
  results = run_analysis(patient_genome,good_genome)
  
  return send_json(results)