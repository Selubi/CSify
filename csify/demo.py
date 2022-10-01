from pathlib import Path
from csv import QUOTE_NONE
from tqdm import tqdm
import requests
import tarfile
import pandas as pd


def generate_jesc_cs(code_switcher):
    test_data_path = Path('./data/split/test')
    print("Checking if Test data exists...")
    get_data(test_data_path)
    print("Converting Test data to dataframe")
    df = read_data(test_data_path)
    result_dir_path = Path("./data/CSified")
    print("Generating EN-CS input for test data")
    apply_df_in_chunks(df, result_dir_path, "EN-Code-Switched", 'EN-Sentence',
                       code_switcher.en_to_cs)
    print("Generating JA-CS input for test data")
    apply_df_in_chunks(df, result_dir_path, "JA-Code-Switched", 'JA-Sentence',
                       code_switcher.ja_to_cs)


def get_data(data_path):
    data_dir_path = data_path.parents[1]
    data_dir_path.mkdir(parents=True, exist_ok=True)
    if not data_path.exists():
        print("Downloading and Extracting data...")
        url = "https://nlp.stanford.edu/projects/jesc/data/split.tar.gz"
        response = requests.get(url, stream=True)
        file = tarfile.open(fileobj=response.raw, mode="r|gz")
        file.extractall(path=data_dir_path)
    print("OK")


def read_data(data_path):
    return pd.read_csv(data_path, quoting=QUOTE_NONE, delimiter="\t", header=None, names=["EN-Sentence", "JA-Sentence"])


def apply_df_in_chunks(df, dir_path, filename, base_column, func, chunksize=0):
    gen_input_func(df, dir_path, filename, base_column, func)


def gen_input_func(df, dir_path, filename, base_column, func):
    if file_exist(dir_path, filename):
        return
    tqdm.pandas()
    df = df.copy()
    df[filename] = df[base_column].progress_map(func)
    df = df.loc[:, [base_column, filename]]
    make_csv(df, dir_path, filename)
    return df


def make_csv(df, dir_path, filename):
    dir_path.mkdir(parents=True, exist_ok=True)
    path_to_file = dir_path / filename
    print(f"Writing to {path_to_file}")
    df.to_csv(path_or_buf=path_to_file,
              index=False, quoting=QUOTE_NONE, sep='\t')
    print("OK")


def file_exist(dir_path, filename):
    dir_path.mkdir(parents=True, exist_ok=True)
    path_to_file = dir_path / filename
    if path_to_file.exists():
        print(f"{dir_path / filename} already exist")
        return True
    return False
