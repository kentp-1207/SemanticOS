from memory_store import MemoryStore, SearchEngine

def main():
    store = MemoryStore()
    searcher = SearchEngine(store)

    print("SemanticOS Free Edition")
    print("------------------------")

    while True:
        print("\n1) Add memory")
        print("2) Search memories")
        print("3) List all memories")
        print("4) Exit")
        choice = input("> ").strip()

        if choice == "1":
            text = input("Memory: ")
            store.add_memory(text)
            searcher.refresh()
            print("Saved.")

        elif choice == "2":
            q = input("Query: ")
            results = searcher.search(q)
            if not results:
                print("No results.")
            else:
                for r in results:
                    print(f"[{r['score']:.3f}] {r['text']}")

        elif choice == "3":
            memories = store.list_memories()
            if not memories:
                print("No memories saved.")
            else:
                for m in memories:
                    print(f"- {m['text']}")

        elif choice == "4":
            print("Bye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
