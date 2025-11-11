from src.data_download import download_data
from src.data_cleaning import clean_data

if __name__ == "__main__":
    download_data()
    dfBus, dfDisc = clean_data()

