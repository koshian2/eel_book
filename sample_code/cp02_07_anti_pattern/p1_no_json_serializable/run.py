import eel
import datetime

# アプリのエンドポイント
def main():
    eel.init("cp02_07_anti_pattern/p1_no_json_serializable")
    eel.start("index.html")

@eel.expose
def get_current_time():
    # JSON化できないアイテムを返すのはNG　→　ここを文字列にすればOK
    eel.updateMessage(datetime.datetime.now())

if __name__ == "__main__":
    main()