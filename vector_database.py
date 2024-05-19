import chromadb
from sentence_transformers import SentenceTransformer
import time


class VectorDatabaseClient:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        try:
            self.client = chromadb.Client()
            self.model = SentenceTransformer(model_name)
        except Exception as e:
            print(f"Error initializing VectorDatabaseClient: {e}")
            raise

    def create_collection(self, collection_name: str):
        try:
            self.client.create_collection(name=collection_name)
            print(f"Collection '{collection_name}' created successfully.")
        except Exception as e:
            print(f"Error creating collection: {e}")
            raise

    def insert_doc(self, collection_name: str, text: str):
        try:
            if not isinstance(text, str):
                raise ValueError("Input text must be a string.")

            print(f"Type of text: {type(text)}")  # Debugging statement
            print(f"Text: {text}")  # Debugging statement

            vector = self.model.encode(text).tolist()

            collection = self.client.get_collection(name=collection_name)
            document_id = f"doc_{int(time.time())}"

            collection.add(
                ids=[document_id],
                documents=[text],
                embeddings=[vector]
            )

            print(f"Document inserted into collection '{collection_name}' with ID '{document_id}'.")
        except Exception as e:
            print(f"Error inserting document: {e}")
            raise

    def update_doc(self, collection_name: str, document_id: str, new_text: str):
        try:
            if not isinstance(new_text, str):
                raise ValueError("Input text must be a string.")

            vector = self.model.encode(new_text).tolist()
            collection = self.client.get_collection(name=collection_name)
            collection.update(
                ids=[document_id],
                documents=[new_text],
                embeddings=[vector]
            )
            print(f"Document '{document_id}' updated in collection '{collection_name}'.")
        except Exception as e:
            print(f"Error updating document: {e}")
            raise

    def delete_doc(self, collection_name: str, document_id: str):
        try:
            collection = self.client.get_collection(name=collection_name)
            collection.delete(ids=[document_id])
            print(f"Document '{document_id}' deleted from collection '{collection_name}'.")
        except Exception as e:
            print(f"Error deleting document: {e}")
            raise

    def retrieve_docs(self, collection_name: str, query_text: str, top_n: int):
        try:
            if not isinstance(query_text, str):
                raise ValueError("Query text must be a string.")

            vector = self.model.encode(query_text).tolist()
            collection = self.client.get_collection(name=collection_name)

            results = collection.query(
                query_texts=[query_text],  # query_texts expects a list of strings
                n_results=top_n
            )

            print(f"Results: {results}")  # Debugging statement to inspect results

            print(f"Documents retrieved from collection '{collection_name}' for query '{query_text}'.")

            # Extract documents from the nested structure
            documents = results.get('documents', [])
            flat_documents = [doc for sublist in documents for doc in sublist]  # Flatten the list of lists

            return flat_documents
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            raise


if __name__ == "__main__":
    db = VectorDatabaseClient("all-MiniLM-L6-v2")
    db.create_collection("my_collection1")
    db.insert_doc("my_collection1", "Sample document for testing CRUD operations")
    documents = db.retrieve_docs("my_collection1", "sample1", 1)
    print(documents)
