from utils import calculate_percentage, round_value, to_records


def calculate_kpis(df):
    total_contacts = len(df)
    converted_customers = int(df["converted"].sum())
    non_converted = total_contacts - converted_customers

    conversion_rate = calculate_percentage(converted_customers, total_contacts)

    avg_duration = round_value(df["duration"].mean())
    avg_campaigns = round_value(df["campaign"].mean())
    avg_balance = round_value(df["balance"].mean())

    return {
        "total_contacts": total_contacts,
        "converted_customers": converted_customers,
        "non_converted": non_converted,
        "conversion_rate": conversion_rate,
        "dropoff_rate": round_value(100 - conversion_rate),
        "average_call_duration": avg_duration,
        "average_campaigns": avg_campaigns,
        "average_balance": avg_balance,
    }


def conversion_distribution(df):
    result = df["y"].value_counts().reset_index()
    result.columns = ["status", "count"]
    return to_records(result)


def conversion_rate_by_column(df, column):
    result = (
        df.groupby(column, observed=True)["converted"]
        .mean()
        .reset_index(name="conversion_rate")
    )

    result["conversion_rate"] = (result["conversion_rate"] * 100).round(2)

    return to_records(result)


def campaign_volume_by_column(df, column):
    result = (
        df.groupby(column, observed=True)
        .size()
        .reset_index(name="contacts")
    )

    return to_records(result)


def generate_executive_summary():
    return [
        "Marketing funnel analysis helps identify where potential customers are lost before conversion.",
        "Campaign conversion performance varies across customer segments, contact methods, and time periods.",
        "Optimizing high-performing channels can improve lead quality and reduce wasted marketing effort.",
        "Customer engagement indicators such as call duration and previous campaign outcome influence conversion performance.",
        "Conversion-focused recommendations can help sales and marketing teams improve revenue outcomes.",
    ]


def generate_recommendations():
    return [
        "Prioritize channels and customer segments with higher conversion rates.",
        "Reduce repeated outreach to low-performing segments to improve campaign efficiency.",
        "Improve follow-up strategy for customers with previous positive campaign outcomes.",
        "Analyze low-conversion months and adjust campaign timing accordingly.",
        "Focus marketing resources on segments that show both high contact volume and strong conversion potential.",
    ]