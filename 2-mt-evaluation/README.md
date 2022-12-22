# MT Evaluation

Comparison of two system outputs. Since no linguistic knowledge of the target is required, we here focus on automatic evaluation.

## Automatic scores
We select the automatic metrics to run in such a way that they can mirror different aspects of the outputs.
- BLEU - n-gram string similarity
- chrF2 - Character F score
- TER   - edit-distance-based
- COMET - embedding-based, also considers source

SacreBLEU: Compute BLEU, chrF2, TER and bootstrap resampling test. 
`sacrebleu `

Note: COMET is obtained through MT-telescope (see below)


### Scores
| System | BLEU (μ ± 95% CI) | chrF2 (μ ± 95% CI) | TER (μ ± 95% CI) | COMET |
|-----------------------|-----------|-----------|-----------|----------------|
| system1.txt | 35.5 (35.5 ± 0.9) | 62.0 (62.0 ± 0.6) | 51.0 (51.0 ± 0.8) | 0.826 |
| system2.txt | 27.9 (27.9 ± 0.8) | 55.7 (55.7 ± 0.6) | 59.6 (59.5 ± 0.8) | 0.623 |
| bootstrap resampling | (p = 0.0010)* | (p = 0.0010)* | (p = 0.0010)* |

All metrics agree in ranking the output of system1 higher. The statistical tests show that, assuming a significance threshold of 0.05, the null hypothesis can be rejected, which means that system2 is significantly different than system1.

Metric signatures

    BLEU nrefs:1|bs:1000|seed:12345|case:mixed|eff:no|tok:13a|smooth:exp|version:2.0.0
    chrF2 nrefs:1|bs:1000|seed:12345|case:mixed|eff:yes|nc:6|nw:0|space:no|version:2.0.0
    TER nrefs:1|bs:1000|seed:12345|case:lc|tok:tercom|norm:no|punct:yes|asian:no|version:2.0.0

## Inspection through MT-telescope
 ` telescope compare -s source.txt -x system1.txt -y system2.txt -r reference.txt -l ro -m COMET -o .`
 
 
Bucket analysis: Shows the percentage of sentences falling in buckets of different quality.  
 ![Bucket analysis of the COMET scores for the two system outputs](https://github.com/fatalinha/assignment/blob/main/2-mt-evaluation/bucket-analysis.png)

The graph shows that system1 has a much higher percentage of high quality segments (dark green) than system 2. System 2 also has a 15% of segments of critical quality (red).
