import eel

# アプリのエンドポイント
def main():
    eel.init("cp02_07_anti_pattern/p2_no_vm")
    eel.start("index.html")

@eel.expose
def get_data():
    eel.updateMessage({
        "normalMessage": "更新完了",
        "listMessage": [i for i in range(10000)]
    })

if __name__ == "__main__":
    main()