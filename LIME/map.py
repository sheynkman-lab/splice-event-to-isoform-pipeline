import pandas as pd
from readData import *
import os

# returns simple dictionary of transcript_id --> mapDict
# should write a function to use this to create transcript-centric table & event-centric table


def getTranscriptDict(mergeannotquants):
    mergeannotquants = pd.read_table(mergeannotquants)
    LRDict = {}
    return LRDict

def mappingEventsToTranscripts(eventTable, transcriptDict):
    mapDict = {}
    for transcript_id in transcriptDict:
        rmatsEventList = []
        for index, row in eventTable.iterrows():
            if str(row["incJunction"]) in str(transcriptDict["transcript_id"]):
                rmatsEventList.append(row["incID"])
            elif str(row["excJunction"]) in str(transcriptDict["transcript_id"]):
                rmatsEventList.append(row["excID"])
        mapDict[transcript_id] = rmatsEventList
    return mapDict

