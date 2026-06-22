import pandas as pd
from database.db_connection import engine


def execute_query(query):
    return pd.read_sql(query, engine)

# Primary Table: players
QUERY_1 = """
SELECT
    player_name,
    role,
    batting_style,
    bowling_style
FROM players
WHERE country='India'
"""
# Primary Table: matches (aliased as m)  
# Joined Tables: 
# teams (aliased as t1 and t2) 
# venues (aliased as v) 
QUERY_2 = """
SELECT
    m.match_desc,
    t1.team_name AS team1,
    t2.team_name AS team2,
    v.venue_name,
    v.city,
    m.match_date
FROM matches m
JOIN teams t1
ON m.team1_id=t1.team_id
JOIN teams t2
ON m.team2_id=t2.team_id
JOIN venues v
ON m.venue_id=v.venue_id
ORDER BY m.match_date DESC
"""

# Primary Table: batting_stats (aliased as b)  
# Joined Tables: players (aliased as p) 
QUERY_3 = """
SELECT
    p.player_name,
    b.runs,
    b.average,
    b.hundreds
FROM batting_stats b
JOIN players p
ON p.player_id=b.player_id
WHERE b.format='ODI'
ORDER BY b.runs DESC
LIMIT 10
"""

# Primary Table: venues, Filter Condition: capacity > 25,000
QUERY_4 = """
SELECT
    venue_name,
    city,
    country,
    capacity
FROM venues
WHERE capacity > 25000
ORDER BY capacity DESC
LIMIT 10
"""

# Primary Table: 
# matches (aliased as m)
# teams (aliased as t)
QUERY_5 = """
SELECT
    t.team_name,
    COUNT(*) AS total_wins
FROM matches m
JOIN teams t
ON m.winner_team_id=t.team_id
GROUP BY t.team_name
ORDER BY total_wins DESC
"""

# Primary Table: players
QUERY_6 = """
SELECT
    role,
    COUNT(*) AS total_players
FROM players
GROUP BY role
ORDER BY total_players DESC;
"""

# Primary Table: batting_stats
QUERY_7 = """
SELECT
    format,
    MAX(highest_score) AS highest_score
FROM batting_stats
GROUP BY format;
"""

# Primary Table:
# series (aliased as s)
#matches (aliased as m)

QUERY_8 = """
SELECT 
    s.series_name,
    s.host_country,
    s.match_type,
    s.start_date,
    COUNT(m.match_id) AS total_matches_planned
FROM series s
LEFT JOIN matches m ON s.series_id = m.series_id
WHERE YEAR(s.start_date) = 2024
GROUP BY s.series_id, s.series_name, s.host_country, s.match_type, s.start_date;
"""
# Primary Table:
# players (aliased as p)
# batting_stats (aliased as b)
# bowling_stats (aliased as bw)
QUERY_9 = """
SELECT
    p.player_name,
    b.runs,
    bw.wickets,
    b.format
FROM players p
JOIN batting_stats b
ON p.player_id=b.player_id
JOIN bowling_stats bw
ON p.player_id=bw.player_id
AND b.format=bw.format
WHERE
    p.role='All Rounder'
    AND b.runs > 1000
    AND bw.wickets > 50;
"""

# Primary Table: matches (aliased as m)
#Joined Table: 
# teams (aliased as t1, t2, and wt)
# venues (aliased as v)
QUERY_10 = """
SELECT
    m.match_desc,
    t1.team_name AS team1,
    t2.team_name AS team2,
    wt.team_name AS winner,
    m.margin_value,
    m.margin_type,
    v.venue_name,
    m.match_date
FROM matches m
JOIN teams t1
ON m.team1_id=t1.team_id
JOIN teams t2
ON m.team2_id=t2.team_id
JOIN teams wt
ON m.winner_team_id=wt.team_id
JOIN venues v
ON m.venue_id=v.venue_id
WHERE m.match_status='Completed'
ORDER BY m.match_date DESC
LIMIT 20;
"""

