# btc-eur-market-cycles
A Python project where I find a decade of Bitcoin prices to see if traditional stock market math can actually spot crypto bull runs.
# 📈 10 Years of Bitcoin: A Python Data Analysis

## 👋 Welcome to my project!
Everyone talks about Bitcoin's wild price swings, but I wanted to actually look at the raw data to see if we can make sense of it. 

For this project, I took a massive dataset of 10 years of daily Bitcoin prices (in Euros) and built a Python script to see if traditional stock market math—specifically Moving Averages—could successfully track and predict crypto market cycles. 

Instead of just drawing a static chart, I built this script to act as a mini "data engine." When you run it, it automatically parses the dataset, crunches the numbers, and prints out a real-time market report to the console.

## 🤔 What was I trying to find out?
I went into this project with three main questions:
1. **What is the actual, mathematical growth of Bitcoin over the last decade?** (Ignoring the daily hype).
2. **Can traditional finance indicators work on crypto?** (I tested the 50-Day and 200-Day Simple Moving Averages).
3. **Can code identify historic "Bull" and "Bear" markets automatically?**

## 💻 What the code actually finds (Terminal Output)
When you run the script, it doesn't just process the data behind the scenes—it answers the questions above by printing this exact report directly into your terminal:

```text
----------------------------------------
📈 BITCOIN MACRO TREND REPORT
----------------------------------------
Start Date:  2014-09-18 | Price: €328.54
End Date:    2024-03-15 | Price: €62,881.39
Total Macro Growth: 19,039.68%

🟢 RECENT GOLDEN CROSSES (Bull Market Start):
   -> 2021-09-12 at €38,997.03
   -> 2023-02-15 at €22,735.56
   -> 2023-10-26 at €32,653.23

🔴 RECENT DEATH CROSSES (Bear Market Start):
   -> 2021-06-19 at €30,019.23
   -> 2022-01-18 at €37,403.79
   -> 2023-09-13 at €24,023.85
----------------------------------------
