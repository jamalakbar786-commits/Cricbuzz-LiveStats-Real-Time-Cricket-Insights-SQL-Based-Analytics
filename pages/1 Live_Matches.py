import streamlit as st
from api.cricbuzz_api import get_live_matches

st.title("🏏 Live Cricket Matches")

# Fetch data safely from your API endpoint
with st.spinner("Loading live matches..."):
    data = get_live_matches() or {}

type_matches = data.get("typeMatches", [])

# Counter flag to keep track of active records
matches_found = False

for match_type in type_matches:
    series_matches = match_type.get("seriesMatches", [])
    
    for series in series_matches:
        # Resolve wrapper object safely
        series_info = series.get("seriesAdWrapper") or series
        matches = series_info.get("matches", [])
        
        for match in matches:
            match_info = match.get("matchInfo", {})
            if not match_info:
                continue
                
            matches_found = True
            st.divider()
            
            # Extract names safely using original exact keys
            team1_name = match_info.get("team1", {}).get("teamName", "Team 1")
            team2_name = match_info.get("team2", {}).get("teamName", "Team 2")
            
            st.subheader(f"{team1_name} vs {team2_name}")
            st.write(
                f"**Match:** {match_info.get('matchDesc', 'N/A')}"
            )
            st.write(
               f"**Format:** {match_info.get('matchFormat', 'N/A')}"
            )
            venue = (
                match_info.get("venueInfo", {})
                .get("ground", "N/A")
            )
            st.write(f"**Venue:** {venue}")
            st.write(f"**Series:** {series_info.get('seriesName', 'N/A')}")
            st.write(f"**Status:** {match_info.get('status', 'N/A')}")
            
            # --- Dynamic Live Match Score Logic ---
            score = match.get("matchScore", {})
            
            def get_formatted_score(score_dict, team_key):
                if team_key not in score_dict:
                    return "Yet to bat"
                
                team_data = score_dict[team_key]
                # Target the active innings layout safely (Innings 2 -> Innings 1 -> Fallback)
                innings = team_data.get("inngs2") or team_data.get("inngs1") or {}
                
                if not innings:
                    return "Yet to bat"
                    
                runs = innings.get("runs", 0)
                wickets = innings.get("wickets", 0)
                overs = innings.get("overs", 0)
                declared = " dec" if innings.get("isDeclared") else ""
                
                return f"{runs}/{wickets} ({overs} ov){declared}"

            team1_score = get_formatted_score(score, "team1Score")
            team2_score = get_formatted_score(score, "team2Score")
            
            # --- Streamlit Column Layout Render ---
            col1, col2 = st.columns(2)
            with col1:
                st.metric(team1_name, team1_score)
            with col2:
                st.metric(team2_name, team2_score)

if not matches_found:
    st.info("No active live matches found at the moment.")