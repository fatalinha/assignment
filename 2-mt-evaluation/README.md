# MT Evaluation

Comparison of two system outputs. Since no linguistic knowledge of the target is required, we here focus on automatic evaluation.

## Automatic scores
We select the automatic metrics to run in such a way that they can mirror different aspects of the outputs.
- BLEU - n-gram string similarity
- chrF2 - Character F score
- TER   - edit-distance-based
- COMET - embedding-based, also considers source

SacreBLEU 
``

### Scores


## Inspection through MT-telescope
 ` telescope compare -s source.txt -x system1.txt -y system2.txt -r reference.txt -l ro -m COMET -o .`
 
 
Bucket analysis: Shows the percentage of sentences falling in buckets of different quality.  
 ![Bucket analysis of the COMET scores for the two system outputs](https://github.com/fatalinha/assignment/blob/main/2-mt-evaluation/bucket-analysis.png)

The graph shows that system1 has a much higher percentage of high quality segments (dark green) than system 2. System 2 also has a 15% of segments of critical quality (red).
