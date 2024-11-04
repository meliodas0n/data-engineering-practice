import glob, pandas as pd

def main():
    jfiles = glob.glob("data/**/*.json", recursive=True)
    for i, jf in enumerate(jfiles):
        if i == 0: df = pd.read_json(jf)
        else: df = pd.concat([df, pd.read_json(jf)])
    df = df.explode("geolocation")
    df.to_csv("data.csv", index=False)

if __name__ == "__main__":
    main()