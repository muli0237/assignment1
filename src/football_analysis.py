#!/usr/bin/env python3
"""
Football Analysis - Uses ./data/results.csv
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# LOAD YOUR DATASET
csv_path = 'data/results.csv'
print(f"✅ Loading {csv_path}...")

df = pd.read_csv(csv_path)
print(f"📊 Raw shape: {df.shape}")

# Fix dates (handles all formats)
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['date']).reset_index(drop=True)
df.to_csv('data/processed/results_clean.csv', index=False)

print(f"✅ Cleaned: {df.shape[0]:,} matches ({df['date'].min().year}–{df['date'].max().year})")
print("\nColumns:", list(df.columns))

# 1. BASIC EXPLORATION
print("\n📈 BASIC EXPLORATION")
print(f"• Matches: {df.shape[0]:,}")
print(f"• Years: {df['date'].min().year} to {df['date'].max().year}")
print(f"• Countries: {pd.concat([df['home_team'], df['away_team']]).nunique()}")
print(f"• Top home team: {df['home_team'].value_counts().head(1).index[0]}")

# 2. GOALS
df['total_goals'] = df['home_score'] + df['away_score']
print("\n⚽ GOALS ANALYSIS")
print(f"• Avg goals/match: {df['total_goals'].mean():.2f}")
print(f"• Home advantage: {df['home_score'].mean():.2f} vs {df['away_score'].mean():.2f}")
print(f"• Most common total: {int(df['total_goals'].mode()[0])}")

high_match = df.loc[df['total_goals'].idxmax()]
print(f"• Highest scoring: {high_match['home_team']} {int(high_match['home_score'])}-{int(high_match['away_score'])} {high_match['away_team']}")

# 3. RESULTS
print("\n🏆 MATCH RESULTS")
def match_result(row):
    if pd.isna(row['home_score']) or pd.isna(row['away_score']): return 'Invalid'
    if row['home_score'] > row['away_score']: return 'Home Win'
    if row['home_score'] < row['away_score']: return 'Away Win'
    return 'Draw'

df['result'] = df.apply(match_result, axis=1)
valid_matches = df[df['result'] != 'Invalid']
home_win_pct = (valid_matches['result'] == 'Home Win').mean() * 100
print(f"• Home win %: {home_win_pct:.1f}%")

# Most wins
home_wins = valid_matches[valid_matches['result']=='Home Win']['home_team'].value_counts()
away_wins = valid_matches[valid_matches['result']=='Away Win']['away_team'].value_counts()
total_wins = home_wins.add(away_wins, fill_value=0).astype(int)
print(f"• Most wins: {total_wins.idxmax()} ({total_wins.max()})")

# 4. VISUALIZATIONS
print("\n📊 VISUALIZATIONS")
os.makedirs('output', exist_ok=True)
plt.style.use('dark_background')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Goals histogram
df['total_goals'].hist(bins=20, ax=axes[0,0], color='cyan', alpha=0.8, edgecolor='white')
axes[0,0].set_title('Goals per Match Histogram')
axes[0,0].set_xlabel('Total Goals')
axes[0,0].tick_params(colors='white')

# Outcomes bar
valid_matches['result'].value_counts().plot.bar(ax=axes[0,1], 
                  color=['#00ff41', '#ffea00', '#ff4757'])
axes[0,1].set_title('Match Outcomes')
axes[0,1].tick_params(colors='white')

# Top 10 wins
total_wins.head(10).plot.bar(ax=axes[1,0], color='gold')
axes[1,0].set_title('Top 10 Teams by Wins')
axes[1,0].tick_params(colors='white')

# Home advantage trend
trend = valid_matches.groupby(valid_matches['date'].dt.year)['result'].apply(lambda x: (x=='Home Win').mean())
trend.plot(ax=axes[1,1], color='lime', linewidth=2)
axes[1,1].set_title('Home Win % Over Time')
axes[1,1].tick_params(colors='white')

plt.suptitle('Football Analysis - All Exercise Visuals', color='cyan', fontsize=16)
plt.tight_layout()
plt.savefig('output/football_analysis.png', dpi=300, facecolor='black', bbox_inches='tight')
plt.show()

# 5. EXERCISE ANSWERS TABLE
print("\n📋 EXERCISE ANSWERS")
answers = pd.DataFrame({
    'Question': [
        'How many matches?',
        'Earliest/latest year?',
        'Unique countries?',
        'Most frequent home team?',
        'Avg goals per match?',
        'Highest scoring match?',
        'More home or away goals?',
        'Most common total goals?',
        'Home win percentage?',
        'Country with most wins?'
    ],
    'Answer': [
        f"{df.shape[0]:,}",
        f"{df['date'].min().year}/{df['date'].max().year}",
        f"{pd.concat([df['home_team'], df['away_team']]).nunique()}",
        df['home_team'].value_counts().head(1).index[0],
        f"{df['total_goals'].mean():.2f}",
        f"{high_match['home_team']} {int(high_match['home_score'])}-{int(high_match['away_score'])} {high_match['away_team']}",
        f"Home ({df['home_score'].mean():.2f} > Away {df['away_score'].mean():.2f})",
        f"{int(df['total_goals'].mode()[0])}",
        f"{home_win_pct:.1f}%",
        f"{total_wins.idxmax()} ({total_wins.max()})"
    ]
})
print(answers.to_string(index=False))
answers.to_csv('output/exercise_answers.csv', index=False)

print("\n🎉 DONE!")
print("📁 Files: output/football_analysis.png | output/exercise_answers.csv")
