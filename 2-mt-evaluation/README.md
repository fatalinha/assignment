# MT Evaluation

Comparison of two system outputs. Since no linguistic knowledge of the target is required, we here focus on automatic evaluation.

## Automatic scores

 - BLEU - n-gram string similarity
 - chrF2 - Character F score
 - TER   - edit-distance-based
- COMET - embedding-based, also considers source

## Inspection through MT-telescope
 telescope compare -s source.txt -x system1.txt -y system2.txt -r reference.txt -l ro -m COMET -o .
 
 ![Bucket analysis of the COMET scores for the two system outputs](https://github.com/fatalinha/assignment/blob/main/2-mt-evaluation/bucket-analysis.png)