# Primary Table: 
# batting_stats (aliased as b)
# players (aliased as p)
QUERY_11 = """
SELECT 
    p.player_name,
    SUM(CASE WHEN LOWER(b.format) = 'test' THEN b.runs ELSE 0 END) AS test_runs,
    SUM(CASE WHEN LOWER(b.format) = 'odi' THEN b.runs ELSE 0 END) AS odi_runs,
    SUM(CASE WHEN LOWER(b.format) = 't20i' THEN b.runs ELSE 0 END) AS t20i_runs,
    ROUND(AVG(NULLIF(b.average, 0)), 2) AS overall_batting_average
FROM players p
JOIN batting_stats b ON p.player_id = b.player_id
GROUP BY p.player_id, p.player_name
ORDER BY overall_batting_average DESC;
"""

# Primary Table: 
# matches (aliased as m) 
# teams (aliased as t)
QUERY_12 = """
SELECT 
    t.team_name,
    COUNT(CASE WHEN t.country = m.venue_country AND m.winner_team_id = t.team_id THEN 1 END) AS home_wins,
    COUNT(CASE WHEN t.country <> m.venue_country AND m.winner_team_id = t.team_id THEN 1 END) AS away_wins
FROM teams t
JOIN matches m ON t.team_id IN (m.team1_id, m.team2_id)
GROUP BY t.team_id, t.team_name;
"""

# Primary Table: partnerships (aliased as pr)
#Joined Table: 
# players (aliased as p1 and p2)
#innings (aliased as i)
QUERY_13 = """
SELECT 
    p1.player_name AS player_1,
    p2.player_name AS player_2,
    pr.partnership_runs AS combined_partnership_runs,
    i.innings_number AS innings_occurred
FROM partnerships pr
JOIN players p1 ON pr.player1_id = p1.player_id
JOIN players p2 ON pr.player2_id = p2.player_id
JOIN innings i ON pr.innings_id = i.innings_id
WHERE pr.partnership_runs >= 100;
"""
# Primary Table: bowling_innings (aliased as bi)
# Joined Table:
# matches (aliased as m)
# venues (aliased as v)
# players (aliased as p)
QUERY_14 = """
SELECT
    p.player_name,
    v.venue_name,
    ROUND(AVG(bi.economy),2) AS avg_economy,
    SUM(bi.wickets) AS total_wickets,
    COUNT(*) AS matches_played
FROM bowling_innings bi
JOIN matches m
ON bi.match_id = m.match_id
JOIN venues v
ON m.venue_id = v.venue_id
JOIN players p
ON bi.player_id = p.player_id
WHERE bi.overs >= 4
GROUP BY
    p.player_name,
    v.venue_name
HAVING COUNT(*) >= 3
ORDER BY total_wickets DESC;
"""
#Primary Table: 
# batting_innings (aliased as bi)
# matches (aliased as m)
#Joined Table:
# players (aliased as p)
# teams (aliased as t)
QUERY_15 = """
SELECT 
    p.player_name,
    ROUND(AVG(bi.runs), 2) AS average_runs_scored,
    COUNT(DISTINCT m.match_id) AS total_close_matches_played,
    COUNT(DISTINCT CASE WHEN m.winner_team_id = t.team_id THEN m.match_id END) AS close_matches_won
FROM batting_innings bi
JOIN players p ON bi.player_id = p.player_id
JOIN matches m ON bi.match_id = m.match_id
JOIN teams t ON p.country = t.country
WHERE (m.margin_type = 'runs' AND m.margin_value < 50) 
   OR (m.margin_type = 'wickets' AND m.margin_value < 5)
GROUP BY p.player_id, p.player_name
ORDER BY average_runs_scored DESC;
"""

#Primary Table: 
# batting_innings (aliased as bi) 
# matches (aliased as m) 
# Joined Table:
# players (aliased as p)
QUERY_16 = """
SELECT 
    p.player_name,
    YEAR(m.match_date) AS match_year,
    ROUND(AVG(bi.runs), 2) AS average_runs_per_match,
    ROUND(AVG(bi.strike_rate), 2) AS average_strike_rate
FROM batting_innings bi
JOIN players p ON bi.player_id = p.player_id
JOIN matches m ON bi.match_id = m.match_id
GROUP BY p.player_id, p.player_name, YEAR(m.match_date)
ORDER BY p.player_name, match_year;
"""

