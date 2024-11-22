# Data Analytics Application with CI/CD Pipeline  
This repository contains a Python-based data analytics application developed as part of **Assignment #4: Python-Based Data Analytics Application Deployment Assignment**. The project implements a complete CI/CD pipeline using tools such as Docker, Minikube, Jenkins, and more.  

## **Objective**  
The primary goal is to build, test, deploy, and monitor a Python application in a fully automated CI/CD pipeline environment.  

## **Features**  
- Data analytics using Python (Pandas, NumPy, Matplotlib).  
- Web-based application interface (Flask).  
- Fully containerized application using Docker.  
- Deployment on Kubernetes cluster with Minikube.  
- Automated CI/CD pipeline using Jenkins.  
- Server configuration automation with Ansible/Chef.  
- Application monitoring with AWS CloudWatch.  

---

## **Technologies Used**  
1. **Version Control**: GitHub  
2. **Containerization**: Docker  
3. **Orchestration**: Minikube (Kubernetes)  
4. **CI/CD**: Jenkins  
5. **Build Tool**: Maven (optional)  
6. **Testing Tools**: Pytest, Selenium (optional for web interface)  
7. **Configuration Management**: Ansible or Chef  
8. **Monitoring**: AWS CloudWatch  
9. **Operating System**: Ubuntu  

---

## **Project Structure**  
```
├── data                 # Directory for sample datasets
│   └── sample.csv       # Example dataset for analytics
├── src                  # Source code directory
│   ├── app.py           # Flask application entry point
│   ├── analysis.py      # Data analysis logic
│   └── utils.py         # Utility functions
├── tests                # Unit test cases
│   └── test_analysis.py # Example test for analysis
├── k8s                  # Kubernetes deployment manifests
│   ├── deployment.yaml  # Deployment configuration
│   └── service.yaml     # Service configuration
├── requirements.txt     # Application dependencies
├── Dockerfile           # Docker build configuration
├── Jenkinsfile          # CI/CD pipeline configuration
└── README.md            # Project documentation
```  

---

## **Setup Instructions**  

### **Step 1: Clone Repository**  
```bash
git clone https://github.com/<your-username>/data-analytics-app.git
cd data-analytics-app
```

### **Step 2: Set Up Virtual Environment**  
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **Step 3: Run the Application**  
```bash
python src/app.py
```
Access the application at: `http://localhost:5000`

---

## **Dockerizing the Application**  
### **Step 1: Build Docker Image**  
```bash
docker build -t data-analytics-app .
```

### **Step 2: Run Docker Container**  
```bash
docker run -p 5000:5000 data-analytics-app
```

---

## **CI/CD Pipeline**  

### **Jenkins Pipeline Configuration**  
A `Jenkinsfile` has been created to automate the following:  
1. Build the application and install dependencies.  
2. Run unit tests using Pytest.  
3. Build a Docker image.  
4. Deploy to Minikube Kubernetes cluster.  

---

## **Testing**  

### **Unit Testing**  
Run tests using Pytest:  
```bash
pytest tests/
```

### **Optional: Web Interface Testing with Selenium**  
Automated browser tests can be implemented to validate the web interface functionality.

---

## **Deployment on Minikube**  
### **Step 1: Start Minikube Cluster**  
```bash
minikube start
```

### **Step 2: Deploy to Kubernetes**  
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### **Step 3: Access the Application**  
Use Minikube's service URL:  
```bash
minikube service myapp-service
```

---

## **Monitoring with AWS CloudWatch (Bonus)**  
- Set up AWS CloudWatch to monitor application performance and resource utilization.
- Create custom dashboards for visualizing metrics like CPU usage, memory consumption, and logs.

---

## **Dataset Details**  

### **Dataset Name**: `ifood_df.csv`  

#### **Description**:  
This dataset consists of 2206 customer records from XYZ Company, including:  
- **Customer Profiles**: Demographics, income, etc.  
- **Product Preferences**: Data on customer interests.  
- **Campaign Success/Failures**: Results of marketing campaigns.  
- **Channel Performance**: Effectiveness of marketing channels.

#### **Potential Use Cases**:  
1. Exploratory Data Analysis (EDA).  
2. Statistical Analysis.  
3. Data Visualizations.

---

## **Deliverables**  
1. **GitHub Repository**:  
   Public repository containing:  
   - Source code.  
   - Dockerfile, Jenkinsfile.  
   - Kubernetes manifests.  
   - Ansible/Chef scripts.  

2. **Documentation**:  
   Detailed README with setup, testing, and deployment instructions.  

3. **Presentation/Report**:  
   Summary of the project, challenges, and key learnings.  

---

## **Evaluation Criteria**  
- **Code Quality**: Clean and modular code.  
- **Pipeline Implementation**: End-to-end functionality of the CI/CD pipeline.  
- **Documentation**: Clarity and completeness.  
- **Presentation**: Articulation of project insights.  

---  
