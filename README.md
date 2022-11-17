# Long-read Isoform Mapping to (Alternative Splicing) Events (LIME) (or LIMASE) (this is a working title)

## Data input
> Currently, data is stored in Sheynkman Lab project storage; description of input data will be followed by a path to the corresponding files in project storage

- Short read alternative splicing events 
    - rMATS output: a pathway to rMATS output *folder*
        - In project storage: /Volumes/sheynkman/projects/EC_stem_cell_differentiation/001_ips-s1s2/003_ips-s1s2_output/002_ips-s1s2_rmats-out  
- Long read sequencing data
    - Transcript annotation file (GTF) for condition 1:
        - In project storage: /Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/03_chr19_gtfs/chr19_EC.gtf
    - Transcript quantification file (TSV) for condition 1 and condition 2:
        - In project storage, condition 1: /Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/WTC11-1.tsv"
        - In project storage, condition 2: /Volumes/sheynkman/projects/shay_thesis/data/EC-LR/long-read-EC-data/01_tsv/EC.tsv

## Running script:
    - Run main.py to load in short read and long read data as Pandas dataframe
        - references readData.py to load in short read events as Pandas df, construct junction strings for inclusion/exclusion events, append event type/inclusion/exclusion-specific IDs, load annotation file into pandas, load quantification files into pandas, merge, calculate TPM
        - main.py also constructs a dictionary of {transcript_id:junctionString} based on long read GTF