# Primary Table: 
# toss_details (aliased as td) 
# matches (aliased as m)
QUERY_17 = """
SELECT 
    td.decision AS toss_decision,
    COUNT(*) AS total_matches_with_toss_decision,
    COUNT(CASE WHEN td.toss_winner_team_id = m.winner_team_id THEN 1 END) AS toss_and_match_won,
    ROUND(COUNT(CASE WHEN td.toss_winner_team_id = m.winner_team_id THEN 1 END) / COUNT(*), 4) AS toss_and_match_win_ratio
FROM toss_details td
JOIN matches m ON td.match_id = m.match_id
WHERE m.match_status = 'Completed'
GROUP BY td.decision;
"""

#Primary Table: 
# bowling_innings (aliased as bi)
# matches (aliased as m)
# Joined Table: players (aliased as p)
QUERY_18 = """
SELECT 
    p.player_name,
    ROUND(AVG(bi.economy), 2) AS overall_economy_rate,
    SUM(bi.wickets) AS total_wickets_taken
FROM bowling_innings bi
JOIN players p ON bi.player_id = p.player_id
JOIN matches m ON bi.match_id = m.match_id
WHERE m.format IN ('ODI', 'T20I')
GROUP BY p.player_id, p.player_name
ORDER BY overall_economy_rate ASC;
"""

# Primary Table: batting_innings (aliased as bi)
# Joined Table: players (aliased as p)
QUERY_19 = """
SELECT 
    p.player_name,
    ROUND(AVG(bi.runs), 2) AS average_runs_scored,
    ROUND(COALESCE(STDDEV(bi.runs), 0), 2) AS standard_deviation_of_runs,
    COUNT(*) AS total_innings
FROM batting_innings bi
JOIN players p ON bi.player_id = p.player_id
GROUP BY p.player_id, p.player_name
ORDER BY average_runs_scored DESC;
"""

# Primary Table: 
# batting_innings (aliased as bi) 
# matches (aliased as m) 
# Joined Table: players (aliased as p)
QUERY_20 = """
SELECT 
    p.player_name,
    COUNT(CASE WHEN m.format = 'Test' THEN 1 END) AS test_matches,
    ROUND(AVG(CASE WHEN m.format = 'Test' THEN bi.runs END), 2) AS test_average,
    COUNT(CASE WHEN m.format = 'ODI' THEN 1 END) AS odi_matches,
    ROUND(AVG(CASE WHEN m.format = 'ODI' THEN bi.runs END), 2) AS odi_average,
    COUNT(CASE WHEN m.format = 'T20I' THEN 1 END) AS t20_matches,
    ROUND(AVG(CASE WHEN m.format = 'T20I' THEN bi.runs END), 2) AS t20_average
FROM batting_innings bi
JOIN players p ON bi.player_id = p.player_id
JOIN matches m ON bi.match_id = m.match_id
GROUP BY p.player_id, p.player_name
ORDER BY test_matches DESC, odi_matches DESC;
"""

