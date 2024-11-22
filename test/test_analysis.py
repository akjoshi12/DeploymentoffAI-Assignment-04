import pytest
import sys
import os
from flask import Flask
import pandas as pd
import io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.app import app  # Corrected import
from src.data_analysis import load_data, calculate_total_spending  # Corrected import

@pytest.fixture
def client():
    """Flask test client fixture."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"CSV Analysis Tool" in response.data

def test_analyze_route_no_file(client):
    """Test the analyze route with no file uploaded."""
    response = client.post('/analyze')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_analyze_route_with_file(client):
    """Test the analyze route with a valid file."""
    # Create a sample CSV
    sample_data = """MntWines,MntFruits,MntMeatProducts,MntFishProducts,MntSweetProducts,MntGoldProds
    100,20,300,50,10,30
    200,30,400,60,20,40
    """
    data = io.BytesIO(sample_data.encode('utf-8'))
    data.name = 'test.csv'
    
    response = client.post('/analyze', data={'file': data}, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b"Dataset Summary" in response.data
    assert b"Total Spending Distribution" in response.data

def test_load_data():
    """Test the load_data function."""
    sample_data = """MntWines,MntFruits,MntMeatProducts,MntFishProducts,MntSweetProducts,MntGoldProds
    100,20,300,50,10,30
    200,30,400,60,20,40
    """
    data = io.StringIO(sample_data)
    df = load_data(data)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 6)

def test_calculate_total_spending():
    """Test the calculate_total_spending function."""
    df = pd.DataFrame({
        "MntWines": [100, 200],
        "MntFruits": [20, 30],
        "MntMeatProducts": [300, 400],
        "MntFishProducts": [50, 60],
        "MntSweetProducts": [10, 20],
        "MntGoldProds": [30, 40]
    })
    result = calculate_total_spending(df)
    assert "Total_Spending" in result.columns
    assert result["Total_Spending"].tolist() == [510, 750]
