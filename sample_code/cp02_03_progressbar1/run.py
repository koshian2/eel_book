import eel
import datetime

# アプリのエンドポイント
def main():
    eel.init("cp02_03_progressbar1")
    eel.start("index.html")

def _calc_progress(target_date, resolution):
    if resolution == "daily":
        start_date = datetime.datetime(target_date.year, target_date.month, target_date.day)
        end_date = start_date + datetime.timedelta(1)
    elif resolution == "yearly":
        start_date = datetime.datetime(target_date.year, 1, 1)
        end_date = datetime.datetime(target_date.year+1, 1, 1)
    return (target_date-start_date) / (end_date-start_date)

@eel.expose
def get_time_progress():
    # 現在時刻
    dt = datetime.datetime.now()
    # 日次のプログレス
    daily_progress = _calc_progress(dt, "daily")
    # 年次のプログレス
    yearly_progress = _calc_progress(dt, "yearly")

    eel.updateMessage({
        "date": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "daily_progress": round(daily_progress*100, 1),
        "yearly_progress": round(yearly_progress*100, 1)
    })

if __name__ == "__main__":
    main()
