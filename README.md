Semantic OS – Free Edition (English README)

Semantic OS – Free Edition
A lightweight, local-only “memory search OS” for text notes.

Semantic OS Free Edition lets you search your locally saved text notes at high speed, all without internet access.

Fully local

Minimal dependencies

Launch in seconds

Save up to 500 notes

String-based search only (meaning-based search in Pro version)


Perfect for those who want a light, reliable, local memory management tool.


---

Features (Free Edition)

Local storage (JSONL)

Fast string-based search

Up to 500 memories

Simple CLI interface

No internet required


The free edition is designed to stay light and stable, without advanced features.


---

Install

git clone https://github.com/yourname/semantic-os-free.git
cd semantic-os-free
pip install -r requirements.txt

> Setup is fast since dependencies are minimal.




---

Usage (CLI)

Start CLI:

python main.py --mode cli

Add a memory:

add
memory: Today’s meeting notes
saved.

Search:

search
query: meeting
→ Displays memories containing “meeting”

List all memories:

list
1: Today’s meeting notes

> Meaning-based search (MiniLM) is available in the Pro version.




---

Saved Data

All data is saved locally

Nothing is sent externally

File: data/memories.jsonl

Simple “one-line per memory” format



---

Pro Version (Semantic OS Pro)

Once you try the free edition, if you want more advanced search and unlimited storage, Semantic OS Pro is the answer.

Pro features:

MiniLM-powered semantic search

Unlimited memory storage

Fast vector search engine

Web UI (Flask)

License key unlock


The free edition is your entry point to the Pro version.


---

Folder Structure (Free Edition)

semantic_os/
  core/
    memory_store.py
    search_string.py
  ui/
    cli.py
  data/
    memories.jsonl
  main.py


---

License

MIT License


---

Contributing

Issues / PRs welcome.
Improving the free edition directly benefits the evolution of the Pro version.