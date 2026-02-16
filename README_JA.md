# Semantic OS – Free Edition

軽くて速い、ローカル専用の「記憶検索 OS」

Semantic OS Free Edition は、  
ローカルに保存したテキストメモを高速に検索できる無料版です。

- 完全ローカル  
- 依存最小  
- 10秒で起動  
- 500件まで保存可能  
- 文字列検索のみ（意味検索はプロ版）

「まずは軽く試したい」「ローカルでメモを管理したい」  
そんな人向けのエントリーモデルです。

---

## 特徴（無料版）

- ローカル保存（JSONL）  
- 高速な文字列検索  
- 500件まで保存可能  
- CLI でシンプルに操作  
- インターネット不要

無料版は「軽くて壊れない」ことを最優先に設計されています。

---

## インストール

```bash
git clone https://github.com/yourname/semantic-os-free.git
cd semantic-os-free
pip install -r requirements.txt


---

使い方（CLI）

起動

python main.py --mode cli

メモを追加

add
memory: 今日の会議メモをまとめた
saved.

検索

search
query: 会議
→ "会議" を含むメモを表示

一覧表示

list
1: 今日の会議メモをまとめた

※ 意味検索（MiniLM）はプロ版で利用できます。


---

保存データについて

すべてローカルに保存されます

外部送信は一切ありません

保存形式：data/memories.jsonl

1行1メモのシンプルな構造



---

プロ版（Semantic OS Pro）について

無料版を使ってみて、
「もっと検索したい」「もっと保存したい」と感じたら、
プロ版が最適です。

プロ版では：

MiniLM による高速意味検索

保存件数無制限

高速ベクトル検索エンジン

Web UI（Flask）

ライセンスキーで解放


が利用できます。


---

ファイル構成（無料版）

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

コード例（無料版）

memory_store.py

# ここに先ほど作った memory_store.py のコードをそのまま貼る


---

ライセンス

MIT License


---

コントリビューション

Issue / PR 歓迎です。
無料版の改善はプロ版の進化にもつながります。