import pandas as pd
from makeEvents import *
from structures import *
from getTranscripts import *
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
    
    eventDict = makeEvents(se, srSource, "se", eventDict)
    eventDict = makeEvents(mxe, srSource, "mxe", eventDict)
    eventDict = makeEvents(a3ss, srSource, "a3ss", eventDict)
    eventDict = makeEvents(a5ss, srSource, "a5ss", eventDict)
    print(eventDict)

    filepath = "/Volumes/sheynkman/projects/shay_thesis/data/chr19-lr-proc/aykshort.csv"
    transcriptDict = getTranscripts(filepath)
    #eventDict has all events
    #transcriptDict has all transcripts 
    
    

main()
