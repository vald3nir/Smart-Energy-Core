import csv
import json

import pandas as pd


def _dataframe_to_json(frame):
    json_str = frame.to_json(orient='records')
    return json.loads(json_str)


def _load_dataframe(file_csv):
    return pd.read_csv(file_csv, error_bad_lines=False)


def list_column_values(file_csv, column):
    df = _load_dataframe(file_csv)
    return df[column].tolist()


def sum_columns(file_csv, column):
    df = _load_dataframe(file_csv)
    return df[column].sum()


def csv_to_json(file_csv):
    df = _load_dataframe(file_csv)
    frame = df.iloc[:]
    return _dataframe_to_json(frame)


def read_last_row(file_csv, n_rows=5):
    df = _load_dataframe(file_csv)
    frame = df.iloc[-n_rows:]
    return _dataframe_to_json(frame)


def append_file_csv(file_path, fields):
    with open(file_path, 'a') as f:
        csv.writer(f).writerow(fields)
