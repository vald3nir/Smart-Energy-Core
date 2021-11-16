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


def reduce_and_sum(file_csv, column_index, offset='60Min'):
    df = _load_dataframe(file_csv)
    df[column_index] = pd.to_datetime(df[column_index])
    data_json = df.groupby(pd.Grouper(key=column_index, freq=offset)).sum().reset_index().to_json()
    return json.loads(data_json)


def csv_to_json(file_csv):
    df = _load_dataframe(file_csv)
    frame = df.iloc[:]
    return _dataframe_to_json(frame)


def read_last_row(file_csv, n_rows=5):
    df = _load_dataframe(file_csv)
    frame = df.iloc[-n_rows:]
    return _dataframe_to_json(frame)


def create_file_csv(file_path, fields):
    df = pd.DataFrame(fields)
    df.to_csv(file_path, index=False)


def append_file_csv(file_path, fields):
    with open(file_path, 'a') as f:
        csv.writer(f).writerow(fields)
