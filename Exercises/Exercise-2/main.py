import os, re, requests, pandas as pd
from concurrent.futures import ThreadPoolExecutor

URL = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021"

def download(fname):
    url = f"{URL}/{fname}"
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(f"downloads/{fname}", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"{url = } downloaded")

def get_files():
    df = pd.read_html(URL)[0]
    df = df[df['Last modified'] == '2024-01-19 10:27']
    os.makedirs("downloads") if "downloads" not in os.listdir() else None
    with ThreadPoolExecutor(max_workers=100) as tpe:
        tpe.map(download, list(df['Name'].unique()))

def main():
    get_files()
    for i, f in enumerate(os.listdir("downloads")):
        if i == 0: df = pd.read_csv(f"downloads/{f}", low_memory=False)
        else: df = pd.concat([df, pd.read_csv(f"downloads/{f}", low_memory=False)], ignore_index=True)
    df = pd.read_csv("data.csv", low_memory=False)
    df['HourlyDryBulbTemperature'] = df['HourlyDryBulbTemperature'].apply(lambda x : re.sub(r'[a-zA-Z]', '', str(x))).replace('', '0').fillna(0).replace('*', 0)
    print(f"Max HourlyDryBulbTemperature = {max(list(df['HourlyDryBulbTemperature'].astype(float)))}")

if __name__ == "__main__":
    main()