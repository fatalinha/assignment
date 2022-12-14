# Data cleaning
The given corpus is very noisy. Main issues:
* Bad text: encoding, spelling, trailing spaces
* Wrong language in source or target
* Misalignments
* Low-value segments: Non-text characters, non-fluent text
* Offensive language

## Approach
1) Fix issues to preserve possibly useful content
2) Filter out problematic sentences

### Fix
Fixing the issues is dome with the tool Bifixer https://github.com/bitextor/bifixer
* Fix issues (spelling, HTML, tokenisation etc), normalise punctuation, remove empty
* resegment long lines (>15 words)
* detect (near-)duplicates using hashes (using --aggressive_dedup)

`python bifixer/bifixer.py corpus.de-en.txt corpus.fixed-dedup.txt de en --aggressive_dedup --scol 1 --tcol 2`

### Filter
1) Remove duplicates based on identical hashes and keep only the source-target text in the file 

The two following segments have the same hash even if they are not identical. This means that they are identified as near-duplicates and can be removed.

| Source | Target | Hash | Score |
|--------|--------|------|-----------|
| April 1961:  |   April 1961:  |   **00714cc78651a098**  |    73.0 |
| April 2002   |   April 2013   |   **00714cc78651a098**    |    73.3 |

`sort -t $'\t' -k 3,3 -u corpus.fixed-dedup.en-de.txt | cut -d $'\t' -f1,2 > corpus.nodup.en-de.txt`

2) Now that duplicates are removed, we use Bicleaner https://github.com/bitextor/bicleaner to score segments based on some criteria.
 
Download language pack en-de from https://github.com/bitextor/bicleaner-data/releases/download/v1.5/en-de.tar.gz. Use the metadata file provided in this repository.

We use a hard-rule classifier to filter out:
- problematic sentences (too long, too short, with large S/T length ratio, containing wrong language)
- low-value sentences (only non-text, numbers, titles, breadcrumps, non-fluent sentences based on LM score)
- porn filter (implemented separately): removes sentences containing [^fuck.\*, ^ass$, ^cock$]

`bicleaner-hardrules --annotated_output --disable_porn_removal -s de -t en --scol 1 --tcol 2 --metadata de-en.yaml corpus.nodup.en-de.txt corpus.hard`

|          Filter     	| Sentences filtered |
|-----------------------|-----------|
| not_too_short(left) |	174893 |
| no_wrong_language(left) |	169610 |
| length_ratio(left,right) |	79075 |
| no_wrong_language(right) |	61156 |
| not_too_short(right) |	50481 |
| no_identical(left,right) |	50328 |
| lm_filter(left,right) |	34952 |
| no_unicode_noise(left) |	33052 |
| no_titles(left,right) |	25979 |
| no_repeated_words(left) |	15463 |
| no_glued_words(left) |	11667 |
| no_repeated_words(right) |	6100 |
| no_glued_words(right) |	5843 |
| no_literals(left) |	4384 |
| no_paren(left,right) |	4071 |
| not_too_long(left) |	2981 |
| no_literals(right) |	2394 |
| no_only_numbers(left) |	2192 |
| no_unicode_noise(right) |	1898 |
| no_only_numbers(right) |	1784 |
| no_only_symbols(left)	| 1411 |
| no_only_symbols(right) | 1272 |
| not_too_long(right)	 | 783 |
| no_bad_encoding(left)	| 715 |
| no_bad_encoding(right)	| 578 |
| no_breadcrumbs(left) |	466 |
| no_space_noise(left)	| 339 |
| no_breadcrumbs(right)	| 330 |
| no_space_noise(right)	| 247 |
| porn	| 52 |
| no_escaped_unicode(left) |	19 |
| no_escaped_unicode(right)	| 2 |
| **Total**	            | 744517 |

As shown in the table of filtered sentences, the main issues are too short segments, unbalanced sentence ratio, wrong language and unfluent segments.

## Corpus Statistics:
| Corpus  | Sentences |  Words |
|----------|----------|--------|
| Original | 1039252 | 19641988 |
| Resegmentation and fix | 1067502 | 21487686 |
| Remove duplicates | 917328 | 18191989 |
| Hard rules (final) | 172811  | 5343510 |

The clean corpus can be found here: https://u.pcloud.link/publink/show?code=XZ8c0DVZNoP1OUl0IvkJPVdDcBodwhNRbGHX

## Further issues: Misalignments
We may have removed a lot of problematic and low-value segments, but we can still observe many segments in which the source-target are not translations of each other  (misaligned segments). So the next step is to identify these segments. There are different possible approaches to this problem:
- Check for number and punctuation mismatches between source-target
- Sentence embedding cosine similarity source-target e.g. using LASER embeddings
- Translate source sentence with MT and compare to similarity to target (either using surface metrics or embeddings)
