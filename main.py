import pandas as pd

def main():
    # step 0: determine source of SR data
    srSource = "rmats"
    lrSource = "pacbio"

    #implement later: if statement for source event types, to accommodate variation
    eventTypes = ("se", "mxe", "ri", "a3ss", "a5ss")
    # init empty dictionary for tool
    eventDict = {}

    #there has to be a 
    for eventType in eventTypes:
        filepath = "/Volumes/sheynkman/projects/shay_thesis/data/toy-rmats-maserproc/" + eventType + "Toy.csv"
        if eventType == "se":
            se = pd.read_csv(filepath, index_col = 0)
            
        elif eventType == "mxe":
            mxe = pd.read_csv(filepath, index_col = 0)
            
        elif eventType == "ri":
            ri = pd.read_csv(filepath, index_col = 0)
                    
        elif eventType == "a3ss":
            a3ss = pd.read_csv(filepath, index_col = 0)
            
        elif eventType == "a5ss":
            a5ss = pd.read_csv(filepath, index_col = 0)

        else:
            print("Error: event type not registered")

    #THIS IS INEFFICIENT; JUST TESTING IF IT WORKS! 
    #eventDict = makeEvents(se, srSource, "se", eventDict)
    #eventDict = makeEvents(mxe, srSource, "mxe", eventDict)

##    for eventType in eventTypes:
##        eventDict = makeEvents(eval(eventType), srSource, eventType, eventDict)
    eventDict = makeEvents(se, srSource, "se", eventDict)
    eventDict = makeEvents(mxe, srSource, "mxe", eventDict)
    eventDict = makeEvents(ri, srSource, "ri", eventDict)
    eventDict = makeEvents(a3ss, srSource, "a3ss", eventDict)
    eventDict = makeEvents(a5ss, srSource, "a5ss", eventDict)
    #print(eventDict)
    #print(len(eventDict))

##    Looping thru event maker function
##    for eventType in eventTypes:
##        makeEvents(eventType, srSource, eventType, eventDict)
