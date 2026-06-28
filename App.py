import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Marketing Funnel Intelligence",
    page_icon="📈",
    layout="wide",
)

@st.cache_data
def load_data():
    df = pd.read_csv("Dataset/bank-full.csv", sep=";")
    df["converted"] = df["y"].map({"yes": 1, "no": 0})
    return df

df = load_data()

total_contacts = len(df)
converted = int(df["converted"].sum())
not_converted = total_contacts - converted
conversion_rate = round((converted / total_contacts) * 100, 2)
dropoff_rate = round(100 - conversion_rate, 2)
avg_duration = round(df["duration"].mean(), 2)

st.title("Marketing Funnel Intelligence")
st.caption("Marketing Funnel & Conversion Performance Analysis")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Contacts", f"{total_contacts:,}")
col2.metric("Converted Customers", f"{converted:,}")
col3.metric("Conversion Rate", f"{conversion_rate}%")
col4.metric("Drop-off Rate", f"{dropoff_rate}%")

st.markdown("---")

st.subheader("Funnel Overview")

funnel_df = pd.DataFrame({
    "Stage": ["Total Contacts", "Converted", "Not Converted"],
    "Count": [total_contacts, converted, not_converted]
})

fig_funnel = px.funnel(
    funnel_df,
    x="Count",
    y="Stage",
    title="Marketing Funnel Drop-off"
)

st.plotly_chart(fig_funnel, use_container_width=True)

st.markdown("---")

left, right = st.columns(2)

with left:
    st.subheader("Conversion by Contact Type")
    contact_rate = (
        df.groupby("contact")["converted"]
        .mean()
        .reset_index()
    )
    contact_rate["conversion_rate"] = contact_rate["converted"] * 100

    fig_contact = px.bar(
        contact_rate,
        x="contact",
        y="conversion_rate",
        title="Contact Channel Conversion Rate",
        text=contact_rate["conversion_rate"].round(2),
    )
    st.plotly_chart(fig_contact, use_container_width=True)

with right:
    st.subheader("Conversion by Month")
    month_rate = (
        df.groupby("month")["converted"]
        .mean()
        .reset_index()
    )
    month_rate["conversion_rate"] = month_rate["converted"] * 100

    fig_month = px.bar(
        month_rate,
        x="month",
        y="conversion_rate",
        title="Monthly Conversion Performance",
        text=month_rate["conversion_rate"].round(2),
    )
    st.plotly_chart(fig_month, use_container_width=True)

st.markdown("---")

left, right = st.columns(2)

with left:
    st.subheader("Conversion by Job")
    job_rate = (
        df.groupby("job")["converted"]
        .mean()
        .reset_index()
        .sort_values("converted", ascending=False)
    )
    job_rate["conversion_rate"] = job_rate["converted"] * 100

    fig_job = px.bar(
        job_rate,
        x="conversion_rate",
        y="job",
        orientation="h",
        title="Job Segment Conversion Rate",
        text=job_rate["conversion_rate"].round(2),
    )
    st.plotly_chart(fig_job, use_container_width=True)

with right:
    st.subheader("Conversion by Education")
    education_rate = (
        df.groupby("education")["converted"]
        .mean()
        .reset_index()
    )
    education_rate["conversion_rate"] = education_rate["converted"] * 100

    fig_education = px.pie(
        education_rate,
        names="education",
        values="conversion_rate",
        title="Education Segment Conversion Share"
    )
    st.plotly_chart(fig_education, use_container_width=True)

st.markdown("---")

st.subheader("Campaign Performance Insights")

insight_col1, insight_col2, insight_col3 = st.columns(3)

best_contact = contact_rate.sort_values("conversion_rate", ascending=False).iloc[0]
best_month = month_rate.sort_values("conversion_rate", ascending=False).iloc[0]
best_job = job_rate.sort_values("conversion_rate", ascending=False).iloc[0]

insight_col1.info(
    f"Best Contact Channel: {best_contact['contact']} "
    f"({best_contact['conversion_rate']:.2f}% conversion)"
)

insight_col2.success(
    f"Best Month: {best_month['month']} "
    f"({best_month['conversion_rate']:.2f}% conversion)"
)

insight_col3.warning(
    f"Best Job Segment: {best_job['job']} "
    f"({best_job['conversion_rate']:.2f}% conversion)"
)

st.markdown("---")

st.subheader("Growth Recommendations")

recommendations = [
    "Focus marketing efforts on contact channels with higher conversion rates.",
    "Optimize campaigns during months that show stronger conversion performance.",
    "Reduce repeated outreach to low-performing segments to improve efficiency.",
    "Prioritize customer groups with stronger historical conversion patterns.",
    "Use funnel drop-off insights to improve lead nurturing and follow-up strategy.",
]

for rec in recommendations:
    st.write(f"- {rec}")

st.markdown("---")

st.subheader("Dataset Preview")
st.dataframe(df.head(50), use_container_width=True)

st.markdown("---")
st.caption("Built with Python, Streamlit, Pandas, and Plotly | Future Interns DS_03")