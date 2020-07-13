# Barcode-extract
Use this python script to extract barcodes from your fastq.gz file for Qiime 2 analysis
Before running install the following package:
Biopython:
pip install biopython

To run barcode_split.py:

python barcode_split.py -i "input fastq.gz file" -l "Barcode length" -o "output file path"

Output: Will generate a barcode file and sequence file which can be run in Qiime2
