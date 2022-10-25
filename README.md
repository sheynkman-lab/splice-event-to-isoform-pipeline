# splice-event-to-isoform-pipeline
Shay's splice event to isoform integration pipeline

### structures.py: 
- all classes will be stored here
    - Event superclass
        - Attributes:
            - source: tool used to call events
            - eventType: current functionality: "se", "mxe", "a3ss", "a5ss"
            - eventid: [eventType].[rMATS-assigned Event ID number]
            - ensg: ENSG key for associated gene
            - gene: Associated gene name
            - pvalue: Significance of delta PSI value
            - fdr: false discovery rate
            - dpsi: delta Percent Spliced In; measures extent to which event inclusion form prevalent in Condition 1 (dpsi>0) or Condition 2 (dpsi <0)
            - chrom: associated chromosome (format chr0)
            - strand: + or -
        - SE, MXE, A3SS, A5SS subclasses (missing RI)
            - Subclass-specific attributes:
                - SE
                    - target, upstream, downstream: exon ranges
                    - incjunction, excjunction: junction ranges for inclusion & exclusion form
                    - incid, excid: [eventid].["inc"/"exc"]
                    - row: dictionary of all attributes that can be ported into pd.Series and appended to pd.DataFrame
                - MXE
                    - exon1, exon2, upstream, downstream: exon ranges
                    - incjunction, excjunction: junction ranges for inclusion & exclusion form
                    - incid, excid: [eventid].["inc"/"exc"]
                    - row: dictionary of all attributes that can be ported into pd.Series and appended to pd.DataFrame
                - A3SS
                    - exonlong, exonshort, exonflanking: exon ranges
                    - incjunction, excjunction: junction ranges for inclusion & exclusion form
                    - incid, excid: [eventid].["inc"/"exc"]
                    - row: dictionary of all attributes that can be ported into pd.Series and appended to pd.DataFrame
                - A5SS
                    - exonlong, exonshort, exonflanking: exon ranges
                    - incjunction, excjunction: junction ranges for inclusion & exclusion form
                    - incid, excid: [eventid].["inc"/"exc"]
                    - row: dictionary of all values that can be ported into pd.Series and appended to pd.DataFrame
            - Subclass-specific methods:
                - rowDict(): returns dictionary of attributes that can be converted to pd.Series and appended to pd.DataFrame
                - inclusionJunctionString() and exclusionJunctionString(): returns strings corresponding to event's inclusion/exclusion form junctions
    - Transcript class
        - Attributes:
            - transcript_id: Isoform transcript-specific ID 
            - ExonsDict: Dictionary of all exon ranges. Key = exon number, value = list of exon start/stop values
            - gene_name: associated gene name
            - gene_id: associated gene ENSG
            - junctionString: string of all junctions for a transcript
            - row: dictionary of all attributes that can be ported into pd.Series and appended to pd.DataFrame
        - Methods:
            - rowDict(): returns dictionary of attributes that can be converted to pd.Series and appended to pd.DataFrame
            - makeJunctionString: returns a string of all junctions for a transcript

### getEvents.py
- returns a dictionary of Events
    - event ID: Event Object

### getTranscripts.py
- returns a dictionary of Transcripts
    - transcript ID: Transcript object

### convertToTable.py
- EventDictToTable(): takes in output of getEvents.py, returns pandas dataframe EventTable
- TranscriptDictToTable(): takes in output of getTranscripts.py, returns pandas dataframe TranscriptTable

### map.py
- takes in pandas dataframe of Events and Transcripts, returns a pandas dataframe with two rows, the transcript ID and a list of event IDs that have mapped

### main.py
- executes functions