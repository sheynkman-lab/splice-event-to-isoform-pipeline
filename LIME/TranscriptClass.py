import pandas as pd
class Transcript():
    def __init__(self, gene_id, gene_name, transcript_id, feature, seqname, strand, tpm_WTC11, tpm_EC, exonsdict):
        self.gene_id = gene_id
        self.gene_name = gene_name
        self.transcript_id = transcript_id
        self.feature = feature
        self.seqname = seqname
        self.strand = strand
        self.tpm_WTC11 = tpm_WTC11
        self.tpm_EC = tpm_EC
        self.exonsdict = exonsdict
        self.junctionString = Transcript.makeJunctionString(self, self.exonsdict)
        self.UJC = Transcript.makeUJC(self)
        self.row = Transcript.rowDict(self)
    
    def makeUJC(self):
        printstring = self.seqname + "|" + self.strand + "|" + self.transcript_id + "|" + self.junctionString
        return(printstring)

    def rowDict(self):
        row = {"gene_id":self.gene_id, "gene_name":self.gene_name, "transcript_id":self.transcript_id, "feature":self.feature, "tpm_WTC11":self.tpm_WTC11, "tpm_EC":self.tpm_EC, "UJC": self.UJC}
        row = pd.Series(row)
        return row
        
    def makeJunctionString(self, exonsdict):
        junctionString = ""
        for i in exonsdict:
            if i+1 in exonsdict:
                exon = exonsdict[i]
                next_exon = exonsdict[i+1]
                junction = str(exon[1]) + "-" + str(next_exon[0]-1)
                junctionString = junctionString + junction
                if i+2 in exonsdict:
                    junctionString = junctionString + ":"
        return junctionString 

