#!/bin/sh
python json2tsv.py noisy-corpus.json corpus.de-en.txt

echo "Running bifixer"
python /home/alin/software/bifixer/bifixer/bifixer.py corpus.de-en.txt corpus.fixed-dedup.txt de en --aggressive_dedup --scol 1 --tcol 2

sort -t $'\t' -k 3,3 -u corpus.fixed-dedup.txt | cut -d $'\t' -f1,2 > corpus.nodup.txt

echo "Running bicleaner"
bicleaner-hardrules --annotated_output --disable_porn_removal -s de -t en --scol 1 --tcol 2 --metadata de-en.yaml corpus.nodup.txt corpus.hard

python filter.py corpus.hard corpus.clean hardfilters.csv
