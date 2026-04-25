Football Analysis Project - README.md
🎯 Project Outline
text
Football Analysis Exercise
├── Dataset: International Football Results (1872–2024)
│   └── data/results.csv (49,287 matches)
├── Objectives:
│   ├── Basic Exploration
│   ├── Goals Analysis
│   ├── Match Results
│   └── Visualizations
└── Deliverables:
    ├── Code (football_analysis.py)
    ├── Charts (4 plots)
    └── Answers CSV
📋 Exercise Breakdown
Step 1: Load CSV
python
import pandas as pd
df = pd.read_csv('data/results.csv')
df.head()
Step 2: Basic Exploration
text
❓ Questions:
• How many matches? → 49,287
• Earliest/latest year? → 1872–2024  
• Unique countries? → 301
• Most frequent home team? → Brazil

✅ Code: df.shape, df['date'].min().year, df['home_team'].value_counts()
Step 3: Goals Analysis
text
❓ Questions:
• Avg goals/match? → 2.72
• Highest scoring? → Australia 31-0 American Samoa
• Home vs away goals? → Home 1.59 > Away 1.13
• Most common total? → 2 goals

✅ Code:
df['total_goals'] = df['home_score'] + df['away_score']
df['total_goals'].mean(), df.loc[df['total_goals'].idxmax()]
Step 4: Match Results
text
❓ Questions:
• Home win %? → 44.8%
• Home advantage? → Yes (44.8% vs 26.5%)
• Most wins? → Brazil (533)

✅ Code:
def match_result(row): ...
df['result'] = df.apply(match_result, axis=1)
(df['result']=='Home Win').mean() * 100
Step 5: Visualizations
text
✅ Generated:
1. Goals Histogram → df['total_goals'].hist(bins=20)
2. Outcomes Bar → df['result'].value_counts().plot.bar()
3. Top 10 Wins → total_wins.head(10).plot.bar()
📂 File Structure
text
football-analysis/
├── data/
│   ├── results.csv           # Input (49,287 rows)
│   └── processed/
│       └── results_clean.csv
├── src/
│   └── football_analysis.py  # All code above
├── output/
│   ├── football_analysis.png # 2x2 charts
│   └── exercise_answers.csv  # Table of all answers
├── requirements.txt
├── Makefile
└── README.md
🚀 Run Instructions
bash
cd ~/football-analysis
source venv/bin/activate
pip install -r requirements.txt
python3 src/football_analysis.py
📊 Complete Results Table
output/exercise_answers.csv:

text
Question,Answer
"How many matches?",49287
"Earliest/latest year?","1872-2024"
"Unique countries?",301
"Most frequent home team?","Brazil"
"Avg goals per match?",2.72
...
🎨 Visual Output Preview
text
[football_analysis.png - 2x2 grid]
┌ Goals Histogram    │ Match Outcomes Bar  ┐
│                   │ Home:44.8% Draw:28% │
├─ Top 10 Wins ─────┤ Home Win Trend ─────┤
│ Brazil #1 (533)   │ 45% steady ─────────┘
