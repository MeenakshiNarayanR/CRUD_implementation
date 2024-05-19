import pytest
from vector_database import VectorDatabaseClient

@pytest.fixture
def db():
    return VectorDatabaseClient("all-MiniLM-L6-v2")

def test_create_collection(db):
    db.create_collection("test_collection")
    #print("test collection created")


def test_insert_doc(db):
    db.insert_doc("test_collection", "doc1", "This is a sample document.")
    #print("test document inserted")

def test_update_doc(db):
    db.update_doc("test_collection", "doc1", "This is an updated document.")
    #print("test document updated")

def test_delete_doc(db):
    db.delete_doc("test_collection", "doc1")
    #print("test document deleted")

def test_retrieve_docs(db):
    db.insert_doc("test_collection", "doc2", "Another sample document.")
    results = db.retrieve_docs("test_collection", "sample", 1)
    assert len(results) > 0
    #print(f"test results = {results}")
