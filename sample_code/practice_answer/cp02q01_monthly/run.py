import eel
import datetime

## 2章演習問題Q1

# アプリのエンドポイント
def main():
    eel.init("practice_answer/cp02q01_monthly/view")
    eel.start("index.html")

def _calc_progress(target_date, resolution):
    if resolution == "daily":
        start_date = datetime.datetime(target_date.year, target_date.month, target_date.day)
        end_date = start_date + datetime.timedelta(1)
    elif resolution == "monthly":
        start_date = datetime.datetime(target_date.year, target_date.month, 1)
        end_date = datetime.datetime(target_date.year+target_date.month//12, 
                    target_date.month%12+1, 1)
    elif resolution == "yearly":
        start_date = datetime.datetime(target_date.year, 1, 1)
        end_date = datetime.datetime(target_date.year+1, 1, 1)
    return (target_date-start_date) / (end_date-start_date)

# 公開名を変更
@eel.expose("server_get_time_progress")
def get_time_progress():
    # 現在時刻
    dt = datetime.datetime.now()
    # 日次のプログレス
    daily_progress = _calc_progress(dt, "daily")
    # 月次のプログレス
    monthly_progress = _calc_progress(dt, "monthly")
    # 年次のプログレス
    yearly_progress = _calc_progress(dt, "yearly")

    eel.client_updateMessage({
        "currentTime": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "dailyProgress": round(daily_progress*100, 1),
        "monthlyProgress": round(monthly_progress*100, 1),
        "yearlyProgress": round(yearly_progress*100, 1)
    })

if __name__ == "__main__":
    main()
