import eel
import os
import glob
import re

## 2章演習問題Q2

# アプリのエンドポイント
def main():
    eel.init("practice_answer/cp02q02_novel/view")
    eel.start("index.html")

# 公開名を変更
@eel.expose("server_load_novels")
def load_novels():
    post_data = []
    # ファイルを列挙
    files = sorted(glob.glob("practice_answer/cp02q02_novel/data/*.txt"))
    for f in files:
        with open(f, encoding="utf-8") as fp:
            raw_data = fp.read()
        # 編集注を削除
        data = re.sub("［＃[^］.]*］", "", raw_data)
        # ルビを削除
        data = re.sub("《[^》.]*》", "", data)
        # 行単位で分割（改行コードの統一）
        lines = data.replace("\r\n", "\n").split("\n")
        post_data.append({
            "Title": os.path.splitext(os.path.basename(f))[0],
            "Text": lines
        })
    # Eelに転送
    eel.client_updatePosts(post_data)

if __name__ == "__main__":
    main()
