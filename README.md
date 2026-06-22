# <a name="cricbuzz-livestats-dashboard"></a>🏏 Cricbuzz LiveStats Dashboard
## <a name="project-overview"></a>Project Overview
Cricbuzz LiveStats Dashboard is a Streamlit-based cricket analytics application that combines real-time cricket information from Cricbuzz RapidAPI with advanced SQL analytics and database management features.

The application allows users to:

- View live cricket matches
- View player batting and bowling statistics
- Execute 25 cricket analytics SQL queries
- Perform CRUD operations on player records
- Analyze historical cricket data stored in MySQL
-----
# <a name="features"></a>Features
## <a name="home-page"></a>1. Home Page
- Project introduction
- Application overview
- Navigation guide
- Technology stack information
-----
## <a name="live-matches-page"></a>2. Live Matches Page
Data Source: Cricbuzz RapidAPI

Features:

- Live match information
- Match status
- Team details
- Venue details
- Real-time updates

API Endpoint Used:

/matches/v1/live

-----
## <a name="player-statistics-page"></a>3. Player Statistics Page
Data Source: Cricbuzz RapidAPI

Features:

- Search player
- Batting statistics
- Bowling statistics
- Player profile information

API Endpoints Used:

/stats/v1/player/search\
/stats/v1/player/{player\_id}\
/stats/v1/player/{player\_id}/batting\
/stats/v1/player/{player\_id}/bowling

-----
## <a name="sql-analytics-page"></a>4. SQL Analytics Page
Data Source: MySQL Database

Features:

- 25 SQL analytical queries
- Beginner, Intermediate and Advanced levels
- Cricket performance analysis
- Team analysis
- Venue analysis
- Partnership analysis
- Toss impact analysis
- Player ranking analysis
### <a name="sql-questions-covered"></a>SQL Questions Covered
#### <a name="beginner-level"></a>*Beginner Level*
Q1. Find all players who represent India. Display their full name, playing role, batting style, and bowling style.

Q2. Show all cricket matches that were played in the last Few days. Include the match description, both team names, venue name with city, and the match date. Sort by most recent matches first.

Q3. List the top 10 highest run scorers in ODI cricket. Show player name, total runs scored, batting average, and number of centuries. Display the highest run scorer first.

Q4. Display all cricket venues that have a seating capacity of more than 25,000 spectators. Show venue name, city, country, and capacity. Order by largest capacity first (10 Venues enough).

Q5. Calculate how many matches each team has won. Show team name and total number of wins. Display teams with the most wins first.

Q6. Count how many players belong to each playing role (like Batsman, Bowler, All-rounder, Wicket-keeper). Show the role and count of players for each role.

Q7. Find the highest individual batting score achieved in each cricket format (Test, ODI, T20I). Display the format and the highest score for that format.

Q8. Show all cricket series that started in the year 2024. Include series name, host country, match type, start date, and total number of matches planned.

#### <a name="intermediate-level"></a>*Intermediate Level*

Q9. Find all-rounder players who have scored more than 1000 runs AND taken more than 50 wickets in their career. Display player name, total runs, total wickets, and the cricket format.

Q10. Get details of the last 20 completed matches. Show match description, both team names, winning team, victory margin, victory type (runs/wickets), and venue name. Display the most recent matches first.

Q11. Compare each player's performance across different cricket formats. For players who have played at least 2 different formats, show their total runs in Test cricket, ODI cricket, and T20I cricket, along with their overall batting average across all formats.

Q12. Analyze each international team's performance when playing at home versus playing away. Determine whether each team played at home or away based on whether the venue country matches the team's country. Count wins for each team in both home and away conditions.

Q13. Identify batting partnerships where two consecutive batsmen (batting positions next to each other) scored a combined total of 100 or more runs in the same innings. Show both player names, their combined partnership runs, and which innings it occurred in.

Q14. Examine bowling performance at different venues. For bowlers who have played at least 3 matches at the same venue, calculate their average economy rate, total wickets taken, and number of matches played at each venue. Focus on bowlers who bowled at least 4 overs in each match.

Q15. Identify players who perform exceptionally well in close matches. A close match is defined as one decided by less than 50 runs OR less than 5 wickets. For these close matches, calculate each player's average runs scored, total close matches played, and how many of those close matches their team won when they batted.

Q16. Track how players' batting performance changes over different years. For matches since 2020, show each player's average runs per match and average strike rate for each year. Only include players who played at least 5 matches in that year.

#### <a name="advanced-level"></a>*Advanced Level*

Q17. Investigate whether winning the toss gives teams an advantage in winning matches. Calculate what percentage of matches are won by the team that wins the toss, broken down by their toss decision (choosing to bat first or bowl first).

Q18. Find the most economical bowlers in limited-overs cricket (ODI and T20 formats). Calculate each bowler's overall economy rate and total wickets taken. Only consider bowlers who have bowled in at least 10 matches and bowled at least 2 overs per match on average.

Q19. Determine which batsmen are most consistent in their scoring. Calculate the average runs scored and the standard deviation of runs for each player. Only include players who have faced at least 10 balls per innings and played since 2022. A lower standard deviation indicates more consistent performance.

Q20. Analyze how many matches each player has played in different cricket formats and their batting average in each format. Show the count of Test matches, ODI matches, and T20 matches for each player, along with their respective batting averages. Only include players who have played at least 20 total matches across all formats.

Q21. Create a comprehensive performance ranking system for players. Combine their batting performance (runs scored, batting average, strike rate), bowling performance (wickets taken, bowling average, economy rate), and fielding performance (catches, stumpings, Run out) into a single weighted score. Use this formula and rank players:
Batting points: (runs_scored × 0.01) + (batting_average × 0.5) + (strike_rate × 0.3)
Bowling points: (wickets_taken × 2) + (50 - bowling_average) × 0.5) + ((6 - economy_rate) × 2)

