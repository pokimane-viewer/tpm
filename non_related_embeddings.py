Below is a **drop-in Python script** that will

1. read any plain-text document,
2. split it into 1 000-character chunks,
3. embed each chunk (using the open-source `sentence-transformers` model `all-mpnet-base-v2`, 768-dim), and
4. save every embedding as its own `.npy` file in a *new* folder on your Desktop (it creates the folder if it doesn’t already exist).

```bash
# one-time setup
pip install -U sentence-transformers numpy
```

```python
# embed_doc.py  ── run:  python embed_doc.py mydoc.txt  (or .md/.pdf converted to text)

import sys, os, json
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNK_SIZE = 1000                      # characters
MODEL_NAME = "all-mpnet-base-v2"       # 768-dim
OUT_DIRNAME = "mydoc_embeddings"       # folder on Desktop

def load_text(filepath: Path) -> str:
    """Very simple loader; assumes UTF-8 text file."""
    return filepath.read_text(encoding="utf-8")

def chunkify(text: str, size: int = CHUNK_SIZE):
    """Yield non-overlapping chunks of ≤ size chars."""
    for i in range(0, len(text), size):
        yield i // size, text[i : i + size]

def main():
    if len(sys.argv) < 2:
        print("Usage: python embed_doc.py <path/to/document.txt>")
        sys.exit(1)

    src_file = Path(sys.argv[1]).expanduser().resolve()
    if not src_file.exists():
        raise FileNotFoundError(src_file)

    # 1. load & split
    text = load_text(src_file)
    chunks = list(chunkify(text))

    # 2. prepare output folder on Desktop
    desktop = Path.home() / "Desktop"
    out_dir = desktop / OUT_DIRNAME
    out_dir.mkdir(parents=True, exist_ok=True)   # no error if it exists

    # 3. embed
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode([c[1] for c in chunks], batch_size=16,
                              convert_to_numpy=True, normalize_embeddings=True)

    # 4. persist each vector
    meta = []    # we’ll also keep a tiny index file
    for (idx, _), vec in zip(chunks, embeddings):
        fname = f"chunk_{idx:03d}.npy"
        np.save(out_dir / fname, vec)
        meta.append({"chunk_idx": idx, "file": fname})

    # write an index.json so you know what’s what
    with open(out_dir / "index.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    print(f"✅  {len(embeddings)} chunks embedded and saved to {out_dir}")

if __name__ == "__main__":
    main()
```

#### How it works

| Step                | Code line(s)                      | Detail                                                                                                |
| ------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Chunking**        | `chunkify()`                      | Simple slice every 1 000 characters. No overlap; tweak logic for sliding windows if you need context. |
| **Embedding model** | `SentenceTransformer(MODEL_NAME)` | Loads weights locally (≈420 MB the first time). Returns a 768-dim NumPy vector for each chunk.        |
| **Vector storage**  | `numpy.save()`                    | Saves each vector as its own binary `.npy` file for fast re-load. `index.json` maps chunk → file.     |

#### Switching to OpenAI / Gemini / Claude embeddings

Replace the model section:

```python
import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")
embeddings = []
for _, chunk in chunks:
    res = openai.Embedding.create(
            model="text-embedding-3-large",
            input=chunk)
    embeddings.append(res["data"][0]["embedding"])
embeddings = np.array(embeddings, dtype="float32")
```

Dimensionality jumps to **3 072** (OpenAI) or whatever your provider returns; everything else (chunking, folder logic, storage) stays identical—just keep the folder name different if you mix dims.

---

Run the script, then open the new `~/Desktop/mydoc_embeddings` folder—you’ll see:

```
chunk_000.npy
chunk_001.npy
…
index.json
```

Each `.npy` is ready for loading into FAISS/Chroma or any other vector DB:

```python
vec = np.load("chunk_000.npy")
```

That’s it—happy embedding!
Below is a **drop-in Python script** that will

1. read any plain-text document,
2. split it into 1 000-character chunks,
3. embed each chunk (using the open-source `sentence-transformers` model `all-mpnet-base-v2`, 768-dim), and
4. save every embedding as its own `.npy` file in a *new* folder on your Desktop (it creates the folder if it doesn’t already exist).

```bash
# one-time setup
pip install -U sentence-transformers numpy
```

```python
# embed_doc.py  ── run:  python embed_doc.py mydoc.txt  (or .md/.pdf converted to text)

import sys, os, json
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNK_SIZE = 1000                      # characters
MODEL_NAME = "all-mpnet-base-v2"       # 768-dim
OUT_DIRNAME = "mydoc_embeddings"       # folder on Desktop

def load_text(filepath: Path) -> str:
    """Very simple loader; assumes UTF-8 text file."""
    return filepath.read_text(encoding="utf-8")

def chunkify(text: str, size: int = CHUNK_SIZE):
    """Yield non-overlapping chunks of ≤ size chars."""
    for i in range(0, len(text), size):
        yield i // size, text[i : i + size]

def main():
    if len(sys.argv) < 2:
        print("Usage: python embed_doc.py <path/to/document.txt>")
        sys.exit(1)

    src_file = Path(sys.argv[1]).expanduser().resolve()
    if not src_file.exists():
        raise FileNotFoundError(src_file)

    # 1. load & split
    text = load_text(src_file)
    chunks = list(chunkify(text))

    # 2. prepare output folder on Desktop
    desktop = Path.home() / "Desktop"
    out_dir = desktop / OUT_DIRNAME
    out_dir.mkdir(parents=True, exist_ok=True)   # no error if it exists

    # 3. embed
    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode([c[1] for c in chunks], batch_size=16,
                              convert_to_numpy=True, normalize_embeddings=True)

    # 4. persist each vector
    meta = []    # we’ll also keep a tiny index file
    for (idx, _), vec in zip(chunks, embeddings):
        fname = f"chunk_{idx:03d}.npy"
        np.save(out_dir / fname, vec)
        meta.append({"chunk_idx": idx, "file": fname})

    # write an index.json so you know what’s what
    with open(out_dir / "index.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    print(f"✅  {len(embeddings)} chunks embedded and saved to {out_dir}")

if __name__ == "__main__":
    main()
```

#### How it works

| Step                | Code line(s)                      | Detail                                                                                                |
| ------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Chunking**        | `chunkify()`                      | Simple slice every 1 000 characters. No overlap; tweak logic for sliding windows if you need context. |
| **Embedding model** | `SentenceTransformer(MODEL_NAME)` | Loads weights locally (≈420 MB the first time). Returns a 768-dim NumPy vector for each chunk.        |
| **Vector storage**  | `numpy.save()`                    | Saves each vector as its own binary `.npy` file for fast re-load. `index.json` maps chunk → file.     |

#### Switching to OpenAI / Gemini / Claude embeddings

Replace the model section:

```python
import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")
embeddings = []
for _, chunk in chunks:
    res = openai.Embedding.create(
            model="text-embedding-3-large",
            input=chunk)
    embeddings.append(res["data"][0]["embedding"])
embeddings = np.array(embeddings, dtype="float32")
```

Dimensionality jumps to **3 072** (OpenAI) or whatever your provider returns; everything else (chunking, folder logic, storage) stays identical—just keep the folder name different if you mix dims.

---

Run the script, then open the new `~/Desktop/mydoc_embeddings` folder—you’ll see:

```
chunk_000.npy
chunk_001.npy
…
index.json
```

Each `.npy` is ready for loading into FAISS/Chroma or any other vector DB:

```python
vec = np.load("chunk_000.npy")
```

That’s it—happy embedding!
