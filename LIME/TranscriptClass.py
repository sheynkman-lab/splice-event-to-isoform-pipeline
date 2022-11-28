import pandas as pd
class Transcript():
    def __init__(self, transcript_id, ExonsDict, gene_name, gene_id, tpm_c1, tpm_c2):
        self.transcript_id = transcript_id
        self.ExonsDict = ExonsDict
        self.gene_name = gene_name
        self.gene_id = gene_id
        self.tpm_c1 = tpm_c1
        self.tpm_c2 = tpm_c2
        self.junctionString = Transcript.makeJunctionString(self)
        self.row = Transcript.rowDict(self)
    
    def __str__(self):
        printstring = self.transcript_id + " --> " + self.junctionString
        return(printstring)


    def rowDict(self):
        row = {"transcript_id" : self.transcript_id, "ExonsDict":self.ExonsDict, "gene_name":self.gene_name, "gene_id":self.gene_id, "junctionString":self.junctionString}
        return row

    def makeJunctionString(self):
        # ExonsDict = {1: [70928, 70945], 2: [66346, 66499]}
        # in GTF files, features go from left to right (upstream to downstream) when looking @ chromosome as we see in Browser track
        # if transcript is +, upstream coordinate is 5' end, downstream coordinate is 3' end
        # if transcript is -, first feature is most upstream ("end" is actually the start of the exon)
        # function in BioSurfer & SQANTI, etc
        # how handling negative strand vs. positive strand
        """
        
        """
        junctionString = ""
        for i in self.ExonsDict:
            if i+1 in self.ExonsDict:
                exon = self.ExonsDict[i]
                next_exon = self.ExonsDict[i+1]
                junction = str(exon[1]) + "-" + str(next_exon[0])
                junctionString = junctionString + junction + ":"
        return junctionString 

