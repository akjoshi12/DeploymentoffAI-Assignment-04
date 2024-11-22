import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
from flask import Flask, request, render_template_string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from src.data_analysis import load_data, calculate_total_spending

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSV Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1, h2 {
            text-align: center;
        }
        form {
            text-align: center;
            margin-bottom: 30px;
        }
        .graphs {
            margin: 20px auto;
            width: 80%;
        }
        .graphs img {
            max-width: 100%;
        }
    </style>
</head>
<body>
    <h1>CSV Analysis Tool</h1>
    <form action="/analyze" method="post" enctype="multipart/form-data">
        <label for="file">Choose a CSV file:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Analyze</button>
    </form>
    {% if summary_stats_graph or spending_graph %}
        <div class="graphs">
            <h2>Dataset Summary</h2>
            <div>
                <h3>Summary Statistics (Top Numeric Columns)</h3>
                <img src="data:image/png;base64,{{ summary_stats_graph }}" alt="Summary Statistics Graph">
            </div>
        </div>
        <div class="graphs">
            <h2>Total Spending Distribution</h2>
            <img src="data:image/png;base64,{{ spending_graph }}" alt="Spending Distribution">
        </div>
    {% endif %}
</body>
</html>
"""

def create_summary_stats_graph(data):
    """Generate a heatmap of summary statistics for top numeric columns."""
    numeric_cols = data.select_dtypes(include='number').iloc[:, :5]
    summary_stats = numeric_cols.describe().transpose()
    plt.figure(figsize=(10, 6))
    sns.heatmap(summary_stats, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    plt.title('Summary Statistics for Top Numeric Columns', fontsize=16)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.read()).decode('utf-8')
    plt.close()
    return graph_url

def create_spending_graph(data):
    """Generate a graph of total spending."""
    plt.figure(figsize=(10, 6))
    plt.hist(data['Total_Spending'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Total Spending Distribution', fontsize=16)
    plt.xlabel('Total Spending', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.read()).decode('utf-8')
    plt.close()
    return graph_url

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, summary_stats_graph=None, spending_graph=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Load uploaded file
        file = request.files['file']
        data = load_data(file)
        
        # Perform analysis
        data = calculate_total_spending(data)
        
        # Generate graphs
        summary_stats_graph = create_summary_stats_graph(data)
        spending_graph = create_spending_graph(data)
        
        # Render template with results
        return render_template_string(
            HTML_TEMPLATE,
            summary_stats_graph=summary_stats_graph,
            spending_graph=spending_graph
        )
    except Exception as e:
        return render_template_string("<h1>Error</h1><pre>{{ error }}</pre><a href='/'>Go Back</a>", error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
