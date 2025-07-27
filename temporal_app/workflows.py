from temporalio import workflow
from temporal_app.activities import generate_dummy_csv
from datetime import timedelta

    
@workflow.defn
class JobWorkflow:
    @workflow.run
    async def run(self, job_id: str, job_type: str):
        await workflow.execute_activity(
            generate_dummy_csv,
            args=[job_id, job_type],  
            schedule_to_close_timeout=timedelta(seconds=10), 
        )

