import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_provider_workload(workload_df: pd.DataFrame):
    """
    Bar chart of encounters per provider.
    """
    plt.figure(figsize=(10, 5))
    sns.barplot(data=workload_df, x='doctor_id', y='encounter_count')
    plt.title('Encounters per Provider')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_wait_time_by_department(dept_df: pd.DataFrame):
    """
    Bar chart of average wait time by department.
    """
    plt.figure(figsize=(10, 5))
    sns.barplot(data=dept_df, x='department', y='avg_wait_time')
    plt.title('Average Wait Time by Department')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_continuity_distribution(cont_df: pd.DataFrame):
    """
    Histogram of continuity scores.
    """
    plt.figure(figsize=(8, 4))
    sns.histplot(cont_df['continuity_score'], bins=20, kde=True)
    plt.title('Continuity of Care Score Distribution')
    plt.xlabel('Continuity Score')
    plt.tight_layout()
    plt.show()
