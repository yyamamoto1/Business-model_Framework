# -*- coding: utf-8 -*-
import pandas as pd

def analyze_churn(csv_path):
    '''
    サブスクリプションデータから月次のチャーンレートを計算する簡単な例。
    '''
    try:
        df = pd.read_csv(csv_path, parse_dates=['start_date', 'end_date'])
    except FileNotFoundError:
        print(f"エラー: {csv_path} が見つかりません。")
        return

    # end_dateがNaTでない（=解約済み）ものをチャーンと定義
    df['churned'] = df['end_date'].notna()
    
    # 簡単のため、start_dateの月を契約月とする
    df['start_month'] = df['start_date'].dt.to_period('M')
    
    # 月ごとに契約者数とチャーン数を計算
    monthly_subs = df.groupby('start_month').size()
    monthly_churns = df[df['churned']].groupby('start_month').size()
    
    # 月次チャーンレートを計算
    churn_rate = (monthly_churns / monthly_subs).fillna(0) * 100
    
    print("--- 月次チャーンレート分析結果 ---")
    for month, rate in churn_rate.items():
        print(f"{month}: {rate:.2f}%")

if __name__ == '__main__':
    # サンプルCSVファイルを読み込んで分析実行
    analyze_churn('data/sample_subscriptions.csv')
