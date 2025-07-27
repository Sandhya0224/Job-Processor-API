from temporalio.client import Client
import asyncio
import uuid

from models import SessionLocal, Job, JobStatus
from temporal_app.workflows import JobWorkflow  


async def trigger_temporal_workflow(job_type: str):
    db = SessionLocal()

    job_id = str(uuid.uuid4())
    job = Job(id=job_id, job_type=job_type, status=JobStatus.PENDING)
    db.add(job)
    db.commit()
    db.close()

    client = await Client.connect("localhost:7233")
    await client.start_workflow(
        JobWorkflow,
        args=[job_id, job_type],
        id=job_id,
        task_queue="job-task-queue",
    )

    return job_id
