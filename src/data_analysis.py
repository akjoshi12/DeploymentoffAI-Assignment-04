
import pandas as pd

def load_data(filepath):
    """Load and preprocess the dataset."""
    data = pd.read_csv(filepath)
    return data

def summarize_data(data):
    """Provide a summary of the dataset."""
    return {
        "shape": data.shape,
        "columns": list(data.columns),
        "null_values": data.isnull().sum().to_dict(),
        "basic_stats": data.describe().to_dict()
    }

def calculate_total_spending(data):
    """Calculate total spending for each customer."""
    data['Total_Spending'] = (
        data['MntWines'] + data['MntFruits'] + data['MntMeatProducts'] +
        data['MntFishProducts'] + data['MntSweetProducts'] + data['MntGoldProds']
    )
    return data[['Total_Spending']]
