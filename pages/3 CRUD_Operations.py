import streamlit as st

from database.player_db import (
    add_player,
    get_players,
    delete_player,
    update_player
)

st.title("👨‍💻 Player CRUD Operations")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Add",
        "View",
        "Update",
        "Delete"
    ]
)

with tab1:

    st.subheader("Add Player")

    player_name = st.text_input("Player Name")

    country = st.text_input("Country")

    role = st.text_input("Role")

    batting_style = st.text_input("Batting Style")

    bowling_style = st.text_input("Bowling Style")

    if st.button("Add Player"):

        add_player(
            player_name,
            country,
            role,
            batting_style,
            bowling_style
        )

        st.success("Player Added")

with tab2:

    st.subheader("All Players")

    df = get_players()

    st.dataframe(
        df,
        width="stretch"
    )

with tab4:

    st.subheader("Delete Player")

    player_id = st.number_input(
        "Player ID",
        min_value=1
    )

    if st.button("Delete"):

        delete_player(player_id)

        st.success("Player Deleted")

with tab3:

    st.subheader("Update Player")

    player_id = st.number_input(
        "Update Player ID",
        min_value=1
    )

    player_name = st.text_input("New Name")

    country = st.text_input("New Country")

    role = st.text_input("New Role")

    batting_style = st.text_input("New Batting Style")

    bowling_style = st.text_input("New Bowling Style")

    if st.button("Update"):

        update_player(
            player_id,
            player_name,
            country,
            role,
            batting_style,
            bowling_style
        )

        st.success("Player Updated")
