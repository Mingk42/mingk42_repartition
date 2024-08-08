import pandas as pd

def repartition(dt="20150101"):
    df = pd.read_parquet(f"/home/root2/data/movie_2015/load_dt={dt}")

    df["load_dt"]=dt
    
    df.to_parquet("~/data/movie/repartition/", partition_cols=['load_dt','multiMovieYn', 'repNationCd'])
