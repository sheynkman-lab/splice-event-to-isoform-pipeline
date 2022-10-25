import pandas as pd
from map import *
from getEvents import *
from structures import *
from getTranscripts import *
from getEvents import *
from convertToTable import *
import os
from gtfparse import read_gtf

def main():
    # step 0: determine source of SR data
    srSource = "rmats"
    lrSource = "pacbio"

    #implement later: if statement for source event types, to accommodate variation
    eventTypes = ("se", "mxe", "a3ss", "a5ss")
    # init empty dictionary for tool
    eventDict = {}

    for eventType in eventTypes:
        filepath = "/Volumes/sheynkman/projects/shay_thesis/data/chr19-rmats-maserproc/" + eventType + "Toy.csv"
        if eventType == "se":
            se = pd.read_csv(filepath, index_col = 0)
            
        elif eventType == "mxe":
            mxe = pd.read_csv(filepath, index_col = 0)
                    
        elif eventType == "a3ss":
            a3ss = pd.read_csv(filepath, index_col = 0)
            
        elif eventType == "a5ss":
            a5ss = pd.read_csv(filepath, index_col = 0)

        else:
            print("Error: event type not registered")
    
    eventDict = getEvents(se, srSource, "se", eventDict)
    eventDict = getEvents(mxe, srSource, "mxe", eventDict)
    eventDict = getEvents(a3ss, srSource, "a3ss", eventDict)
    eventDict = getEvents(a5ss, srSource, "a5ss", eventDict)
    eventTable = EventDictToTable(eventDict)
    
    filepath = "/Volumes/sheynkman/projects/shay_thesis/data/chr19-lr-proc/ayk.csv"
    transcriptDict = getTranscripts(filepath)
    transcriptTable = TranscriptDictToTable(transcriptDict)

    #transcriptTableSmall = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/data/chr19-lr-proc/ayk_post-test.csv", index_col = 0) 
    
    mapTable = mappingEventsToTranscripts(eventTable, transcriptTable)
    outputpath = "/Volumes/sheynkman/projects/shay_thesis/output/mapping_test_1.csv"
    mapTable.to_csv(outputpath)

main()
