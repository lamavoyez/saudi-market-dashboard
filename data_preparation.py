import yfinance as yf
import pandas as pd
import numpy as np

# 1- Define Stocks

stocks = ['2222.SR', '1180.SR', '2010.SR', 'KSA']
start_date = '2015-01-01'

all_data = []

# 2) Download + Clean + Feature Engineering

for stock in stocks:
    
    print(f"Downloading {stock} ...")
    
    df = yf.download(stock, start=start_date, auto_adjust=True, progress=False)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.dropna()
    df = df.sort_index()

    df['Stock'] = stock

    # Financial Metrics 
    df['Daily Return'] = df['Close'].pct_change()
    df['Cumulative Return'] = (1 + df['Daily Return']).cumprod()

    # Max Drawdown 
    df['Running_Max'] = df['Cumulative Return'].cummax()
    df['Drawdown'] = df['Cumulative Return'] / df['Running_Max'] - 1

    # Moving Averages
    df['MA20'] = df['Close'].rolling(20).mean()
    df['MA50'] = df['Close'].rolling(50).mean()
    df['MA200'] = df['Close'].rolling(200).mean()

    # Volatility
    df['Volatility_30D'] = df['Daily Return'].rolling(30).std()

    df = df.dropna()

    all_data.append(df)

# 3- Combine All Stocks

final_df = pd.concat(all_data)
final_df.reset_index(inplace=True)

final_df['Date'] = pd.to_datetime(final_df['Date'])
final_df = final_df.drop_duplicates()
final_df = final_df.sort_values(by=['Stock', 'Date'])

# 4- Save Clean Dataset

final_df.to_csv("clean_stock_data.csv", index=False)
print("clean_stock_data.csv saved")

# 5- Correlation Matrix

pivot = final_df.pivot(index='Date', columns='Stock', values='Daily Return')
correlation = pivot.corr()
correlation.to_csv("correlation_matrix.csv")
print(" correlation_matrix.csv saved")

# 6- Risk Summary Table

risk_summary = []

for stock in final_df['Stock'].unique():
    
    temp = final_df[final_df['Stock'] == stock]
    
    annual_return = temp['Daily Return'].mean() * 252
    annual_volatility = temp['Daily Return'].std() * np.sqrt(252)
    
    sharpe_ratio = annual_return / annual_volatility if annual_volatility != 0 else 0
    
    max_drawdown = temp['Drawdown'].min()

    risk_summary.append({
        'Stock': stock,
        'Annual Return': annual_return,
        'Annual Volatility': annual_volatility,
        'Sharpe Ratio': sharpe_ratio,
        'Max Drawdown': max_drawdown
    })

risk_df = pd.DataFrame(risk_summary)
risk_df.to_csv("risk_summary.csv", index=False)

print("risk_summary.csv saved")
print("Data preparation completed successfully!")