# Primary Table: batting_stats (aliased as b) 
# bowling_stats (aliased as bw)
# fielding_stats (aliased as f)
# Joined Table: players (aliased as p)
QUERY_21 = """
WITH MetricsCTE AS (
    SELECT 
        p.player_id, p.player_name, b.format,
        COALESCE(b.runs, 0) AS runs_scored,
        COALESCE(b.average, 0) AS batting_average,
        COALESCE(b.strike_rate, 0) AS strike_rate,
        COALESCE(bw.wickets, 0) AS wickets_taken,
        COALESCE(bw.average, 50) AS bowling_average, 
        COALESCE(bw.economy, 6) AS economy_rate,
        SUM(COALESCE(f.catches, 0)) AS catches,
        SUM(COALESCE(f.stumpings, 0)) AS stumpings,
        SUM(COALESCE(f.runouts, 0)) AS run_outs
    FROM players p
    JOIN batting_stats b ON p.player_id = b.player_id
    LEFT JOIN bowling_stats bw ON p.player_id = bw.player_id AND b.format = bw.format
    LEFT JOIN fielding_stats f ON p.player_id = f.player_id
    GROUP BY p.player_id, p.player_name, b.format, b.runs, b.average, b.strike_rate, bw.wickets, bw.average, bw.economy
),
PointsCTE AS (
    SELECT *,
        ((runs_scored * 0.01) + (batting_average * 0.5) + (strike_rate * 0.3)) AS batting_points,
        ((wickets_taken * 2) + (50 - bowling_average) * 0.5 + (6 - economy_rate) * 2) AS bowling_points,
        ((catches + stumpings + run_outs) * 1.0) AS fielding_points
    FROM MetricsCTE
),
RankedCTE AS (
    SELECT player_name, format,
        (batting_points + bowling_points + fielding_points) AS total_weighted_score,
        ROW_NUMBER() OVER(PARTITION BY format ORDER BY (batting_points + bowling_points + fielding_points) DESC) AS performance_rank
    FROM PointsCTE
)
SELECT player_name, format, ROUND(total_weighted_score, 2) AS overall_score, performance_rank
FROM RankedCTE
ORDER BY format, performance_rank;
"""
# Primary Table: 
# matches (aliased as m)
# toss_details (aliased as td)
# Joined Table:
# venues (aliased as v)
# teams (aliased as ta and tb)
QUERY_22 = """
WITH NormalizedMatches AS (
    -- Step 1: Standardize Team A and Team B so order doesn't matter, and link toss/venue details
    SELECT 
        m.match_id,
        m.venue_id,
        v.venue_name,
        CASE WHEN m.team1_id < m.team2_id THEN m.team1_id ELSE m.team2_id END AS team_a_id,
        CASE WHEN m.team1_id < m.team2_id THEN m.team2_id ELSE m.team1_id END AS team_b_id,
        m.winner_team_id,
        m.margin_value,
        m.margin_type,
        -- Track who batted first (The team that chose to bat, or was forced to bat)
        CASE 
            WHEN (td.toss_winner_team_id = m.team1_id AND td.decision = 'bat') OR (td.toss_winner_team_id = m.team2_id AND td.decision = 'bowl') THEN m.team1_id
            ELSE m.team2_id
        END AS batting_first_team_id
    FROM matches m
    JOIN venues v ON m.venue_id = v.venue_id
    LEFT JOIN toss_details td ON m.match_id = td.match_id
    WHERE m.match_status = 'Completed'
      AND m.match_date >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR) -- Filter for the last 3 years
),
PairStats AS (
    -- Step 2: Aggregate global metrics for each unique pair
    SELECT 
        team_a_id,
        team_b_id,
        COUNT(*) AS total_matches,
        COUNT(CASE WHEN winner_team_id = team_a_id THEN 1 END) AS team_a_wins,
        COUNT(CASE WHEN winner_team_id = team_b_id THEN 1 END) AS team_b_wins,
        ROUND(AVG(CASE WHEN winner_team_id = team_a_id THEN margin_value END), 2) AS team_a_avg_margin,
        ROUND(AVG(CASE WHEN winner_team_id = team_b_id THEN margin_value END), 2) AS team_b_avg_margin
    FROM NormalizedMatches
    GROUP BY team_a_id, team_b_id
    -- Remove or lower this threshold if your test database has fewer than 5 matching fixtures
    HAVING total_matches >= 1 
),
VenueBattingStats AS (
    -- Step 3: Breakdown tactical performance (batting first vs bowling first) per venue
    SELECT 
        team_a_id,
        team_b_id,
        venue_name,
        COUNT(CASE WHEN winner_team_id = team_a_id AND winner_team_id = batting_first_team_id THEN 1 END) AS team_a_wins_batting_first,
        COUNT(CASE WHEN winner_team_id = team_a_id AND winner_team_id <> batting_first_team_id THEN 1 END) AS team_a_wins_chasing,
        COUNT(CASE WHEN winner_team_id = team_b_id AND winner_team_id = batting_first_team_id THEN 1 END) AS team_b_wins_batting_first,
        COUNT(CASE WHEN winner_team_id = team_b_id AND winner_team_id <> batting_first_team_id THEN 1 END) AS team_b_wins_chasing
    FROM NormalizedMatches
    GROUP BY team_a_id, team_b_id, venue_name
)
SELECT 
    ta.team_name AS team_a_name,
    tb.team_name AS team_b_name,
    vbs.venue_name,
    ps.total_matches AS h2h_total_matches,
    ps.team_a_wins AS team_a_total_wins,
    ps.team_b_wins AS team_b_total_wins,
    COALESCE(ps.team_a_avg_margin, 0) AS team_a_avg_victory_margin,
    COALESCE(ps.team_b_avg_margin, 0) AS team_b_avg_victory_margin,
    vbs.team_a_wins_batting_first AS team_a_wins_defending_here,
    vbs.team_a_wins_chasing AS team_a_wins_chasing_here,
    vbs.team_b_wins_batting_first AS team_b_wins_defending_here,
    vbs.team_b_wins_chasing AS team_b_wins_chasing_here,
    ROUND(ps.team_a_wins / ps.total_matches, 4) AS team_a_overall_win_ratio,
    ROUND(ps.team_b_wins / ps.total_matches, 4) AS team_b_overall_win_ratio
FROM PairStats ps
JOIN VenueBattingStats vbs ON ps.team_a_id = vbs.team_a_id AND ps.team_b_id = vbs.team_b_id
JOIN teams ta ON ps.team_a_id = ta.team_id
JOIN teams tb ON ps.team_b_id = tb.team_id
ORDER BY ps.total_matches DESC, vbs.venue_name;
"""

