import os, glob, json, pandas as pd

def main():
    DATA = []
    jfiles = glob.glob("data/**/*.json", recursive=True)
    for i, jf in enumerate(jfiles):
        if i == 0: df = pd.read_json(jf)
        else: df = pd.concat([df, pd.read_json(jf)])
    print(df.head())

if __name__ == "__main__":
    main()