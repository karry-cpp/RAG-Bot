from pathlib import Path

from FileIO import FileIO
from Embeddings import Embeddings

if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent
    f = FileIO(root / 'all files')
    files = f.get_files_ext(r'.txt')

    for ind, fname in enumerate(files):
        if ind > 2:
            break
        print(fname)
        coll_name = Path(fname).stem.strip().replace(' ', '')
        print(coll_name)

        emb = Embeddings(root / 'chroma_test')
        if emb.load_collection(coll_name):
            print('Using stored embeddings.')
        else:
            from Chunking import Chunking

            print('No stored embeddings found. Indexing document...')
            chunk_list = Chunking().create_chunks(fname, 100, 20)
            emb.create_embeddings(coll_name, chunk_list)
    while True:
        que = input('Ask Question: ')
        res = emb.get_answer(que, 3, True)
        print(res)
    