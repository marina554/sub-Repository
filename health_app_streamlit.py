# health_app_streamlit.py
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import datetime
from matplotlib import rcParams

# 日本語フォント対応（Windows / Mac / Colab）
rcParams['font.family'] = 'Yu Gothic'  # Windowsなら'MS Gothic'や'Yu Gothic'
rcParams['axes.unicode_minus'] = False

CSV_FILE = "health_log.csv"

def get_score():
    score = st.slider("今日の気分スコアを選んでください（0～100）", 0, 100, 50)
    return score

def show_message(score):
    if score <= 50:
        st.info("今日は無理をしないでください。")
    elif score <= 70:
        st.success("普段どおりいきましょう。")
    else:
        st.success("いいですね！その調子です！")

def save_to_csv(score):
    date = datetime.date.today()
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        import csv
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Score"])
        writer.writerow([date, score])
    st.write(f"{date} のスコア（{score}点）を記録しました。")

def plot_health_log():
    if not os.path.exists(CSV_FILE):
        st.warning("まだ記録がありません。")
        return

    df = pd.read_csv(CSV_FILE)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df["Date"], df["Score"], marker="o", linestyle="-")
    ax.set_title("気分スコアの推移")
    ax.set_xlabel("日付")
    ax.set_ylabel("スコア")
    ax.grid(True, linestyle="--", alpha=0.5)

    # 日付軸を自動調整
    if len(df) <= 30:
        ax.xaxis.set_major_locator(mdates.DayLocator())
    else:
        ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    fig.autofmt_xdate()
    st.pyplot(fig)

def main():
    st.title("🩺 Health Logger アプリ")
    st.write("日々の気分スコアを記録し、グラフで可視化します。")

    score = get_score()
    if st.button("記録する"):
        show_message(score)
        save_to_csv(score)
        plot_health_log()

    # 過去データのグラフ表示
    if st.checkbox("過去の記録を表示"):
        plot_health_log()

if __name__ == "__main__":
    main()






