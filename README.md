# 📈 Portfolio Optimization with Modern Portfolio Theory

This project explores how to build optimal investment portfolios using historical stock data and principles from Modern Portfolio Theory (MPT). It calculates key portfolio statistics like expected return, volatility, and Sharpe ratio, and then finds asset allocations that either **maximize the Sharpe ratio** or **minimize portfolio variance**.

## 🚀 Key Features

- Input your own list of stock tickers
- Download historical stock price data from Yahoo Finance
- Calculate:
  - Daily returns (log returns)
  - Annualized expected return
  - Annualized portfolio volatility
  - Sharpe ratio
- Optimize portfolio for:
  - **Maximum Sharpe Ratio**
  - **Minimum Variance**
- Visualize the **Efficient Frontier** with optimal points highlighted

## 📂 Folder Structure

```
portfolio-optimization/
├── data/           # Optional saved datasets (e.g. .csv of prices)
├── notebooks/      # Jupyter notebooks for development
├── scripts/        # Reusable Python functions
├── results/        # Output plots, images, results
├── requirements.txt
└── README.md
```

## 🛠️ Tools & Libraries

- Python
- Jupyter Notebooks
- pandas, numpy, matplotlib, yfinance, scipy

## 🧠 Learning Goals

This is an independent project designed to:
- Strengthen skills in data analysis, financial modeling, and optimization
- Demonstrate application of MPT for a technical portfolio
- Learn through building, applying theoretical knowledge to a practical tool
