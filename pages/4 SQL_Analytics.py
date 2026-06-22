import streamlit as st

from sql_queries.query_collection import *

st.title("🗄 SQL Analytics Dashboard")

query_choice = st.selectbox(
    "Choose Query",
    [
    "Q1 - Find all players who represent India",
    "Q2 - Show all cricket matches played in the recent",
    "Q3 - List the top 10 highest run scorers in ODI cricket",
    "Q4 - Display cricket venues with a capacity > 25,000",
    "Q5 - Calculate how many matches each team has won",
    "Q6 - Count how many players belong to each playing role",
    "Q7 - Find the highest individual batting score in each cricket format",
    "Q8 - Show all cricket series that started in the year 2024",
    "Q9 - Find all-rounders with > 1000 runs AND > 50 wickets",
    "Q10 - Get details of the last 20 completed matches",
    "Q11 - Compare each player's performance across different cricket formats",
    "Q12 - Analyze each international team's performance playing at home versus away",
    "Q13 - Identify batting partnerships where consecutive batsmen scored >= 100 runs",
    "Q14 - Examine bowling performance at different venues",
    "Q15 - Identify players who perform exceptionally well in close matches",
    "Q16 - Track how players' batting performance changes over different years",
    "Q17 - Investigate whether winning the toss gives teams an advantage",
    "Q18 - Find the most economical bowlers in limited-overs cricket",
    "Q19 - Determine which batsmen are most consistent in their scoring",
    "Q20 - Analyze format appearance matrices and individual batting averages",
    "Q21 - Comprehensive Performance Ranking System for Players",
    "Q22 - Complete Head-to-Head Match Prediction Analysis",
    "Q23 - Analyze recent player form and momentum",
    "Q24 - Study successful batting partnerships to identify best player combinations",
    "Q25 - Time-Series Analysis of Player Performance Evolution"
    ]
)

if query_choice == "Q1 - Find all players who represent India":
    st.dataframe(execute_query(QUERY_1))

elif query_choice == "Q2 - Show all cricket matches played in the recent":
    st.dataframe(execute_query(QUERY_2))

elif query_choice == "Q3 - List the top 10 highest run scorers in ODI cricket":
    st.dataframe(execute_query(QUERY_3))

elif query_choice == "Q4 - Display cricket venues with a capacity > 25,000":
    st.dataframe(execute_query(QUERY_4))

elif query_choice == "Q5 - Calculate how many matches each team has won":
    st.dataframe(execute_query(QUERY_5))

elif query_choice == "Q6 - Count how many players belong to each playing role":
    st.dataframe(execute_query(QUERY_6))

elif query_choice == "Q7 - Find the highest individual batting score in each cricket format":
    st.dataframe(execute_query(QUERY_7))

elif query_choice == "Q8 - Show all cricket series that started in the year 2024":
    st.dataframe(execute_query(QUERY_8))

elif query_choice == "Q9 - Find all-rounders with > 1000 runs AND > 50 wickets":
    st.dataframe(execute_query(QUERY_9))

elif query_choice == "Q10 - Get details of the last 20 completed matches":
    st.dataframe(execute_query(QUERY_10))

elif query_choice == "Q11 - Compare each player's performance across different cricket formats":
    st.dataframe(execute_query(QUERY_11))

elif query_choice == "Q12 - Analyze each international team's performance playing at home versus away":
    st.dataframe(execute_query(QUERY_12))

elif query_choice == "Q13 - Identify batting partnerships where consecutive batsmen scored >= 100 runs":
    st.dataframe(execute_query(QUERY_13))

elif query_choice == "Q14 - Examine bowling performance at different venues":
    st.dataframe(execute_query(QUERY_14))

elif query_choice == "Q15 - Identify players who perform exceptionally well in close matches":
    st.dataframe(execute_query(QUERY_15))

elif query_choice == "Q16 - Track how players' batting performance changes over different years":
    st.dataframe(execute_query(QUERY_16))

elif query_choice == "Q17 - Investigate whether winning the toss gives teams an advantage":
    st.dataframe(execute_query(QUERY_17))

elif query_choice == "Q18 - Find the most economical bowlers in limited-overs cricket":
    st.dataframe(execute_query(QUERY_18))

elif query_choice == "Q19 - Determine which batsmen are most consistent in their scoring":
    st.dataframe(execute_query(QUERY_19))

elif query_choice == "Q20 - Analyze format appearance matrices and individual batting averages":
    st.dataframe(execute_query(QUERY_20))

elif query_choice == "Q21 - Comprehensive Performance Ranking System for Players":
    st.dataframe(execute_query(QUERY_21))

elif query_choice == "Q22 - Complete Head-to-Head Match Prediction Analysis":
    st.dataframe(execute_query(QUERY_22))

elif query_choice == "Q23 - Analyze recent player form and momentum":
    st.dataframe(execute_query(QUERY_23))

elif query_choice == "Q24 - Study successful batting partnerships to identify best player combinations":
    st.dataframe(execute_query(QUERY_24))

elif query_choice == "Q25 - Time-Series Analysis of Player Performance Evolution":
    st.dataframe(execute_query(QUERY_25))