import streamlit as st
import pydeck as pdk
import pandas as pd
import data

def app(names): 
    with st.spinner("Preparing map..."):
        print()

        st.map(df)

        us_data = data.get_data()

        lats = us_data['decimalLatitude']
        longs = us_data['decimalLongitude']
        mask = longs.isna() | lats.isna()
        mask = mask | us_data['scientificName'].isna()
        for name in names:
            mask = mask | ~(us_data['scientificName'] == name)

        df = pd.DataFrame()
        df['lat'] = lats
        df['lon'] = longs

        df = df[~mask]
        st.map(df)

    #TODO Filter out non-US (maybe)

with st.spinner("Preparing data..."):
    us_data = pd.read_parquet('final_data.parquet')

    st.write(us_data.keys())

    for key in us_data.keys():
        if key == 'verbatimScientificName':
            st.write(us_data[key])
        
    lats = us_data['decimalLatitude']
    longs = us_data['decimalLongitude']
    mask = longs.isna() | lats.isna()


if __name__ == "__main__":
    app(names=[])
