import os
from os import path
import gdown

def download_data():
    """Download CSVs from Google Drive if not present in data/raw."""
    files = {
        "TTU Data - Bus Conduct.csv": "13xLuMoCk3lqFCSnhX5a7NUjTk_9gJkz_",
        "AnotherFile.csv": "1GdMkumBPN4bWEZYb3RILIVNB4iICfIdp",
        "Disciplinary Referral.csv": "1wm74X1pobUXX-Ui_5aF-i5p9cXgNcqyF"
    }

    for filename, file_id in files.items():
        filepath = f"data/raw/{filename}"
        if not path.isfile(filepath):
            print(f"Downloading {filename}...")
            gdown.download(id=file_id, output=filepath, quiet=False)
        else:
            print(f"{filename} already exists.")
