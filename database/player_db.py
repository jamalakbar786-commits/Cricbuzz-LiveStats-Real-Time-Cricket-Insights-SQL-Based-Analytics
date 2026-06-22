import pandas as pd
from sqlalchemy import text

from database.db_connection import engine

def add_player(
        player_name,
        country,
        role,
        batting_style,
        bowling_style
):

    query = text("""
        INSERT INTO players
        (
            player_name,
            country,
            role,
            batting_style,
            bowling_style
        )
        VALUES
        (
            :player_name,
            :country,
            :role,
            :batting_style,
            :bowling_style
        )
    """)

    with engine.begin() as conn:

        conn.execute(
            query,
            {
                "player_name": player_name,
                "country": country,
                "role": role,
                "batting_style": batting_style,
                "bowling_style": bowling_style
            }
        )

def get_players():

    query = """
    SELECT *
    FROM players
    ORDER BY player_id
    """

    return pd.read_sql(query, engine)

def delete_player(player_id):

    query = text("""
        DELETE FROM players
        WHERE player_id = :player_id
    """)

    with engine.begin() as conn:

        conn.execute(
            query,
            {
                "player_id": player_id
            }
        )

def update_player(
        player_id,
        player_name,
        country,
        role,
        batting_style,
        bowling_style
):

    query = text("""
        UPDATE players
        SET
            player_name = :player_name,
            country = :country,
            role = :role,
            batting_style = :batting_style,
            bowling_style = :bowling_style
        WHERE player_id = :player_id
    """)

    with engine.begin() as conn:

        conn.execute(
            query,
            {
                "player_id": player_id,
                "player_name": player_name,
                "country": country,
                "role": role,
                "batting_style": batting_style,
                "bowling_style": bowling_style
            }
        )
