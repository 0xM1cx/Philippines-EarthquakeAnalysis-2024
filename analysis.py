import pandas as pd
import os

def get_DF(file) -> pd.DataFrame:
    df = pd.read_csv(os.path.join("./philvocs-data/", file))
    return df


if __name__ == "__main__":
    #files = os.listdir("./philvocs-data")
    file = "1234567_merged.csv"
    tanan_dataframes = []
    #for file in files:
    df = get_DF(file)
    #tanan_dataframes.append(df)

    #combined_DF = pd.concat(tanan_dataframes, ignore_index=True)
    df.columns = ["Date_Time", "Latitude_N", "Longitude_E", "Depth(KM)", "Magnitude", "Location"]
    print(df.to_string())
