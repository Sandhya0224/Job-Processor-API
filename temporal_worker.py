from temporalio.worker import Worker
from temporalio.client import Client
from temporal_app.workflows import JobWorkflow
from temporal_app.activities import generate_dummy_csv

import asyncio

async def main():
    client = await Client.connect("localhost:7233")
    print("✅ Connected to Temporal server")

    worker = Worker(
        client,
        task_queue="job-task-queue",
        workflows=[JobWorkflow],
        activities=[generate_dummy_csv],
    )

    print("✅ Worker is starting...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
