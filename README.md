# 🛠️ Job Processor API with FastAPI and Temporal

This project implements a background job processing system using **FastAPI**, **Temporal.io**, **SQLite**, and **Pandas**.

Jobs are submitted via REST API and processed asynchronously using Temporal. The result of each job is saved as a `.csv` file locally.

---

## 🚀 Features

- Submit background jobs via `POST /jobs/`
- Track job status and results via `GET /jobs/{job_id}`
- Jobs are processed using **Temporal workflows**
- Results saved as `.csv` in the `output/` directory
- Data stored in a **SQLite** database

---

## 📁 Project Structure

job_processor_project/
├── main.py # FastAPI entrypoint
├── routers/
│ └── jobs.py # API endpoints
├── services/
│ └── job_service.py # Business logic and DB integration
├── models.py # SQLite schema + session
├── temporal_app/
│ ├── workflows.py # Temporal workflow definitions
│ └── activities.py # Activities for CSV generation
├── temporal_worker.py # Temporal worker runner
├── output/ # Output directory for .csv files
├── jobs.db # SQLite DB file (auto-generated)
├── .gitignore
└── requirements.txt


---

## ⚙️ Requirements

- Python 3.10+
- Docker (for running the Temporal server)

---

## 🧑‍💻 Clone and Run the Project

### Clone the repository
git clone https://github.com/Sandhya0224/Job-Processor-API.git
cd job-processor-fastapi-temporal

---

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

---

### Install Temporal CLI (Go version)
### Download and install the Temporal CLI from the official release:

### Go to: https://learn.temporal.io/getting_started/python/dev_environment/

### Download the latest .zip for Windows (e.g., temporal-cli_windows_amd64.zip)

### Extract it and move the temporal.exe to a folder like C:\temporal-cli\

### Add the temporal.exe folder to your System PATH:

### Search “Environment Variables” → Edit the PATH variable → Add C:\temporal-cli\

### Verify installation:
temporal --version

temporal server start-dev
### This will start a local Temporal development server accessible at localhost:7233.
### Run Temporal Worker In one terminal:

---

python temporal_worker.py
### This will start the Temporal worker to handle workflows and activities.

---

### Run FastAPI App
uvicorn main:app --reload
### FastAPI will start at: http://localhost:8000

---

### API Usage
### POST /jobs/
### Submit a new job:

### POST /jobs/
{
  "job_type": "generate_csv",
  "payload": {}
}

---

### GET /jobs/{job_id}
### Fetch the job status and result:

### GET /jobs/abc-123

{
  "job_id": "abc-123",
  "status": "COMPLETED",
  "result": "./output/abc-123.csv"
}
