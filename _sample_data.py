import csv
import random

# 1. Define the scope constraints
TIME_PERIODS = 12  # Fits the 8–12 time periods requirement
OUTPUT_FILE = "sample_brand_dataset.csv"

# 2. Setup the headers representing 4 distinct signal families + 1 future outcome
headers = [
    "time_period",
    # Family 1: Search & Traffic Signals
    "search_volume_index", "website_unique_visitors",
    # Family 2: Social & Sentiment Signals
    "social_mention_count", "net_sentiment_score",
    # Family 3: Paid Media & Marketing Signals
    "ad_impressions_thousands", "click_through_rate",
    # Family 4: Market & Competitor Signals
    "competitor_share_of_voice", "industry_growth_baseline",
    # Future Outcome (Kept separate for prediction testing)
    "future_brand_revenue_usd"
]

# 3. Generate synthetic data over time with a realistic growth baseline
data_rows = []
base_revenue = 50000

for month in range(1, TIME_PERIODS + 1):
    # Simulate a brand that is growing slightly month-over-month
    growth_trend = 1.0 + (month * 0.03) 
    
    row = {
        "time_period": f"Month_{month:02d}",
        
        # Family 1: Search & Traffic (Integers, scaled by trend)
        "search_volume_index": int(random.randint(40, 60) * growth_trend),
        "website_unique_visitors": int(random.randint(10000, 15000) * growth_trend),
        
        # Family 2: Social & Sentiment (Volume fluctuates, sentiment bounded between -1 and 1)
        "social_mention_count": int(random.randint(500, 1200) * growth_trend),
        "net_sentiment_score": round(random.uniform(0.1, 0.6), 2),
        
        # Family 3: Paid Media (Marketing inputs)
        "ad_impressions_thousands": int(random.randint(200, 400) * growth_trend),
        "click_through_rate": round(random.uniform(0.015, 0.035), 3),
        
        # Family 4: Market Context
        "competitor_share_of_voice": round(random.uniform(0.20, 0.35), 2),
        "industry_growth_baseline": round(random.uniform(0.01, 0.04), 3),
        
        # Future Outcome: Correlated broadly with signals but containing some variance
        "future_brand_revenue_usd": int(base_revenue * growth_trend * random.uniform(0.95, 1.05))
    }
    data_rows.append(row)

# 4. Save the generated dataset to a CSV file
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for row in data_rows:
        writer.writerow(row)

print(f"Success! Generated '{OUTPUT_FILE}' with {TIME_PERIODS} time periods.")
