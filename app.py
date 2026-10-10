import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Penguin Clustering",
    page_icon="🐧",
    layout="wide"
)

# Load dataset
df = pd.read_csv("penguin_clusters (1).csv")

# Main title
st.title("🐧 Penguin Clustering Dashboard")

st.write(
    "Explore penguin measurements and discover groups "
    "identified using the K-Means clustering algorithm."
)

st.divider()

# Sidebar
st.sidebar.title("About the Project")
st.sidebar.write(
    "This project uses K-Means, an unsupervised "
    "machine learning algorithm, to group penguins "
    "based on their physical measurements."
)

st.sidebar.subheader("Features Used")
st.sidebar.write("- Culmen length")
st.sidebar.write("- Culmen depth")
st.sidebar.write("- Flipper length")
st.sidebar.write("- Body mass")

st.sidebar.info(
    "The clusters represent measurement similarities, "
    "not confirmed penguin species."
)

# Summary cards
total_penguins = len(df)
total_clusters = df["Cluster"].nunique()

col1, col2 = st.columns(2)

with col1:
    st.metric("🐧 Total Penguin Records", total_penguins)

with col2:
    st.metric("🔵 Number of Clusters", total_clusters)

st.divider()

# Dataset section
st.header("📋 Penguin Dataset")

selected_cluster = st.selectbox(
    "Filter by cluster",
    ["All Clusters"] + sorted(df["Cluster"].unique().tolist())
)

if selected_cluster == "All Clusters":
    filtered_df = df
else:
    filtered_df = df[df["Cluster"] == selected_cluster]

st.dataframe(filtered_df, use_container_width=True)

st.caption(f"Showing {len(filtered_df)} records.")

# Cluster counts
st.header("📊 Cluster Counts")

cluster_counts = (
    df["Cluster"]
    .value_counts()
    .sort_index()
    .reset_index()
)

cluster_counts.columns = ["Cluster", "Number of Penguins"]

st.bar_chart(
    cluster_counts,
    x="Cluster",
    y="Number of Penguins",
    x_label="Cluster",
    y_label="Number of Penguins",
    color="#36A2EB"
)

st.subheader("Cluster Summary")
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv_data,
    file_name="penguin_clusters_filtered.csv",
    mime="text/csv"
)

# Interactive cluster visualization
st.header("📈 Explore Penguin Clusters")

col1, col2 = st.columns(2)

with col1:
    x_feature = st.selectbox(
        "Choose X-axis",
        ["culmen_length_mm", "culmen_depth_mm",
         "flipper_length_mm", "body_mass_g"]
    )

with col2:
    y_feature = st.selectbox(
        "Choose Y-axis",
        ["flipper_length_mm", "body_mass_g",
         "culmen_length_mm", "culmen_depth_mm"]
    )

# Create interactive scatter plot
import plotly.express as px

fig = px.scatter(
    filtered_df,
    x=x_feature,
    y=y_feature,
    color="Cluster",
    hover_data=["sex"],
    title="Explore Penguin Measurements",
    labels={
        "culmen_length_mm": "Culmen Length (mm)",
        "culmen_depth_mm": "Culmen Depth (mm)",
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)",
        "sex": "Sex",
        "Cluster": "Cluster"
    }
)

st.plotly_chart(fig, use_container_width=True)