import pandas as pd
from getEvents import *
from structures import *
import os
from gtfparse import read_gtf
from readData import *
    

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