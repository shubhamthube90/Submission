import time, json, redis
from .celery_app import celery
from .database import SessionLocal
from .models import Document

r = redis.Redis(host='localhost', port=6379, db=0)

def publish(event, doc_id):
    r.publish("progress", json.dumps({"doc_id": doc_id, "event": event}))

@celery.task
def process_document(doc_id):
    db = SessionLocal()
    doc = db.query(Document).get(doc_id)
    doc.status = "processing"
    db.commit()
    publish("job_started", doc_id)
    time.sleep(2)
    doc.status = "completed"
    doc.result = "done"
    db.commit()
    publish("job_completed", doc_id)
    db.close()
