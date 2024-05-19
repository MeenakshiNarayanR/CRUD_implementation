# CRUD operations using ChromaDB vector database
a Python class that provides an interface for CRUD operations on text documents within a vector database and expanded to include methods that generate RESTful web services for each operation, allowing for interactions with the database over HTTP.

## Python Environment
Use Conda environment to isolate your Python libraries.
```bash
conda create -n <your_env name>
conda activate <your_env name>
```

## Python Libraries Installation
```bash
pip install -r requirements.txt
```

## Sample text document
A sample text document known as sample_text.txt is attached to demonstrate the CRUD operations.


## Python class implementation of vector_database.py
Python class to implement vector database using ChromaDB. This class implemented enables the following operations:
• Collection Creation: A method that creates a new collection or index within the vector database to store vectorized text documents.
• Document Insertion: A method that receives a plain text input, vectorizes it, and adds it as a new entry in the collection.
• Document Update: A method that updates or replaces an existing text entry in the database with new text provided as an argument.
• Document Deletion: A method that deletes a text entry from the database based on a specified identifier.
• Document Retrieval: A method that receives a plain text input and a number N. Returns the top N documents from the database that are ordered in relevancy to the text.

### to run the example CRUD operations implementation in the vector database class
```bash
python vector_database.py
```
### to run your examples to check the vector database class implementation
```python
if __name__ == "__main__":
    db = VectorDatabaseClient("your_chromadb_uri")
    db.create_collection("<collection_name>")
    db.insert_doc("<collection_name>", "<text in str>")
    db.update_doc("<collection_name", "<document_id>", "<update text>")
    documents_1 = db.retrieve_docs("<collection_name", "<query_name>", <top_n number>)
    print(documents_1)
    db.delete_doc("<collection_name>", "<document_id>")
    documents_2 = db.retrieve_docs("<collection_name", "<query_name>", <top_n number>)
    print(documents_2)
```

## to run FastAPI server
aap.py extends the vector database class implementation to allow the database to interact with web services

### option 1 - 
```bash
uvicorn main:app --reload
```

### option 2 - 
```bash
python app.py
```

## Testing REST API service for the CRUD operations
testing can be done using curl tool

### 1. Creation of collection
```bash
curl -X POST "http://localhost:8000/create_collection/<YourCollectionName>"
```

### 2. Document Insertion
```bash
curl -X POST "http://localhost:8000/insert_document/<YourCollectionName>" -H "Content-Type: application/json" -d '{"text": "<enter your text here>"}'
```

### 3. Document Update
```bash
curl -X PUT "http://localhost:8000/update_document/<YourCollectionName>" -H "Content-Type: application/json" -d '{"document_id": "<YourDocumentID>", "new_text": "<enter New text here>"}'
```

### 4. Document Deletion
```bash
curl -X DELETE "http://localhost:8000/delete_document/<YourCollectionName>/<YourDocumentID>"
```

### 4. Documents Retrieval
```bash
curl -X POST "http://localhost:8000/retrieve_documents/<YourCollectionName>" -H "Content-Type: application/json" -d '{"text": "<Your query text>", "top_n": <top_n number>}'
```

## Testing
test the vector database implementation using pytest. Add assertions to check the CRUD operation as required.

```bash
python unit_test_vector_database.py
```




