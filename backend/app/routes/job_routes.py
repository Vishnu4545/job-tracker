from fastapi import APIRouter, HTTPException
from app.models.jobs import Job

router = APIRouter()

fake_jobs_db = []

@router.get("/jobs")
def get_jobs():
    return fake_jobs_db

@router.get("/jobs/{job_id}")
def get_job(job_id: int):
    for job in fake_jobs_db:
        if job['id'] == job_id:
            return job
    raise HTTPException(status_code=404, detail="Job not found")

@router.post("/jobs")
def add_job(job: Job):
    job.id = len(fake_jobs_db) + 1
    fake_jobs_db.append(job.dict())
    return job

@router.put("/jobs/{job_id}")
def update_job(job_id: int, updated_job: Job):
    for index, job in enumerate(fake_jobs_db):
        if job['id'] == job_id:
            fake_jobs_db[index] = updated_job.dict()
            fake_jobs_db[index]['id'] = job_id
            return fake_jobs_db[index]
    raise HTTPException(status_code=404, detail="Job not found")

@router.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    for index, job in enumerate(fake_jobs_db):
        if job['id'] == job_id:
            del fake_jobs_db[index]
            return {"message": "Job deleted"}
    raise HTTPException(status_code=404, detail="Job not found")
