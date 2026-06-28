import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path, sep=";")


def clean_data(df):
    df = df.copy()

    df.columns = df.columns.str.strip()

    text_columns = df.select_dtypes(include="object").columns
    for column in text_columns:
        df[column] = df[column].str.strip()

    df["converted"] = df["y"].map({
        "yes": 1,
        "no": 0
    })

    return df


def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)