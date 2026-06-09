import pandas as pd

def provider_workload(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute workload metrics per doctor_id.
    """
    grouped = df.groupby('doctor_id').agg(
        encounter_count=('patient_id', 'count'),
        avg_wait_time=('wait_time', 'mean'),
        avg_satisfaction=('satisfaction_score', 'mean'),
        admission_rate=('admission_flag', lambda x: (x == 'Y').mean())
    ).reset_index()
    return grouped

def department_workload(df: pd.DataFrame) -> pd.DataFrame:
    """
    Workload metrics per department.
    """
    grouped = df.groupby('department').agg(
        encounter_count=('patient_id', 'count'),
        avg_wait_time=('wait_time', 'mean'),
        avg_satisfaction=('satisfaction_score', 'mean'),
        admission_rate=('admission_flag', lambda x: (x == 'Y').mean())
    ).reset_index()
    return grouped
