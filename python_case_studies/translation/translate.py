# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:42:24 2019

@author: User
"""

import table as data

def read_sequence():
    inputfile = "dna.txt"
    with open(inputfile,"r") as file:
        sequence = file.read()        
    sequence = sequence.replace("\n","").replace("\r","")
    return sequence  


def translate(sequence, table):    
    """
       Translate a string containing a nucleotide sequence into a string
       containing the corresponding sequence of amino acids . Nucleotides are 
       translated in triplets using the table dictionary; each amino acid 4 is 
       encoded with a string of length 1. 
       
    """
    protein=""
    if len(sequence)%3 ==0:        
        for i in range(0,len(sequence),3):
            considering_gene=sequence[i:i+3]
            protein = protein + table[considering_gene]
            
    return protein.replace("_","")

def cut_sequence(start,end,sequence):
    return sequence[start-1:end-1]


table= data.getTable()
sequence = read_sequence()
sequence = cut_sequence(21,939,sequence)

print(translate(sequence, table))
