# MT Evaluation

Comparison of two system outputs. Since no linguistic knowledge of the target is required, we here focus on automatic evaluation.

## Automatic scores

 - BLEU - n-gram string similarity
 - chrF2 - Character F score
 - TER   - edit-distance-based
- COMET - embedding-based, also considers source

## Inspection through MT-telescope
 telescope compare -s source.txt -x system1.txt -y system2.txt -r reference.txt -l ro -m COMET -o .
 
 ![alttext]()
