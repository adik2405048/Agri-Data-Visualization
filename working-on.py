import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
# Set the layout to wide and provide a title for the browser tab.
st.set_page_config(layout="wide", page_title="Agri Data Dashboard")

# --- Embedded Data ---
# The same data from your HTML file is loaded into a Pandas DataFrame for easy manipulation.
agri_data = [
    { 'Year': 2022, 'Division': 'Dhaka', 'Crop': 'Boro Rice', 'Production (Tonnes)': 4500000 },
    { 'Year': 2022, 'Division': 'Dhaka', 'Crop': 'Aman Rice', 'Production (Tonnes)': 2800000 },
    { 'Year': 2022, 'Division': 'Dhaka', 'Crop': 'Wheat', 'Production (Tonnes)': 350000 },
    { 'Year': 2022, 'Division': 'Dhaka', 'Crop': 'Jute', 'Production (Tonnes)': 800000 },
    { 'Year': 2022, 'Division': 'Dhaka', 'Crop': 'Potato', 'Production (Tonnes)': 2500000 },
    { 'Year': 2022, 'Division': 'Chattogram', 'Crop': 'Boro Rice', 'Production (Tonnes)': 3800000 },
    { 'Year': 2022, 'Division': 'Chattogram', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3200000 },
    { 'Year': 2022, 'Division': 'Chattogram', 'Crop': 'Wheat', 'Production (Tonnes)': 150000 },
    { 'Year': 2022, 'Division': 'Chattogram', 'Crop': 'Jute', 'Production (Tonnes)': 400000 },
    { 'Year': 2022, 'Division': 'Chattogram', 'Crop': 'Potato', 'Production (Tonnes)': 1800000 },
    { 'Year': 2022, 'Division': 'Rajshahi', 'Crop': 'Boro Rice', 'Production (Tonnes)': 5200000 },
    { 'Year': 2022, 'Division': 'Rajshahi', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3500000 },
    { 'Year': 2022, 'Division': 'Rajshahi', 'Crop': 'Wheat', 'Production (Tonnes)': 600000 },
    { 'Year': 2022, 'Division': 'Rajshahi', 'Crop': 'Jute', 'Production (Tonnes)': 950000 },
    { 'Year': 2022, 'Division': 'Rajshahi', 'Crop': 'Potato', 'Production (Tonnes)': 3000000 },
    { 'Year': 2022, 'Division': 'Rangpur', 'Crop': 'Boro Rice', 'Production (Tonnes)': 4800000 },
    { 'Year': 2022, 'Division': 'Rangpur', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3100000 },
    { 'Year': 2022, 'Division': 'Rangpur', 'Crop': 'Wheat', 'Production (Tonnes)': 550000 },
    { 'Year': 2022, 'Division': 'Rangpur', 'Crop': 'Jute', 'Production (Tonnes)': 1200000 },
    { 'Year': 2022, 'Division': 'Rangpur', 'Crop': 'Potato', 'Production (Tonnes)': 3500000 },
    { 'Year': 2021, 'Division': 'Dhaka', 'Crop': 'Boro Rice', 'Production (Tonnes)': 4300000 },
    { 'Year': 2021, 'Division': 'Dhaka', 'Crop': 'Aman Rice', 'Production (Tonnes)': 2750000 },
    { 'Year': 2021, 'Division': 'Dhaka', 'Crop': 'Wheat', 'Production (Tonnes)': 330000 },
    { 'Year': 2021, 'Division': 'Dhaka', 'Crop': 'Jute', 'Production (Tonnes)': 780000 },
    { 'Year': 2021, 'Division': 'Dhaka', 'Crop': 'Potato', 'Production (Tonnes)': 2400000 },
    { 'Year': 2021, 'Division': 'Chattogram', 'Crop': 'Boro Rice', 'Production (Tonnes)': 3700000 },
    { 'Year': 2021, 'Division': 'Chattogram', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3100000 },
    { 'Year': 2021, 'Division': 'Chattogram', 'Crop': 'Wheat', 'Production (Tonnes)': 140000 },
    { 'Year': 2021, 'Division': 'Chattogram', 'Crop': 'Jute', 'Production (Tonnes)': 390000 },
    { 'Year': 2021, 'Division': 'Chattogram', 'Crop': 'Potato', 'Production (Tonnes)': 1750000 },
    { 'Year': 2021, 'Division': 'Rajshahi', 'Crop': 'Boro Rice', 'Production (Tonnes)': 5100000 },
    { 'Year': 2021, 'Division': 'Rajshahi', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3400000 },
    { 'Year': 2021, 'Division': 'Rajshahi', 'Crop': 'Wheat', 'Production (Tonnes)': 580000 },
    { 'Year': 2021, 'Division': 'Rajshahi', 'Crop': 'Jute', 'Production (Tonnes)': 930000 },
    { 'Year': 2021, 'Division': 'Rajshahi', 'Crop': 'Potato', 'Production (Tonnes)': 2900000 },
    { 'Year': 2021, 'Division': 'Rangpur', 'Crop': 'Boro Rice', 'Production (Tonnes)': 4700000 },
    { 'Year': 2021, 'Division': 'Rangpur', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3000000 },
    { 'Year': 2021, 'Division': 'Rangpur', 'Crop': 'Wheat', 'Production (Tonnes)': 530000 },
    { 'Year': 2021, 'Division': 'Rangpur', 'Crop': 'Jute', 'Production (Tonnes)': 1150000 },
    { 'Year': 2021, 'Division': 'Rangpur', 'Crop': 'Potato', 'Production (Tonnes)': 3400000 },
    { 'Year': 2020, 'Division': 'Dhaka', 'Crop': 'Boro Rice', 'Production (Tonnes)': 4400000 },
    { 'Year': 2020, 'Division': 'Dhaka', 'Crop': 'Aman Rice', 'Production (Tonnes)': 2850000 },
    { 'Year': 2020, 'Division': 'Dhaka', 'Crop': 'Wheat', 'Production (Tonnes)': 340000 },
    { 'Year': 2020, 'Division': 'Dhaka', 'Crop': 'Jute', 'Production (Tonnes)': 820000 },
    { 'Year': 2020, 'Division': 'Dhaka', 'Crop': 'Potato', 'Production (Tonnes)': 2450000 },
    { 'Year': 2020, 'Division': 'Chattogram', 'Crop': 'Boro Rice', 'Production (Tonnes)': 3750000 },
    { 'Year': 2020, 'Division': 'Chattogram', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3150000 },
    { 'Year': 2020, 'Division': 'Chattogram', 'Crop': 'Wheat', 'Production (Tonnes)': 145000 },
    { 'Year': 2020, 'Division': 'Chattogram', 'Crop': 'Jute', 'Production (Tonnes)': 410000 },
    { 'Year': 2020, 'Division': 'Chattogram', 'Crop': 'Potato', 'Production (Tonnes)': 1850000 },
    { 'Year': 2020, 'Division': 'Rajshahi', 'Crop': 'Boro Rice', 'Production (Tonnes)': 5150000 },
    { 'Year': 2020, 'Division': 'Rajshahi', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3450000 },
    { 'Year': 2020, 'Division': 'Rajshahi', 'Crop': 'Wheat', 'Production (Tonnes)': 590000 },
    { 'Year': 2020, 'Division': 'Rajshahi', 'Crop': 'Jute', 'Production (Tonnes)': 940000 },
    { 'Year': 2020, 'Division': 'Rajshahi', 'Crop': 'Potato', 'Production (Tonnes)': 2950000 },
    { 'Year': 2020, 'Division': 'Rangpur', 'Crop': 'Boro Rice', 'Production (Tonnes)': 4750000 },
    { 'Year': 2020, 'Division': 'Rangpur', 'Crop': 'Aman Rice', 'Production (Tonnes)': 3050000 },
    { 'Year': 2020, 'Division': 'Rangpur', 'Crop': 'Wheat', 'Production (Tonnes)': 540000 },
    { 'Year': 2020, 'Division': 'Rangpur', 'Crop': 'Jute', 'Production (Tonnes)': 1180000 },
    { 'Year': 2020, 'Division': 'Rangpur', 'Crop': 'Potato', 'Production (Tonnes)': 3450000 }
]
df = pd.DataFrame(agri_data)

