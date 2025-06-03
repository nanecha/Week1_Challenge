# 🧠 10 Academy: AI Mastery - Week 1 Challenge
## Project Structure
```
Week1_challenges/
├──githubWorkflow/
    ├──unittests.yml
├── .vscode
    ├──settings.json
├──Data/
    ├──raw data analysis rating.csv      #Folder for datasets
    ├──yfinance_data
├── notebooks/     # Jupyter notebooks
    ├── __init__.py
    ├──EDA for raw_analysis
    ├──quantitaive.ipynb
    ├──financial_analysis.ipynb
    ├──README.md
├──Script    #python scripts
    ├── __init__.py
    ├──data_loader.py
    ├──financial_analysis.py
├── src/                    # Main Python package
│   ├── __init__.py       # test
│   ├── evaluate.py     # Functions for accuracy,
├── tests/                  # Unit tests
│   └── run_tests.py
├── README.md               # Project overview
└── requirements.txt        # Dependencies

  ```
# Getting Started

### Prerequisites
- Python 3.8 or higher
- Libraries: Install dependencies from `requirements.txt` using:
  ```bash
  pip install -r requirements.txt
  ```
## 📈 Predicting Price Moves with News Sentiment

Analyze how financial news influences stock price movements using sentiment analysis, technical indicators, and statistical correlations.

📅 **Duration:** 28 May – 03 June 2025

---

## 🚀 Challenge Overview

This project explores how news sentiment affects stock performance using the **Financial News and Stock Price Integration Dataset (FNSPID)**. It combines skills from data engineering, financial analytics, and machine learning to extract actionable insights.

---

## 🎯 Objectives

- To Perform **sentiment analysis** on financial headlines using NLP.
- To Analyze **correlation** between sentiment and stock price movements.
- To understand  market trend for future prediction and recommendation
---

## 📊 Key Tasks

### ✅ Task 1: Git, GitHub & EDA
-  Git/GitHub with branches and commits
- Perform EDA on headline text and publication patterns
- Perform descriptive statistics and technical analysis

### ✅ Task 2: Technical Analysis
- Use **TA-Lib** & **PyNance** for financial indicators
- Visualize trends and metrics

### ✅ Task 3: Sentiment vs Stock Movement
- Analyze and align datasets by date
- Quantify sentiment with tools like `TextBlob`
- Compute stock returns and correlation scores

# 📰 Financial News Analysis
Analyze financial news headlines

# ✨ Features
🗞️ Financial News Analysis
- Load and preview financial news headlines
- Compute headline length stats (mean, median, min, max)
- Analyze article publication trends by date and day of the week
- Perform sentiment analysis using TextBlob
- Visualizations include:
- Sentiment distribution
- Article frequency by time
- Headline length histograms

# 📊 Stock Market Analysis
- Load historical stock price data using yfinance

- Preprocessing and cleaning of missing values
- Compute daily stats: mean, std, min, max, quartiles
- Generating of advanced visualizations with Matplotlib and Plotly

# Apply technical indicators using TA-Lib:
- RSI, MACD, Bollinger Bands, etc.

- Integrate sentiment scores for enriched insights

# 🧰 Dependencies
Install the required packages:

- bash Copy Edit pip install pandas numpy matplotlib seaborn textblob plotly yfinance Optional (for technical indicators)
bash Copy Edit
- Requires system-specific setup
Refer to the TA-Lib installation guide for your OS
pip install TA-Lib
 - read the requirement.txt  text
# 📂 Dataset Descriptions
- News Headlines Dataset Location: ../Data/raw/raw_analyst_ratings.csv Columns:

- Stock Market Data Fetched via: yfinance Columns:
Open, High, Low, Close, Adj Close, Volume

# ▶️ Usage bash Copy Edit

1. Clone the repository
git clone https://github.com/nanecha/
2. Install dependencies
pip install -r requirements.txt
3. Launch Jupyter Lab or Notebook

# 🧠 Learning Outcomes

- Reproducible Python data science workflows
- Time series & NLP analysis
- Technical indicators: MA, RSI, MACD
- Correlation studies between sentiment and returns

# 🔗 Resources

- [TA-Lib](https://github.com/ta-lib/ta-lib-python)
- [PyNance](https://github.com/mqandil/pynance)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [Git Docs](https://git-scm.com/doc)

## 📬 Contact
 nanechakebede@gmail.com