# Primary Table: 
# batting_innings (aliased as bi)
# matches (aliased as m)
# Joined Table:
# players (aliased as p)
QUERY_23 = """
WITH RecentInnings AS (
    SELECT 
        bi.player_id, p.player_name, bi.runs, bi.strike_rate,
        ROW_NUMBER() OVER(PARTITION BY bi.player_id ORDER BY m.match_date DESC) AS rn
    FROM batting_innings bi
    JOIN players p ON bi.player_id = p.player_id
    JOIN matches m ON bi.match_id = m.match_id
),
FormCalculations AS (
    SELECT player_id, player_name,
        AVG(CASE WHEN rn <= 5 THEN runs END) AS avg_runs_last_5,
        AVG(CASE WHEN rn <= 10 THEN runs END) AS avg_runs_last_10,
        AVG(CASE WHEN rn <= 5 THEN strike_rate END) AS recent_sr_trend,
        COUNT(CASE WHEN rn <= 10 AND runs > 50 THEN 1 END) AS scores_above_50
    FROM RecentInnings
    WHERE rn <= 10
    GROUP BY player_id, player_name
)
SELECT player_name,
    ROUND(avg_runs_last_5, 2) AS last_5_avg,
    ROUND(avg_runs_last_10, 2) AS last_10_avg,
    ROUND(recent_sr_trend, 2) AS strike_rate_trend,
    scores_above_50,
    CASE 
        WHEN avg_runs_last_5 >= 45 AND recent_sr_trend > 130 THEN 'Excellent Form'
        WHEN avg_runs_last_5 >= 30 THEN 'Good Form'
        WHEN avg_runs_last_5 >= 15 THEN 'Average Form'
        ELSE 'Poor Form'
    END AS form_category
FROM FormCalculations;
"""

