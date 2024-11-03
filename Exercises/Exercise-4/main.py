import os, glob, json, pandas as pd

def main():
    DATA = []
    jfiles = glob.glob("data/**/*.json", recursive=True)
    for jd in jfiles:
        with open(jd, "r") as d:
            DATA.append(json.load(d))
        # if i == 0: df = pd.read_json(jf)
        # else: df = pd.concat([df, pd.read_json(jf)])
    # df = df.explode(['type', 'Point'])
    # df.to_csv("data.csv", index=False)
    print(DATA)

if __name__ == "__main__":
    main()