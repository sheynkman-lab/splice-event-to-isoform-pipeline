from lib2to3.pgen2.token import RARROW
import pandas as pd
from makeEvents import *
from structures import *
import os
from gtfparse import read_gtf

def getTranscripts(filepath):
    # making assumption that PacBio data has been converted into csv file w/ tidy_df()
    df = pd.read_csv(filepath, index_col = 0)
    grouped = df.groupby('transcript_id')
    TranscriptDict = {}
    for transcript_id, group in grouped:
        #group is a dataframe for just the rows of this transcript ID
        ExonsDict = {}
        for index, row in group.iterrows():
            # print(type(row)) --> pandas series
            if row[5] == "exon":
                exon_number = int(row[9])
                start = row[1]
                stop = row[2]
                exonRange = [start, stop]
                ExonsDict[exon_number] = exonRange
        
        TranscriptDict[transcript_id] = ExonsDict
    
    TranscriptDictFinal = {}
    for transcript_id in TranscriptDict:
        ExonsDict = TranscriptDict[transcript_id]
        tmp_transcript = Transcript(transcript_id, ExonsDict)
        TranscriptDictFinal[transcript_id] = tmp_transcript

    return TranscriptDictFinal

def TranscriptsToPandas(TranscriptDict):
    transcript_id = list(TranscriptDict.keys())
    transcriptObjects = list()

def main():
    filepath = "/Volumes/sheynkman/projects/shay_thesis/data/chr19-lr-proc/aykshort.csv"
    TranscriptDict = getTranscripts(filepath)
    print(TranscriptsToPandas(TranscriptDict))
    #print(TranscriptDictFinal["ENST00000632506.1"])
main()