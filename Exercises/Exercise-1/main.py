import os, requests, zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
]

def main():
    os.makedirs("downloads") if "downloads" not in os.listdir() else None 
    for url in download_uris:
        f_name = url.split("/")[-1]
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(f"downloads/{f_name}", "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        zip_name = f"downloads/{f_name}"
        with zipfile.ZipFile(zip_name, "r") as z:
            z.extractall("downloads/")
        os.remove(zip_name)

if __name__ == "__main__":
    main()
