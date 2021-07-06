import eel
import datetime

# アプリのエンドポイント（eel.expose）で公開しない
def main():
    eel.init("cp02_01_interactive1")
    eel.start("index.html")

# HTMLから呼ばれる関数。@eel.exposeで公開
@eel.expose
def get_current_time():
    dt = datetime.datetime.now()
    eel.updateMessage(dt.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()