# --- Sidebar Filters ---
st.sidebar.header("Dashboard Filters")

# Get unique values for filters from the DataFrame
all_years = sorted(df['Year'].unique(), reverse=True)
all_crops = sorted(df['Crop'].unique())
all_divisions = sorted(df['Division'].unique())

# Create multiselect widgets in the sidebar
selected_years = st.sidebar.multiselect("Select Year(s)", all_years, default=[all_years[0]])
selected_crops = st.sidebar.multiselect("Select Crop(s)", all_crops, default=['Boro Rice', 'Potato', 'Jute'])
selected_divisions = st.sidebar.multiselect("Select Division(s)", all_divisions, default=all_divisions)

st.sidebar.info("This dashboard visualizes agricultural production data based on BBS statistics.")

# --- Main Content ---
st.title("🌾 Agri Data Visualization Dashboard")
st.markdown("An interactive tool to analyze crop production statistics in Bangladesh.")

# --- Filtering Data based on sidebar selections ---
filtered_df = df[
    df['Year'].isin(selected_years) &
    df['Crop'].isin(selected_crops) &
    df['Division'].isin(selected_divisions)
]

# --- Display Content ---
if filtered_df.empty:
    st.warning("No data available for the selected filters. Please adjust your selections in the sidebar.")
else:
    # --- Key Metrics ---
    total_production = filtered_df['Production (Tonnes)'].sum()
    avg_production = filtered_df['Production (Tonnes)'].mean()
    num_records = len(filtered_df)

    # Display metrics in columns
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Production (Tonnes)", f"{total_production:,.0f}")
    col2.metric("Average Production (Tonnes)", f"{avg_production:,.0f}")
    col3.metric("Number of Records", f"{num_records}")
    
    st.markdown("---")

    # --- Visualizations ---
    # Bar Chart: Crop Production by Division
    st.subheader("Crop Production by Division")
    fig_bar = px.bar(
        filtered_df.groupby(['Division', 'Crop'])['Production (Tonnes)'].sum().reset_index(),
        x='Division',
        y='Production (Tonnes)',
        color='Crop',
        barmode='group',
        title=f"<b>Production for {', '.join(map(str, selected_years))}</b>"
    )
    fig_bar.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.3))
    st.plotly_chart(fig_bar, use_container_width=True)

    # Create two columns for pie and line charts
    col1, col2 = st.columns(2)

    with col1:
        # Pie Chart: Share of Each Crop
        st.subheader("Share of Each Crop")
        pie_df = filtered_df.groupby('Crop')['Production (Tonnes)'].sum().reset_index()
        fig_pie = px.pie(
            pie_df,
            names='Crop',
            values='Production (Tonnes)',
            title='<b>Share in Total Production</b>',
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        # Line Chart: Annual Production Trend
        st.subheader("Annual Production Trend")
        # Filter original dataframe for trend line to show historical data
        line_df = df[df['Crop'].isin(selected_crops) & df['Division'].isin(selected_divisions)]
        trend_df = line_df.groupby(['Year', 'Crop'])['Production (Tonnes)'].sum().reset_index()
        
        fig_line = px.line(
            trend_df,
            x='Year',
            y='Production (Tonnes)',
            color='Crop',
            markers=True,
            title='<b>Production Trend Over Years</b>'
        )
        fig_line.update_xaxes(type='category') # Treat years as distinct categories
        st.plotly_chart(fig_line, use_container_width=True)

