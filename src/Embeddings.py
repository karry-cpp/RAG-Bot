import chromadb
import pathlib 

class Embeddings:
    def __init__(self, pth: str | pathlib.Path ) -> None:
        self.__client = chromadb.PersistentClient(pth)
        pass

    def load_collection(self, coll_name: str) -> bool:
        try:
            collection = self.__client.get_collection(coll_name)
        except Exception:
            return False

        if collection.count() == 0:
            return False

        self.__collection = collection
        return True

    def create_embeddings(self, coll_name: str, chunks: list[str]):
        self.__collection = self.__client.get_or_create_collection(
            coll_name
        )
        self.__collection.upsert(
            ids=[f'chunk_{x}' for x in range(0, len(chunks))],
            documents=chunks
        )

    def get_embeddings(self):
        return self.__collection

    def get_answer(self, query: str, top_k: int = 1, get_distances: bool = False):
        result = self.__collection.query(
            n_results=top_k,
            query_texts=[query]
        )

        if get_distances:
            return result['documents'], result['distances']

        return result['documents']