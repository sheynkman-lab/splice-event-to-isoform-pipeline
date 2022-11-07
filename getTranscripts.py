import pandas as pd
from getEvents import *
from structures import *
import os
from gtfparse import read_gtf
from readData import *

def main():
    LRannot = loadLRannot("/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/03_chr19_gtfs/chr19_EC.gtf")
    LRquant_c1 = loadLRquant("/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/WTC11-1.tsv", "rep1ENCSR507JOF", "WTC11")
    LRquant_c2 = loadLRquant("/Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/EC.tsv", "rep1ENCSR148IIG", "EC")
    LRmergeddf = mergeAnnotQuants(LRannot, LRquant_c1, LRquant_c2)
    # getTranscripts(LRmergeddf)
    

# TO DO: REWRITE GET TRANSCRIPTS

def getTranscripts(filepath):
    # making assumption that PacBio data has been converted into csv file
    df = pd.read_csv(filepath, index_col = 0)
    #grouped for each isoform
    grouped = df.groupby('transcript_id')
    TranscriptDict = {}
    #for all entries corresponding to each isoform
    for transcript_id, group in grouped: 
        #initialize empty list of exons
        ExonsDict = {}
        #for each entry corresponding to an isoform
        for index, row in group.iterrows():
            #add all exons as lists to the dictionary
            if row[5] == "exon":
                exon_number = int(row[9])
                start = row[1]
                stop = row[2]
                exonRange = [start, stop]
                ExonsDict[exon_number] = exonRange
            #store the gene_id and gene_name corresponding to the isoform
            gene_id = row[6]
            gene_name = row[7]
            #make a Transcript object for the isoform
            tmp_transcript = Transcript(transcript_id, ExonsDict, gene_name, gene_id)
            TranscriptDict[transcript_id] = tmp_transcript
    return TranscriptDict

main()

# def getTranscripts(filepath):
#     # making assumption that PacBio data has been converted into csv file
#     df = pd.read_csv(filepath, index_col = 0)
#     #grouped for each isoform
#     grouped = df.groupby('transcript_id')
#     TranscriptDict = {}
#     #for all entries corresponding to each isoform
#     for transcript_id, group in grouped: 
#         #initialize empty list of exons
#         ExonsDict = {}
#         #for each entry corresponding to an isoform
#         for index, row in group.iterrows():
#             #add all exons as lists to the dictionary
#             if row[5] == "exon":
#                 exon_number = int(row[9])
#                 start = row[1]
#                 stop = row[2]
#                 exonRange = [start, stop]
#                 ExonsDict[exon_number] = exonRange
#             #store the gene_id and gene_name corresponding to the isoform
#             gene_id = row[6]
#             gene_name = row[7]
#             #make a Transcript object for the isoform
#             tmp_transcript = Transcript(transcript_id, ExonsDict, gene_name, gene_id)
#             TranscriptDict[transcript_id] = tmp_transcript
#     return TranscriptDict