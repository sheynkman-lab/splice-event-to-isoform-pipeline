import pandas as pd
from makeEvents import *
from structures import *
from getTranscripts import *
import os
from gtfparse import read_gtf

#pseudocode map(eventDict, transcriptDict):
    #make an empty dictionary dict
    # for each gene:
        # get the transcripts
        # get the junction strings of the transcripts
        # get the events
        # get the junction strings of the events
        # for each transcript:
            #initialize an eventList
            #for each event:
                # if the event junction is in the isoform junction:
                    # add the event ID to the eventList
            #dict[transcript_id] = eventList
    #return the dictionary


def main():
    srSource = "rmats"
    lrSource = "pacbio"
    eventTypes = ("se", "mxe", "a3ss", "a5ss")
    eventDict = {}
    for eventType in eventTypes:
        filepath = "/Volumes/sheynkman/projects/shay_thesis/data/chr19-rmats-maserproc/" + eventType + "TCF3.csv"
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

main()