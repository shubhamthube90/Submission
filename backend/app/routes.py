from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, FileResponse
from .database import SessionLocal
from .models import Document
from .tasks import process_document
import redis, json, csv

router = APIRouter()
r = redis.Redis(host='localhost', port=6379, db=0)

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    db = SessionLocal()
    doc = Document(filename=file.filename, status="queued")
    db.add(doc)
    db.commit()
    db.refresh(doc)
    process_document.delay(doc.id)
    return {"id": doc.id, "status": doc.status}

@router.get("/documents")
def get_documents():
    db = SessionLocal()
    return db.query(Document).all()

@router.get("/progress")
def progress_stream():
    pubsub = r.pubsub()
    pubsub.subscribe("progress")
    def event_stream():
        for message in pubsub.listen():
            if message["type"] == "message":
                yield f"data: {message['data'].decode()}\n\n"
    return StreamingResponse(event_stream(), media_type="text/event-stream")
