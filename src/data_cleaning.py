import pandas as pd
import os

def clean_data():
    """Load CSVs, clean, and merge bus and disciplinary referral data."""
    
    bus_file = "data/raw/TTU Data - Bus Conduct.csv"
    disc_file = "data/raw/Disciplinary Referral.csv"
    
    # Load CSVs
    dfBus = pd.read_csv(bus_file)
    dfDisc = pd.read_csv(disc_file)

    # Convert 'Date of Incident' to datetime
    dfBus['Date of Incident'] = dfBus['Date of Incident'].astype('datetime64[ns]')
    dfDisc['Date of Incident'] = dfDisc['Date of Incident'].astype('datetime64[ns]')
    
    # Flag if a referral is a bus incident
    dfDisc['bus_disc'] = dfDisc['Student Identifier'].isin(dfBus['Student Identifier'])
    
    # Make sure processed folder exists
    os.makedirs("data/processed", exist_ok=True)
    
    # Save cleaned CSVs
    dfBus.to_csv("data/processed/bus_clean.csv", index=False)
    dfDisc.to_csv("data/processed/referral_clean.csv", index=False)
    
    print("Data cleaned and saved to data/processed/")
    
    return dfBus, dfDisc
