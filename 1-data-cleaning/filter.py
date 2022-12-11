""" Assignment: data cleaning Dec 2022
Transform json corpus file to tsv containing source target columns

Usage: python filter.py scored_corpus clean_corpus statistics_file """
import sys

scored_corpus = sys.argv[1]
clean_corpus = sys.argv[2]
stat_file = sys.argv[3]
filters = dict()
filters['porn'] = []
porn_filter = [' fuck', ' cock ', ' ass ']

print("Processing...")
with open(scored_corpus) as inf, open(clean_corpus, 'w') as clean:
    for line in inf:
        line = line.rstrip().split('\t')
        de = line[0]
        en = line[1]
        rule = line[3]
        if rule == 'keep':
            if any(w in en for w in porn_filter):
                filters['porn'].append('\t'.join([de, en]))
            else:
                clean.write('\t'.join([de, en]) + '\n')
        else:
            if rule not in filters.keys():
                filters[rule] = []
            filters[rule].append('\t'.join([de, en]))
print("Clean corpus written in " + str(clean_corpus))

stats = dict()
for key, value in filters.items():
    stats[key]= len(value)
sorted_stats = sorted(stats.items(), key=lambda x:x[1], reverse=True)
print('Writing statistics to ' + stat_file)
with open(stat_file, 'w') as out:
    out.write('\t'.join(["Filter", "Sentences"]) + '\n')
    total_removed = 0
    for f in sorted_stats:
        out.write('\t'.join([f[0], str(f[1])]) + '\n')
        total_removed += f[1]
    out.write('\t'.join(["Total", str(total_removed)]))
print("Total sentences removed: " + str(total_removed))
