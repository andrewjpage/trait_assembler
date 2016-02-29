#Input format
The input spreadsheet consists of a CSV file with 3 columns:
1.) the path to the forward reads FASTQ file (optionally gzipped),
2.) the path to the reverse reads FASTQ file (if missing its treated as single ended),
3.) the trait. A 1 means it has the trait, a 0 means the trait is missing.

For example:
    
    sample1_1.fastq.gz,sample1_2.fastq.gz,1
    sample2_1.fastq.gz,sample2_2.fastq.gz,0
    /path/single_ended.fq,,1