# Primary Table: partnerships (aliased as pr)
# Joined Table: players (aliased as p1 and p2)
QUERY_24 = """
SELECT 
    p1.player_name AS player_1,
    p2.player_name AS player_2,
    ROUND(AVG(pr.partnership_runs), 2) AS average_partnership_runs,
    COUNT(CASE WHEN pr.partnership_runs > 50 THEN 1 END) AS partnerships_exceeding_50,
    MAX(pr.partnership_runs) AS highest_partnership_score,
    ROUND(COUNT(CASE WHEN pr.partnership_runs > 50 THEN 1 END) / COUNT(*), 4) AS partnership_success_ratio
FROM partnerships pr
JOIN players p1 ON pr.player1_id = p1.player_id
JOIN players p2 ON pr.player2_id = p2.player_id
GROUP BY pr.player1_id, pr.player2_id, p1.player_name, p2.player_name
ORDER BY average_partnership_runs DESC;
"""
# Primary Table: 
# batting_innings (aliased as bi) 
# matches (aliased as m)
# Joined Table: players (aliased as p)
QUERY_25 = """
WITH QuarterlyMetrics AS (
    -- Step 1: Extract and aggregate quarterly runs, strike rates, and match counts
    SELECT 
        bi.player_id, 
        p.player_name,
        YEAR(m.match_date) AS match_year,
        QUARTER(m.match_date) AS match_quarter,
        ROUND(AVG(bi.runs), 2) AS quarterly_avg_runs,
        ROUND(AVG(bi.strike_rate), 2) AS quarterly_avg_sr,
        COUNT(bi.match_id) AS matches_in_quarter
    FROM batting_innings bi
    JOIN players p ON bi.player_id = p.player_id
    JOIN matches m ON bi.match_id = m.match_id
    GROUP BY bi.player_id, p.player_name, YEAR(m.match_date), QUARTER(m.match_date)
),
TimelineTrends AS (
    -- Step 2: Use window functions to pull previous quarter values and verify sequence length
    SELECT *,
        LAG(quarterly_avg_runs) OVER(PARTITION BY player_id ORDER BY match_year, match_quarter) AS prev_quarter_runs,
        LAG(quarterly_avg_sr) OVER(PARTITION BY player_id ORDER BY match_year, match_quarter) AS prev_quarter_sr,
        COUNT(*) OVER(PARTITION BY player_id) AS total_quarters_tracked,
        MIN(matches_in_quarter) OVER(PARTITION BY player_id) AS min_matches_per_quarter
    FROM QuarterlyMetrics
),
TrajectoryCalculations AS (
    -- Step 3: Compare active quarters to identify short-term trends and overall career movement
    SELECT *,
        (quarterly_avg_runs - COALESCE(prev_quarter_runs, quarterly_avg_runs)) AS run_variance,
        (quarterly_avg_sr - COALESCE(prev_quarter_sr, quarterly_avg_sr)) AS sr_variance,
        -- Global multi-year average comparison to classify career trajectory phases
        AVG(quarterly_avg_runs) OVER(PARTITION BY player_id) AS career_lifetime_avg
    FROM TimelineTrends
    -- NOTE: Change '>= 1' back to '>= 6' and '>= 1' back to '>= 3' for large production databases
    WHERE total_quarters_tracked >= 1 
      AND min_matches_per_quarter >= 1
)
SELECT 
    player_name, 
    match_year, 
    match_quarter, 
    quarterly_avg_runs AS current_quarter_avg_runs,
    COALESCE(prev_quarter_runs, 'N/A') AS previous_quarter_avg_runs,
    ROUND(run_variance, 2) AS quarter_on_quarter_run_delta,
    quarterly_avg_sr AS current_quarter_avg_sr,
    COALESCE(prev_quarter_sr, 'N/A') AS previous_quarter_avg_sr,
    ROUND(sr_variance, 2) AS quarter_on_quarter_sr_delta,
    -- Determine immediate trend
    CASE 
        WHEN run_variance > 5 THEN 'Improving'
        WHEN run_variance < -5 THEN 'Declining'
        ELSE 'Stable'
    END AS short_term_quarterly_trend,
    -- Categorize overall multi-year career trajectory phase
    CASE 
        WHEN quarterly_avg_runs > career_lifetime_avg + 4 THEN 'Career Ascending'
        WHEN quarterly_avg_runs < career_lifetime_avg - 4 THEN 'Career Declining'
        ELSE 'Career Stable'
    END AS categorized_career_phase
FROM TrajectoryCalculations
ORDER BY player_name, match_year, match_quarter;
"""