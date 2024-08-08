import pandas as pd

def transform():
    df = pd.read_parquet("/home/root2/data/movie_2015")
    df.to_parquet("~/data/movie/repartition/", partition_cols=['load_dt','multiMovieYn', 'repNationCd'])
