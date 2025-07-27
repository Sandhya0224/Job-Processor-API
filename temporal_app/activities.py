from temporalio import activity
from models import SessionLocal, Job, JobStatus
import pandas as pd
import os
from uuid import uuid4
import random

@activity.defn
async def generate_dummy_csv(job_id: str, job_type: str):  # Adjust if you only need job_id
    db = SessionLocal()

    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        db.close()
        raise Exception(f"Job with ID {job_id} not found in the database")

    job.status = JobStatus.IN_PROGRESS
    db.commit()

    # Dummy data generation
    df = pd.DataFrame({
        "Name": [f"Name_{i}" for i in range(1000)],
        "Value": [i for i in range(1000)],
    })

    os.makedirs("output", exist_ok=True)
    output_path = f"output/{job_id}.csv"
    df.to_csv(output_path, index=False)

    job.status = JobStatus.COMPLETED
    job.result_path = output_path
    db.commit()
    db.close()

    return output_path