Rank the top performers in each cricket format.

Q22. Build a head-to-head match prediction analysis between teams. For each pair of teams that have played at least 5 matches against each other in the last 3 years, calculate:
Total matches played between them
Wins for each team
Average victory margin when each team wins
Performance when batting first vs bowling first at different venues
Overall win percentage for each team in this head-to-head record

Q23. Analyze recent player form and momentum. For each player's last 10 batting performances, calculate:
Average runs in their last 5 matches vs their last 10 matches
Recent strike rate trends
Number of scores above 50 in recent matches
A consistency score based on standard deviation
Based on these metrics, categorize players as being in "Excellent Form", "Good Form", "Average Form", or "Poor Form".

Q24. Study successful batting partnerships to identify the best player combinations. For pairs of players who have batted together as consecutive batsmen (positions differ by 1) in at least 5 partnerships:
Calculate their average partnership runs
Count how many of their partnerships exceeded 50 runs
Find their highest partnership score
Calculate their success rate (percentage of good partnerships)
Rank the most successful batting partnerships.

Q25. Perform a time-series analysis of player performance evolution. Track how each player's batting performance changes over time by:
Calculating quarterly averages for runs and strike rate
Comparing each quarter's performance to the previous quarter
Identifying whether performance is improving, declining, or stable
Determining overall career trajectory over the last few years
Categorizing players' career phase as "Career Ascending", "Career Declining", or "Career Stable"
Only analyze players with data spanning at least 6 quarters and a minimum of 3 matches per quarter.

-----
## <a name="crud-operations-page"></a>5. CRUD Operations Page
Data Source: MySQL Database

Features:
### <a name="create"></a>Create
Add new player
### <a name="read"></a>Read
View all players
### <a name="update"></a>Update
Modify player information
### <a name="delete"></a>Delete
Remove player records

Fields:

- Player Name
- Country
- Role
- Batting Style
- Bowling Style
-----
# <a name="technology-stack"></a>Technology Stack
## <a name="frontend"></a>Frontend
- Streamlit
## <a name="backend"></a>Backend
- Python
## <a name="database"></a>Database
- MySQL
## <a name="orm-database-connector"></a>ORM / Database Connector
- SQLAlchemy
## <a name="api-integration"></a>API Integration
- Cricbuzz RapidAPI
## <a name="data-processing"></a>Data Processing
- Pandas
-----
# <a name="project-structure"></a>Project Structure
Cricbuzz\_LiveStats/\
│\
├── About.py\
│\
├── api/\
│   └── cricbuzz\_api.py\
│\
├── database/\
│   ├── db\_connection.py\
│   └── player\_db.py\
│\
├── pages/\
│   ├── Live\_Matches.py\
│   ├── Player\_Stats.py\
│   ├── CRUD\_Operations.py\
│   └── SQL\_Analytics.py\
│\
├── queries/\
│   └── query\_collection.py\
│\
├── requirements.txt\
│\
└── README.md

-----
# <a name="database-tables"></a>Database Tables
The project uses the following tables:

players\
teams\
venues\
series\
matches\
innings\
partnerships\
batting\_stats\
bowling\_stats\
batting\_innings\
bowling\_innings\
fielding\_stats\
toss\_details

-----
# <a name="installation"></a>Installation
## <a name="step-3"></a>Step 1
Install dependencies

pip install -r requirements.txt

-----
## <a name="step-4"></a>Step 2
Configure MySQL Database

Create database:

**CREATE** **DATABASE** cricbuzz\_livestats;

Import all required tables.

Update database connection settings inside:

database/db\_connection.py

Example:

**from** sqlalchemy **import** create\_engine\
\
engine = create\_engine(\
`    `"mysql+pymysql://root:password@localhost/cricbuzz\_livestats"\
)

-----
## <a name="step-5"></a>Step 3
Configure RapidAPI Key

Open:

api/cricbuzz\_api.py

Replace:

RAPID\_API\_KEY = "YOUR\_RAPID\_API\_KEY"

with:

RAPID\_API\_KEY = "ACTUAL\_KEY"

-----
## <a name="step-6"></a>Step 4
Run Application

Python -m streamlit run About.py

-----
# <a name="requirements"></a>Requirements
streamlit\
pandas\
sqlalchemy\
requests

Install manually:

pip install streamlit pandas sqlalchemy requests

-----
# <a name="data-sources"></a>Data Sources
## <a name="live-match-data"></a>Live Match Data
Cricbuzz RapidAPI

Used only for:

- Live Matches Page
- Player Statistics Page
## <a name="mysql-database"></a>MySQL Database
Used for:

- SQL Analytics Page
- CRUD Operations Page

The SQL Analytics and CRUD modules operate on manually curated cricket data stored in MySQL.

-----
# <a name="error-handling"></a>Error Handling
The application includes:

- API exception handling
- Database transaction handling
- Null value handling
- Streamlit validation checks
-----
# <a name="security"></a>Security
- API keys are stored separately
- Database credentials are configurable
- SQLAlchemy parameterized queries prevent SQL injection
-----
# <a name="learning-outcomes"></a>Learning Outcomes
This project demonstrates:

- Python programming
- Streamlit dashboard development
- REST API integration
- MySQL database management
- SQL analytics
- CRUD operations
- Data visualization and reporting
-----
# <a name="author"></a>Author
Project: Cricbuzz LiveStats Dashboard

Developed as a Cricket Analytics and Database Management Project using Python, Streamlit, MySQL, SQLAlchemy, and Cricbuzz RapidAPI.
