import asyncio
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status
from models import SessionLocal, Job, JobStatus
from services.job_service import trigger_temporal_workflow

router = APIRouter()

@router.post("/jobs/")
async def create_job(job_type: str):
    job_id = await trigger_temporal_workflow(job_type)
    return {"job_id": job_id}


@router.get("/jobs/{job_id}")
def get_job(job_id: str):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()
    db.close()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return {"job_id": job.id, "status": job.status, "result": job.result_path}
