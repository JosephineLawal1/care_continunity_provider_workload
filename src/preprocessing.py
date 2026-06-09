import pandas as pd

def combine_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Combine admission_date and admission_time into a single datetime column.
    """
    df['admission_date'] = pd.to_datetime(df['admission_date'])
    df['admission_time'] = pd.to_timedelta(df['admission_time'] + ':00')
    df['admission_datetime'] = df['admission_date'] + df['admission_time']
    return df

def clean_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure numeric columns are numeric and flags are standardized.
    """
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['wait_time'] = pd.to_numeric(df['wait_time'], errors='coerce')
    df['satisfaction_score'] = pd.to_numeric(df['satisfaction_score'], errors='coerce')
    df['admission_flag'] = df['admission_flag'].astype(str).str.upper()
    return df

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run all preprocessing steps.
    """
    df = combine_datetime(df)
    df = clean_types(df)
    df = df.dropna(subset=['doctor_id', 'patient_id', 'department'])
    return df
