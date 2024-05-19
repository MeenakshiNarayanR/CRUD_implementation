from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vector_database import VectorDatabaseClient

app = FastAPI()
db_client = VectorDatabaseClient()

class Document(BaseModel):
    text: str

class UpdateDocument(BaseModel):
    document_id: str
    new_text: str

class Query(BaseModel):
    text: str
    top_n: int

@app.post("/create_collection/{collection_name}")
def create_collection(collection_name: str):
    try:
        db_client.create_collection(collection_name)
        return {"message": "Collection created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating collection: {e}")

@app.post("/insert_document/{collection_name}")
def insert_doc(collection_name: str, document: Document):
    try:
        db_client.insert_doc(collection_name, document.text)
        return {"message": "Document inserted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting document: {e}")

@app.put("/update_document/{collection_name}")
def update_doc(collection_name: str, update: UpdateDocument):
    try:
        db_client.update_doc(collection_name, update.document_id, update.new_text)
        return {"message": "Document updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating document: {e}")

@app.delete("/delete_document/{collection_name}/{document_id}")
def delete_doc(collection_name: str, document_id: str):
    try:
        db_client.delete_doc(collection_name, document_id)
        return {"message": "Document deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting document: {e}")

@app.post("/retrieve_documents/{collection_name}")
def retrieve_docs(collection_name: str, query: Query):
    try:
        results = db_client.retrieve_docs(collection_name, query.text, query.top_n)
        return {"documents": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving documents: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
