# MT Evaluation

Comparison of two system outputs. Since no linguistic knowledge of the target is required, we here focus on automatic evaluation.

## Automatic scores
We select the automatic metrics to run in such a way that they can mirror different aspects of the outputs.
- **BLEU** - n-gram string similarity
- **chrF2** - Character F score
- **TER**   - edit-distance-based
- **COMET** - embedding-based, also considers source

SacreBLEU (https://github.com/mjpost/sacreBLEU): Compute BLEU, chrF2, TER and bootstrap resampling test. 

`sacrebleu  reference.txt -i system1.txt system2.txt -m bleu chrf ter `

Note: COMET score is obtained through MT-telescope (see below)


### Scores
| System | BLEU (μ ± 95% CI) | chrF2 (μ ± 95% CI) | TER (μ ± 95% CI) | COMET |
|-----------------------|-----------|-----------|-----------|----------------|
| system1.txt | 35.5 (35.5 ± 0.9) | 62.0 (62.0 ± 0.6) | 51.0 (51.0 ± 0.8) | 0.826 |
| system2.txt | 27.9 (27.9 ± 0.8) | 55.7 (55.7 ± 0.6) | 59.6 (59.5 ± 0.8) | 0.623 |
| bootstrap resampling | (p = 0.0010)* | (p = 0.0010)* | (p = 0.0010)* |

All metrics agree in ranking the output of system 1 higher than that of system 2. The statistical tests for all three metrics show that, assuming a significance threshold of 0.05, the null hypothesis can be rejected, which means that system 2 is significantly different than system 1. 

Metric signatures

    BLEU nrefs:1|bs:1000|seed:12345|case:mixed|eff:no|tok:13a|smooth:exp|version:2.0.0
    chrF2 nrefs:1|bs:1000|seed:12345|case:mixed|eff:yes|nc:6|nw:0|space:no|version:2.0.0
    TER nrefs:1|bs:1000|seed:12345|case:lc|tok:tercom|norm:no|punct:yes|asian:no|version:2.0.0

## Inspection through MT-telescope
The automatic metrics showed that the output of system 1 is better than system 2 based on the provided reference (and source). But let's further analyse and compare the outputs and the segments based on COMET. We use MT-telescope https://github.com/Unbabel/MT-Telescope . 
 ` telescope compare -s source.txt -x system1.txt -y system2.txt -r reference.txt -l ro -m COMET -o .`
 
 
Bucket analysis: Shows the percentage of sentences falling in buckets of different quality.  
 ![Bucket analysis of the COMET scores for the two system outputs](https://github.com/fatalinha/assignment/blob/main/2-mt-evaluation/bucket-analysis.png)

The graph shows that system 1 has a much higher percentage of high quality segments (dark green) than system 2. Additionally, system 2 has a 15% of segments of critical quality (red). The analysis shows that not only is the output of system 1 better than that of system 2, but system 1 avoids catastrophic errors, which can be detrimental for user experience. Overall, system 1 appears to be a better system.
