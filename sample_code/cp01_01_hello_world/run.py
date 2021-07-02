import eel

def main():
    # 現在のcp_01_hello_worldフォルダをWebディレクトリとみなす
    # ワークスペースからの実行を想定したパス
    eel.init("cp01_01_hello_world")
    # cp_01_hello_world/index.htmlを表示
    eel.start("index.html")

if __name__ == "__main__":
    main()