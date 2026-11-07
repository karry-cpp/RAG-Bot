from pathlib import Path
import pymupdf

class Chunking:
    def __init__(self) -> None:
        pass

    def create_chunks(self, fileOrText: str | Path, chunk_size: int, overlap: int):
        text = ''
        result: list[str] = []
        if Path(fileOrText).is_file():
            if str(fileOrText).endswith('pdf'):
                with pymupdf.open(fileOrText) as doc:
                    text = " ".join(str(page.get_text()) for page in doc)
            else:
                text = Path(fileOrText).read_text()
        else:
            text = str(fileOrText)
        
        text = text.split(' ')
        step = chunk_size - overlap

        for i in range(0, len(text), step):
            result.append(" ".join(text[i:i+chunk_size]))

            if i + chunk_size > len(text):
                break

        return result

if __name__ == '__main__':
    x = Chunking()
    print(x.create_chunks("I am Kunal. I am a kind guy. I am attractive. I am nice. I am lovely", 4, 1))
