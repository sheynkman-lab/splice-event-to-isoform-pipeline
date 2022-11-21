import pandas as pd
from archive.structures import *
from archive.getEvents import *
from LIME.getTranscripts import *
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

def mappingEventsToTranscripts(eventTable, transcriptTable):
    #print('test begin map')
    mapTable = pd.DataFrame(columns = ['transcript_id', 'mapped_events'])
    for index, transcript in transcriptTable.iterrows():
        gene = transcript["gene_name"]
        associatedEvents = []
        transcriptJunction = str(transcript["junctionString"])
        for index, event in eventTable.iterrows():
            if event["gene"] == gene:
                incjunction = str(event["incjunction"])
                excjunction = str(event["excjunction"])
                if incjunction in transcriptJunction:
                    #print("matched", event["eventid"], "to", transcript["transcript_id"])
                    associatedEvents.append(event["incid"])
                elif excjunction in transcriptJunction:
                    #print("matched", event["eventid"], "to", transcript["transcript_id"])
                    associatedEvents.append(event["excid"])

        ser = pd.Series({"transcript_id": transcript["transcript_id"], "mapped_events": associatedEvents})
        mapTable = pd.concat([mapTable, ser.to_frame().T], ignore_index = True)
    
    print(mapTable)
    return(mapTable)

    '''
    for transcript in transcriptTable:
        gene = transcript.gene_name
        associatedEvents = []
        for event in eventTable where event.gene == gene:
            if event.incjunctionString is in transcript.junctionString:
                associatedEvents.append(event.incid)
            else if event.excjunctionstring is in transcript.junctionstring:
                associatedEvents.append(event.excid)
        row = {"transcript_id" = transcript, "eventList" = associatedEvents}
        ser = pd.Series(row)
        transcriptTable = pd.concat([mapTable, ser.to_frame().T], ignore_index = True)
    '''