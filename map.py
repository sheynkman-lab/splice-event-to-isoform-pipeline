import pandas as pd
from structures import *
from getEvents import *
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

def map(eventDict, transcriptDict):
    mapDict = {}
    