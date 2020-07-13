#Version Python 3.7.5

#Import gzip, os argparse and BIOPython libraries
import gzip
import os
from os import path
from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import argparse

# Create Function to split the fastq.gz to barcode and sequence files
def barcode_split(input_file,output_seq,output_bar,length_barcode):
    with gzip.open(input_file,'rt') as handle ,open(output_seq, "w") as data_seq , open(output_bar, "w") as data_bar: # Here we open the gz file and also open sequence and barcode file to write in
        for (title, sequence, quality) in FastqGeneralIterator(handle): # Here we are parsing the fastq file and splitting it to title, sequence and quality
          if title.startswith("@"): # Every sequence in fastq file always starts with @
              continue
          else:# Here we are dividing the sequence and barcode file based on length of barcode
              data_seq.write("{}\n{}\n+\n{}\n".format('@'+title, sequence[length_barcode:], quality[length_barcode:])) 
              data_bar.write("{}\n{}\n+\n{}\n".format('@'+title, sequence[:length_barcode], quality[:length_barcode]))
    return print("Your files are ready")

# Make a command line interface using Argparse
parser = argparse.ArgumentParser(description="Extract Barcodes for Qiime2 analysis")
parser.add_argument("-i","--input",type=str,help="Input fastq file" ,required= True)
parser.add_argument("-l","--length",type=int,help="Length of barcode",required= True)
parser.add_argument("-o","--output",type=str,help = "Output Path for barcode and sequence fastq file; Optional if not given will paste files to current working directory")
args = parser.parse_args()
input_file = args.input
length_barcode = args.length
output_path = args.output
output_seq = os.path.join(output_path,"sequence.fastq")
output_bar = os.path.join(output_path,"barcode.fastq")

# Checking if given output directory is available If not creating the directory
if path.exists(output_path) == True:
    barcode_split(input_file,output_seq,output_bar,length_barcode)
else:
    os.mkdir(output_path)
    barcode_split(input_file,output_seq,output_bar,length_barcode)

