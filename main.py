from fastapi import FastAPI, UploadFile, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

class VideoRequest(BaseModel):
    script: str
    aspect_ratio: str  # "16:9" or "9:16"

@app.post("/generate-video")
async def generate(request: VideoRequest, background_tasks: BackgroundTasks):
    # Background task for heavy rendering
    background_tasks.add_task(process_video_pipeline, request)
    return {"status": "Processing started", "task_id": "unique_id_123"}
