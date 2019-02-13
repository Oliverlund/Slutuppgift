import argparse, os, datetime, csv

meny = 0
x = datetime.datetime.now()

print("*** Skapa flera användare genom CSV-fil ***")

while meny != 2:

    try: 
        meny = int(input("Gör ett val: "))
    
    except:
        print("Gör ett korrekt val!")

    print("1. Skapa användare",
    "2. Avsluta")

    if meny == 1:
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", "-f", type=str, help="increase output file verbosity")
        args = parser.parse_args()
        print(.file)
        with open(.file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row[''].lower()[0:3] + row[''].lower()[0:3] + (str(x.year)[-2: ]))
    
    else meny == 2:
        print("")



