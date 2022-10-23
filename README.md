# splice-event-to-isoform-pipeline
Shay's splice event to isoform integration pipeline

### structures.py: 
- all classes will be stored here
    - Event superclass
        - SE, MXE, RI, A3SS, A5SS subclasses 
            - Subclasses have a method defining inclusion & exclusion junction strings
    - To do: Transcript superclass (all isoforms of a gene)
        -  Isoform subclass (specific isoforms within a gene)

### makeEvents.py
- Current state: Given tidy input data, create a dictionary of all events (SE, MXE, RI, A3/A5SS) with unique ID as key & Event object as value

### main.py
- reading in tidy input data, calling makeEvents.py for each event type
 
### events-structures-main.py
- I am not familiar with how to reference the structures.py classes in other scripts like makeEvents.py/main.py, so this script just combines the contents of structures.py, makeEvents,py, and main.py 