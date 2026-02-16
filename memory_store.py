import json
import os
from datetime import datetime
from typing import List, Dict, Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = "data/memories.jsonl"
MAX_MEMORIES = 500  # 内部的なメモリ保持上限


class MemoryStore:
    def __init__(self, path: str = DATA_PATH, max_memories: int = MAX_MEMORIES):
        self.path = path
        self.max_memories = max_memories
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self.memories: List[Dict[str, Any]] = self._load()

    def _load(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.path):
            return []
        memories = []
        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                memories.append(json.loads(line))
        return memories

    def save_all(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            for m in self.memories:
                f.write(json.dumps(m, ensure_ascii=False) + "\n")

    def add_memory(self, text: str, meta: Dict[str, Any] | None = None) -> None:
        if meta is None:
            meta = {}
        memory = {
            "id": len(self.memories) + 1,
            "text": text,
            "meta": meta,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.memories.append(memory)

        # 内部的なメモリ保持数の調整
        if len(self.memories) > self.max_memories:
            self.memories = self.memories[-self.max_memories :]

        self.save_all()

    def list_memories(self) -> List[Dict[str, Any]]:
        return list(self.memories)


class SearchEngine:
    def __init__(self, store: MemoryStore):
        self.store = store
        self.vectorizer = TfidfVectorizer()
        self.fit_vectorizer()

    def fit_vectorizer(self) -> None:
        texts = [m["text"] for m in self.store.memories]
        if not texts:
            self.tfidf_matrix = None
            return
        self.tfidf_matrix = self.vectorizer.fit_transform(texts)

    def refresh(self) -> None:
        self.fit_vectorizer()

    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        if not self.store.memories or self.tfidf_matrix is None:
            return []
        query_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(query_vec, self.tfidf_matrix)[0]
        ranked_indices = sims.argsort()[::-1][:top_k]

        results = []
        for idx in ranked_indices:
            m = self.store.memories[idx]
            results.append(
                {
                    "id": m["id"],
                    "text": m["text"],
                    "meta": m["meta"],
                    "timestamp": m["timestamp"],
                    "score": float(sims[idx]),
                }
            )
        return results


def demo():
    store = MemoryStore()
    searcher = SearchEngine(store)

    while True:
        mode = input("add/search/exit > ").strip()
        if mode == "add":
            text = input("memory: ")
            store.add_memory(text)
            searcher.refresh()
            print("saved.")
        elif mode == "search":
            q = input("query: ")
            results = searcher.search(q)
            for r in results:
                print(f"[{r['score']:.3f}] {r['text']}")
        elif mode == "exit":
            break
        else:
            print("unknown command")


if __name__ == "__main__":
    demo()
