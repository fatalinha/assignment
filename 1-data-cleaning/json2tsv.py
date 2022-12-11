""" Assignment: data cleaning Dec 2022
Transform json corpus file to tsv containing source target columns

Usage: python json2tsv.py input output"""
import sys
import pandas as pd

input_text = sys.argv[1]
output_text = sys.argv[2]

print("Converting corpus to tsv")
df = pd.read_json(input_text, lines = True)
df.to_csv(output_text, sep="\t", index = False)
print("Done!")