import streamlit as st
import pandas as pd

from api.cricbuzz_api import (
    search_player,
    get_player_batting,
    get_player_bowling
)

st.title("📊 Player Statistics")

player_name = st.text_input(
    "Enter Player Name",
    placeholder="Virat Kohli"
)

if player_name:

    search_results = search_player(player_name)

    player_list = search_results.get("player", [])

    if not player_list:
        st.warning("No players found.")
        st.stop()

    player_names = {
        p["name"]: p["id"]
        for p in player_list
    }

    selected_player = st.selectbox(
        "Select Player",
        list(player_names.keys())
    )

    player_id = player_names[selected_player]

    batting = get_player_batting(player_id)

    batting_df = pd.DataFrame(
        [row["values"] for row in batting["values"]],
        columns=batting["headers"]
    )

    st.subheader("🏏 Batting Statistics")

    st.dataframe(
        batting_df,
        width="stretch"
    )

    bowling = get_player_bowling(player_id)

    bowling_df = pd.DataFrame(
        [row["values"] for row in bowling["values"]],
        columns=bowling["headers"]
    )

    st.subheader("🎯 Bowling Statistics")

    st.dataframe(
        bowling_df,
        width="content"
    )

    try:

        runs = batting_df[
            batting_df["ROWHEADER"] == "Runs"
        ]["ODI"].iloc[0]

        highest = batting_df[
            batting_df["ROWHEADER"] == "Highest"
        ]["ODI"].iloc[0]

        wickets = bowling_df[
            bowling_df["ROWHEADER"] == "Wickets"
        ]["ODI"].iloc[0]

        col1, col2, col3 = st.columns(3)

        col1.metric("ODI Runs", runs)
        col2.metric("Highest Score", highest)
        col3.metric("ODI Wickets", wickets)

    except:
        pass