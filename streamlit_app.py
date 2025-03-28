import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import time

# Set page configuration
st.set_page_config(
    page_title="Swar - Standup Show Organizer",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FF4B4B;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .card {
        border-radius: 10px;
        padding: 20px;
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .metric-card {
        background-color: #1E88E5;
        color: white;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content {
        background-color: #2E3B4E;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #E03E3E;
        transform: scale(1.05);
    }
    .stProgress > div > div > div > div {
        background-color: #1E88E5;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'comedians' not in st.session_state:
    st.session_state.comedians = [
        {"name": "Dave Chappelle", "rating": 4.9, "fee": 15000, "specialty": "Social commentary"},
        {"name": "Ali Wong", "rating": 4.7, "fee": 10000, "specialty": "Family life"},
        {"name": "John Mulaney", "rating": 4.8, "fee": 12000, "specialty": "Observational"},
        {"name": "Hannah Gadsby", "rating": 4.6, "fee": 8000, "specialty": "Storytelling"},
        {"name": "Kevin Hart", "rating": 4.7, "fee": 20000, "specialty": "Self-deprecating"}
    ]

if 'shows' not in st.session_state:
    st.session_state.shows = [
        {"title": "Comedy Night", "date": datetime.now() + timedelta(days=7), "venue": "Laugh Factory", "capacity": 200, "tickets_sold": 150, "comedians": ["Dave Chappelle", "Ali Wong"]},
        {"title": "Stand Up Special", "date": datetime.now() + timedelta(days=14), "venue": "Comedy Store", "capacity": 300, "tickets_sold": 200, "comedians": ["John Mulaney", "Kevin Hart"]},
        {"title": "Comedy Jam", "date": datetime.now() + timedelta(days=21), "venue": "Improv", "capacity": 250, "tickets_sold": 100, "comedians": ["Hannah Gadsby", "Ali Wong"]}
    ]

if 'venues' not in st.session_state:
    st.session_state.venues = [
        {"name": "Laugh Factory", "capacity": 200, "rental_fee": 2000},
        {"name": "Comedy Store", "capacity": 300, "rental_fee": 3000},
        {"name": "Improv", "capacity": 250, "rental_fee": 2500},
        {"name": "Stand Up NY", "capacity": 150, "rental_fee": 1500},
        {"name": "Comedy Cellar", "capacity": 120, "rental_fee": 1200}
    ]

if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# Sidebar navigation
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>🎭 StandUp Pro</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Add a loading animation for page transitions
def change_page(page):
    with st.spinner(f"Loading {page}..."):
        time.sleep(0.5)  # Simulate loading
        st.session_state.page = page
        st.experimental_rerun()

# Navigation buttons with icons
st.sidebar.button("📊 Dashboard", on_click=change_page, args=["Dashboard"])
st.sidebar.button("🎤 Comedians", on_click=change_page, args=["Comedians"])
st.sidebar.button("🗓️ Shows", on_click=change_page, args=["Shows"])
st.sidebar.button("🏢 Venues", on_click=change_page, args=["Venues"])
st.sidebar.button("📈 Analytics", on_click=change_page, args=["Analytics"])

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='text-align: center; color: #AAAAAA; font-size: 0.8rem;'>© 2025 StandUp Pro</div>", unsafe_allow_html=True)

# Dashboard Page
if st.session_state.page == "Dashboard":
    st.markdown("<h1 class='main-header'>Dashboard</h1>", unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("<div class='metric-card'><h2>5</h2><p>Comedians</p></div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-card'><h2>3</h2><p>Upcoming Shows</p></div>", unsafe_allow_html=True)
    
    with col3:
        total_tickets = sum(show["tickets_sold"] for show in st.session_state.shows)
        st.markdown(f"<div class='metric-card'><h2>{total_tickets}</h2><p>Tickets Sold</p></div>", unsafe_allow_html=True)
    
    with col4:
        total_capacity = sum(show["capacity"] for show in st.session_state.shows)
        occupancy_rate = int((total_tickets / total_capacity) * 100)
        st.markdown(f"<div class='metric-card'><h2>{occupancy_rate}%</h2><p>Occupancy Rate</p></div>", unsafe_allow_html=True)
    
    # Upcoming shows
    st.markdown("<h2 class='sub-header'>Upcoming Shows</h2>", unsafe_allow_html=True)
    
    for show in st.session_state.shows:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"<div class='card'><h3>{show['title']}</h3><p>Date: {show['date'].strftime('%B %d, %Y')}</p><p>Venue: {show['venue']}</p></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='card'><h4>Comedians</h4><p>{', '.join(show['comedians'])}</p></div>", unsafe_allow_html=True)
        with col3:
            progress = int((show['tickets_sold'] / show['capacity']) * 100)
            st.markdown(f"<div class='card'><h4>Ticket Sales</h4><p>{show['tickets_sold']} / {show['capacity']}</p></div>", unsafe_allow_html=True)
            st.progress(progress / 100)
    
    # Quick actions
    st.markdown("<h2 class='sub-header'>Quick Actions</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Add New Show"):
            change_page("Shows")
    
    with col2:
        if st.button("Manage Comedians"):
            change_page("Comedians")
    
    with col3:
        if st.button("View Analytics"):
            change_page("Analytics")

# Comedians Page
elif st.session_state.page == "Comedians":
    st.markdown("<h1 class='main-header'>Comedians</h1>", unsafe_allow_html=True)
    
    # Add new comedian form
    with st.expander("Add New Comedian"):
        with st.form("add_comedian"):
            name = st.text_input("Name")
            rating = st.slider("Rating", 1.0, 5.0, 4.0, 0.1)
            fee = st.number_input("Fee ($)", min_value=500, max_value=50000, value=5000, step=500)
            specialty = st.text_input("Specialty")
            
            submitted = st.form_submit_button("Add Comedian")
            if submitted and name:
                st.session_state.comedians.append({
                    "name": name,
                    "rating": rating,
                    "fee": fee,
                    "specialty": specialty
                })
                st.success(f"Added {name} to the roster!")
                time.sleep(1)
                st.experimental_rerun()
    
    # Display comedians
    st.markdown("<h2 class='sub-header'>Comedian Roster</h2>", unsafe_allow_html=True)
    
    # Search and filter
    search = st.text_input("Search comedians")
    
    filtered_comedians = st.session_state.comedians
    if search:
        filtered_comedians = [c for c in st.session_state.comedians if search.lower() in c["name"].lower()]
    
    # Display comedians in a grid
    cols = st.columns(3)
    for i, comedian in enumerate(filtered_comedians):
        with cols[i % 3]:
            st.markdown(f"""
            <div class='card'>
                <h3>{comedian['name']}</h3>
                <p>Rating: {'⭐' * int(comedian['rating'])} ({comedian['rating']})</p>
                <p>Fee: ${comedian['fee']:,}</p>
                <p>Specialty: {comedian['specialty']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Actions
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Edit {comedian['name']}", key=f"edit_{i}"):
                    st.session_state.edit_comedian = i
            with col2:
                if st.button(f"Delete {comedian['name']}", key=f"delete_{i}"):
                    st.session_state.comedians.pop(i)
                    st.success(f"Removed {comedian['name']} from the roster!")
                    time.sleep(1)
                    st.experimental_rerun()
    
    # Edit comedian (if edit button was clicked)
    if 'edit_comedian' in st.session_state:
        i = st.session_state.edit_comedian
        comedian = st.session_state.comedians[i]
        
        st.markdown("<h2 class='sub-header'>Edit Comedian</h2>", unsafe_allow_html=True)
        
        with st.form("edit_comedian"):
            name = st.text_input("Name", value=comedian["name"])
            rating = st.slider("Rating", 1.0, 5.0, comedian["rating"], 0.1)
            fee = st.number_input("Fee ($)", min_value=500, max_value=50000, value=comedian["fee"], step=500)
            specialty = st.text_input("Specialty", value=comedian["specialty"])
            
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("Save Changes"):
                    st.session_state.comedians[i] = {
                        "name": name,
                        "rating": rating,
                        "fee": fee,
                        "specialty": specialty
                    }
                    st.success(f"Updated {name}'s information!")
                    del st.session_state.edit_comedian
                    time.sleep(1)
                    st.experimental_rerun()
            
            with col2:
                if st.form_submit_button("Cancel"):
                    del st.session_state.edit_comedian
                    st.experimental_rerun()

# Shows Page
elif st.session_state.page == "Shows":
    st.markdown("<h1 class='main-header'>Shows</h1>", unsafe_allow_html=True)
    
    # Add new show form
    with st.expander("Schedule New Show"):
        with st.form("add_show"):
            title = st.text_input("Show Title")
            date = st.date_input("Date", value=datetime.now() + timedelta(days=7))
            time = st.time_input("Time", value=datetime.now().replace(hour=20, minute=0))
            venue = st.selectbox("Venue", [v["name"] for v in st.session_state.venues])
            
            # Get capacity based on selected venue
            capacity = next((v["capacity"] for v in st.session_state.venues if v["name"] == venue), 0)
            
            comedians = st.multiselect("Select Comedians", [c["name"] for c in st.session_state.comedians])
            
            submitted = st.form_submit_button("Schedule Show")
            if submitted and title and venue and comedians:
                # Combine date and time
                show_datetime = datetime.combine(date, time)
                
                st.session_state.shows.append({
                    "title": title,
                    "date": show_datetime,
                    "venue": venue,
                    "capacity": capacity,
                    "tickets_sold": 0,
                    "comedians": comedians
                })
                st.success(f"Scheduled '{title}' at {venue}!")
                time.sleep(1)
                st.experimental_rerun()
    
    # Display shows
    st.markdown("<h2 class='sub-header'>Upcoming Shows</h2>", unsafe_allow_html=True)
    
    # Sort shows by date
    sorted_shows = sorted(st.session_state.shows, key=lambda x: x["date"])
    
    for i, show in enumerate(sorted_shows):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
            <div class='card'>
                <h3>{show['title']}</h3>
                <p>Date: {show['date'].strftime('%B %d, %Y at %I:%M %p')}</p>
                <p>Venue: {show['venue']} (Capacity: {show['capacity']})</p>
                <p>Comedians: {', '.join(show['comedians'])}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='card'>
                <h4>Ticket Sales</h4>
                <p>{show['tickets_sold']} / {show['capacity']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Progress bar for ticket sales
            progress = int((show['tickets_sold'] / show['capacity']) * 100)
            st.progress(progress / 100)
            
            # Actions
            if st.button(f"Sell Tickets", key=f"sell_{i}"):
                # Simulate selling tickets
                additional_tickets = min(random.randint(5, 20), show['capacity'] - show['tickets_sold'])
                st.session_state.shows[i]['tickets_sold'] += additional_tickets
                st.success(f"Sold {additional_tickets} more tickets!")
                time.sleep(1)
                st.experimental_rerun()
            
            if st.button(f"Cancel Show", key=f"cancel_{i}"):
                st.session_state.shows.pop(i)
                st.success(f"Cancelled '{show['title']}'")
                time.sleep(1)
                st.experimental_rerun()

# Venues Page
elif st.session_state.page == "Venues":
    st.markdown("<h1 class='main-header'>Venues</h1>", unsafe_allow_html=True)
    
    # Add new venue form
    with st.expander("Add New Venue"):
        with st.form("add_venue"):
            name = st.text_input("Venue Name")
            capacity = st.number_input("Capacity", min_value=50, max_value=1000, value=200, step=10)
            rental_fee = st.number_input("Rental Fee ($)", min_value=500, max_value=10000, value=2000, step=100)
            
            submitted = st.form_submit_button("Add Venue")
            if submitted and name:
                st.session_state.venues.append({
                    "name": name,
                    "capacity": capacity,
                    "rental_fee": rental_fee
                })
                st.success(f"Added {name} to venues!")
                time.sleep(1)
                st.experimental_rerun()
    
    # Display venues
    st.markdown("<h2 class='sub-header'>Available Venues</h2>", unsafe_allow_html=True)
    
    # Create a DataFrame for better display
    venues_df = pd.DataFrame(st.session_state.venues)
    
    # Add a column for cost per seat
    venues_df["Cost per Seat"] = venues_df["rental_fee"] / venues_df["capacity"]
    
    # Format the DataFrame
    venues_df.columns = ["Name", "Capacity", "Rental Fee ($)", "Cost per Seat ($)"]
    venues_df["Rental Fee ($)"] = venues_df["Rental Fee ($)"].apply(lambda x: f"${x:,.2f}")
    venues_df["Cost per Seat ($)"] = venues_df["Cost per Seat ($)"].apply(lambda x: f"${x:.2f}")
    
    # Display as a table
    st.dataframe(venues_df, use_container_width=True)
    
    # Venue comparison chart
    st.markdown("<h2 class='sub-header'>Venue Comparison</h2>", unsafe_allow_html=True)
    
    fig = px.bar(
        st.session_state.venues,
        x="name",
        y="capacity",
        color="rental_fee",
        labels={"name": "Venue", "capacity": "Capacity", "rental_fee": "Rental Fee ($)"},
        title="Venue Capacity and Rental Fees",
        color_continuous_scale="Viridis"
    )
    
    fig.update_layout(
        xaxis_title="Venue",
        yaxis_title="Capacity",
        coloraxis_colorbar_title="Rental Fee ($)"
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Analytics Page
elif st.session_state.page == "Analytics":
    st.markdown("<h1 class='main-header'>Analytics</h1>", unsafe_allow_html=True)
    
    # Create DataFrames for analysis
    shows_df = pd.DataFrame([
        {
            "title": show["title"],
            "date": show["date"],
            "venue": show["venue"],
            "capacity": show["capacity"],
            "tickets_sold": show["tickets_sold"],
            "occupancy_rate": (show["tickets_sold"] / show["capacity"]) * 100,
            "revenue": show["tickets_sold"] * 25  # Assuming $25 per ticket
        }
        for show in st.session_state.shows
    ])
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = shows_df["revenue"].sum()
        st.markdown(f"<div class='metric-card'><h2>${total_revenue:,.2f}</h2><p>Total Revenue</p></div>", unsafe_allow_html=True)
    
    with col2:
        avg_occupancy = shows_df["occupancy_rate"].mean()
        st.markdown(f"<div class='metric-card'><h2>{avg_occupancy:.1f}%</h2><p>Avg. Occupancy</p></div>", unsafe_allow_html=True)
    
    with col3:
        total_shows = len(shows_df)
        st.markdown(f"<div class='metric-card'><h2>{total_shows}</h2><p>Total Shows</p></div>", unsafe_allow_html=True)
    
    with col4:
        total_tickets = shows_df["tickets_sold"].sum()
        st.markdown(f"<div class='metric-card'><h2>{total_tickets}</h2><p>Tickets Sold</p></div>", unsafe_allow_html=True)
    
    # Revenue by show
    st.markdown("<h2 class='sub-header'>Revenue by Show</h2>", unsafe_allow_html=True)
    
    fig = px.bar(
        shows_df,
        x="title",
        y="revenue",
        color="occupancy_rate",
        labels={"title": "Show", "revenue": "Revenue ($)", "occupancy_rate": "Occupancy Rate (%)"},
        title="Revenue by Show",
        color_continuous_scale="RdYlGn"
    )
    
    fig.update_layout(
        xaxis_title="Show",
        yaxis_title="Revenue ($)",
        coloraxis_colorbar_title="Occupancy (%)"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Occupancy rates
    st.markdown("<h2 class='sub-header'>Occupancy Rates</h2>", unsafe_allow_html=True)
    
    fig = go.Figure()
    
    for show in st.session_state.shows:
        occupancy = (show["tickets_sold"] / show["capacity"]) * 100
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=occupancy,
            title={"text": show["title"]},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [0, 50], "color": "red"},
                    {"range": [50, 75], "color": "yellow"},
                    {"range": [75, 100], "color": "green"}
                ],
                "threshold": {
                    "line": {"color": "black", "width": 4},
                    "thickness": 0.75,
                    "value": 90
                }
            },
            domain={"row": 0, "column": i}
        ))
    
    fig.update_layout(
        grid={"rows": 1, "columns": len(st.session_state.shows)},
        height=250
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Comedian popularity
    st.markdown("<h2 class='sub-header'>Comedian Popularity</h2>", unsafe_allow_html=True)
    
    # Count shows per comedian
    comedian_counts = {}
    for show in st.session_state.shows:
        for comedian in show["comedians"]:
            if comedian in comedian_counts:
                comedian_counts[comedian] += 1
            else:
                comedian_counts[comedian] = 1
    
    # Create DataFrame
    comedian_df = pd.DataFrame([
        {"name": name, "shows": count}
        for name, count in comedian_counts.items()
    ])
    
    if not comedian_df.empty:
        fig = px.pie(
            comedian_df,
            values="shows",
            names="name",
            title="Shows per Comedian",
            hole=0.4
        )
        
        fig.update_traces(textposition="inside", textinfo="percent+label")
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for comedian popularity chart.")
    
    # Revenue forecast
    st.markdown("<h2 class='sub-header'>Revenue Forecast</h2>", unsafe_allow_html=True)
    
    # Generate forecast data (simulated)
    forecast_dates = [datetime.now() + timedelta(days=i*7) for i in range(8)]
    forecast_revenue = [random.randint(5000, 15000) for _ in range(8)]
    
    forecast_df = pd.DataFrame({
        "date": forecast_dates,
        "revenue": forecast_revenue,
        "type": ["Actual" if i < 3 else "Forecast" for i in range(8)]
    })
    
    fig = px.line(
        forecast_df,
        x="date",
        y="revenue",
        color="type",
        labels={"date": "Date", "revenue": "Revenue ($)", "type": "Type"},
        title="Revenue Forecast (Next 8 Weeks)",
        markers=True
    )
    
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Revenue ($)"
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Add a footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #AAAAAA; font-size: 0.8rem;'>© 2025 StandUp Pro | Developed with Streamlit</div>", unsafe_allow_html=True)
