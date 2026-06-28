import json
import os

from preprocess import load_data, clean_data, save_cleaned_data
from insights import (
    calculate_kpis,
    conversion_distribution,
    conversion_rate_by_column,
    campaign_volume_by_column,
    generate_executive_summary,
    generate_recommendations,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(BASE_DIR, "Dataset", "bank-full.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
FRONTEND_PUBLIC = os.path.join(BASE_DIR, "frontend", "public")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(FRONTEND_PUBLIC, exist_ok=True)

df = load_data(DATASET_PATH)
df = clean_data(df)

save_cleaned_data(
    df,
    os.path.join(OUTPUT_DIR, "cleaned_data.csv"),
)

analysis = {
    "kpis": calculate_kpis(df),

    "charts": {
        "conversion_distribution": conversion_distribution(df),

        "contact": conversion_rate_by_column(df, "contact"),
        "job": conversion_rate_by_column(df, "job"),
        "month": conversion_rate_by_column(df, "month"),
        "education": conversion_rate_by_column(df, "education"),

        "campaign_volume": campaign_volume_by_column(df, "contact"),
    },

    "executive_summary": generate_executive_summary(),

    "recommendations": generate_recommendations(),

    "dataset_preview": df.head(10).to_dict(orient="records"),
}

json_path = os.path.join(FRONTEND_PUBLIC, "analysis.json")

with open(json_path, "w") as f:
    json.dump(analysis, f, indent=4)

print("✅ Analysis completed successfully!")
print(f"JSON Output : {json_path}")