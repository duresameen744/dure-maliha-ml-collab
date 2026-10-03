"""Reusable data-cleaning functions for the Adult Income dataset."""


def clean_adult_data(df):
    """Drop duplicate rows and rows with missing values.

    Args:
        df: a pandas DataFrame loaded from the raw Adult Income CSV.

    Returns:
        A new DataFrame with duplicates and missing-value rows removed.
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df
