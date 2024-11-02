import os, requests, zipfile
from concurrent.futures import ThreadPoolExecutor

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
]

def download_extract(url):
    f_name = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(f"downloads/{f_name}", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    zipfile.ZipFile(f"downloads/{f_name}", "r").extractall("data/")
    os.remove(f"downloads/{f_name}")

def main():
    os.makedirs("downloads") if "downloads" not in os.listdir() else None
    with ThreadPoolExecutor(max_workers=len(download_uris)) as exe:
        exe.map(download_extract, download_uris)
        
if __name__ == "__main__":
    main()
