import streamlit as st

st.set_page_config(
    page_title="Cricbuzz LiveStats Dashboard",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 Cricbuzz LiveStats Dashboard")

st.markdown("---")

st.header("📖 Project Overview")

st.write("""
Cricbuzz LiveStats Dashboard is a cricket analytics application built using
**Python, Streamlit, MySQL, SQLAlchemy, and Cricbuzz RapidAPI**.

The application provides:

✅ Live Match Tracking

✅ Player Statistics

✅ CRUD Operations on Cricket Data

✅ SQL Analytics Dashboard

This project demonstrates API Integration, Database Management,
SQL Analytics, and Interactive Dashboard Development.
""")

st.markdown("---")

st.header("🚀 Modules Available")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏏 Live Matches")

    st.write("""
    - View ongoing cricket matches
    - Match status updates
    - Venue information
    - Team details
    - Real-time data from Cricbuzz API
    """)

    st.subheader("📊 Player Statistics")

    st.write("""
    - Search players
    - Batting statistics
    - Bowling statistics
    - Player profiles
    - Cricbuzz API integration
    """)

with col2:

    st.subheader("✏ CRUD Operations")

    st.write("""
    - Add Player
    - View Players
    - Update Player
    - Delete Player
    """)

    st.subheader("🗄 SQL Analytics")

    st.write("""
    - 25 SQL analytical queries
    - Team performance analysis
    - Venue analysis
    - Toss analysis
    - Partnership analysis
    - Player ranking system
    """)

st.markdown("---")

st.header("🛠 Technology Stack")

st.write("""
**Frontend**
- Streamlit

**Backend**
- Python

**Database**
- MySQL

**Database Connector**
- SQLAlchemy

**API Source**
- Cricbuzz RapidAPI

**Libraries**
- Pandas
- Requests
""")

st.markdown("---")

st.header("📂 Database Tables")

st.code("""
players
teams
venues
series
matches
innings
partnerships
batting_stats
bowling_stats
batting_innings
bowling_innings
fielding_stats
toss_details
""")

st.markdown("---")

st.header("📈 SQL Analytics Coverage")

st.write("""
The SQL Analytics module contains:

• Beginner Level Queries (Q1–Q8)

• Intermediate Level Queries (Q9–Q16)

• Advanced Level Queries (Q17–Q25)

Topics include:

- Player Analysis
- Team Analysis
- Match Analysis
- Venue Analysis
- Toss Impact
- Head-to-Head Records
- Player Form Analysis
- Career Progression Analysis
""")

st.markdown("---")

st.header("📌 How To Use")

st.write("""
1. Open the sidebar.

2. Select **Live Matches** to view live cricket matches.

3. Select **Player Statistics** to view player records.

4. Select **SQL Analytics** to execute cricket analytics queries.

5. Select **CRUD Operations** to manage player data.

6. Explore results directly within the Streamlit dashboard.
""")

st.markdown("---")

st.success("✅ Cricbuzz LiveStats Dashboard Ready")