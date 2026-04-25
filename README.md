Football Analysis Project
International Football Results (1872–2024) - Kaggle Dataset Analysis

📊 Project Overview
Dataset: ./data/results.csv (49,287 matches, 9 columns)

Analysis: Basic exploration, goals, match results, visualizations

Outputs: Charts, CSV answers, cleaned data

Tech: Python, Pandas, Matplotlib, Seaborn

🎯 Exercise Answers Summary
Question	Answer
Total matches	49,287
Years covered	1872–2024
Unique countries	301
Top home team	Brazil
Avg goals/match	2.72
Highest scoring	Australia 31-0 American Samoa
Home advantage	Yes (1.59 vs 1.13 goals)
Most common goals	2
Home win %	44.8%
Most wins	Brazil (533)
Full answers: output/exercise_answers.csv

📁 File Structure
text
football-analysis/
├── data/
│   ├── results.csv              # Original Kaggle dataset (49,287 rows)
│   └── processed/
│       └── results_clean.csv    # Cleaned data
├── src/
│   └── football_analysis.py     # Main analysis script
├── output/
│   ├── football_analysis.png    # Tron-themed charts
│   ├── exercise_answers.csv     # All exercise answers
│   └── complete_analysis.png    # Alternative charts
├── README.md                    # This file
└── venv/                        # Python virtual environment
🚀 Quick Start
bash
# 1. Navigate & activate
cd ~/football-analysis
source venv/bin/activate

# 2. Run analysis (auto-creates outputs)
python3 src/football_analysis.py

# 3. View results
xdg-open output/football_analysis.png
cat output/exercise_answers.csv
📈 Visualizations Generated
Goals Histogram - Distribution of total goals per match

Match Outcomes Bar - Home Win/Draw/Away Win percentages

Top 10 Teams Bar - Historical wins ranking

Home Advantage Trend - Home win % over time

Theme: Dark Tron cyberpunk styling

🔧 Key Findings
text
Home Advantage: STRONG (44.8% vs 26.5% away wins)
Average Match: 2.72 goals
Record Win: Australia 31-0 American Samoa (2001)
Dominant Team: Brazil (533 total wins)
Most Common Scoreline: 2 total goals
🐳 Docker (Optional)
text
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install pandas matplotlib seaborn
CMD ["python", "src/football_analysis.py"]
bash
docker build -t football-analysis .
docker run -v $(pwd)/output:/app/output football-analysis
📝 Reproduction
Dataset: Download from Kaggle → data/results.csv

Requirements: pandas matplotlib seaborn

Run: python3 src/football_analysis.py

Results: Instant charts + CSV answers


