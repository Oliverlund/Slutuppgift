import argparse, os, datetime, csv

x = datetime.datetime.now()

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, help="increase output file verbosity")
args = parser.parse_args()
print(args.file)
with open(args.file, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['first_name'].lower()[0:3] + row['last_name'].lower()[0:3] + (str(x.year)[-2: ] + (" ") + row['email'].lower() + (" ") + row['department'.lower()]))

