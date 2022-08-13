import os
import pandas as pd
import glob

def main():
    """
    Concatenates separated seasons data into one file
    """
    files = os.path.join("data", "s*-*.csv")
    files = glob.glob(files)
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    print(f"Total obserwations: {len(df)}")
    
    df.to_csv("data/all_seasons.csv", index=False)
    

if __name__ == '__main__':
    main()