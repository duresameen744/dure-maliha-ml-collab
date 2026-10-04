import pandas as pd

from src.data_cleaning import clean_adult_data


def test_clean_adult_data_removes_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"]})
    result = clean_adult_data(df)
    assert len(result) == 2


def test_clean_adult_data_removes_missing_values():
    df = pd.DataFrame({"a": [1, None, 3], "b": ["x", "y", "z"]})
    result = clean_adult_data(df)
    assert len(result) == 2
    assert result["a"].isnull().sum() == 0


def test_clean_adult_data_keeps_clean_rows_unchanged():
    df = pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"]})
    result = clean_adult_data(df)
    assert len(result) == 3
