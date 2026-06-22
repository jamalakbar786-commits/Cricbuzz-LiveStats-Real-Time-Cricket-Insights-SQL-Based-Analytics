CREATE DATABASE cricbuzz_live_stats;

USE cricbuzz_live_stats;

CREATE TABLE teams(
    team_id INT PRIMARY KEY,
    team_name VARCHAR(100),
    short_name VARCHAR(20),
    country VARCHAR(100)
);

CREATE TABLE venues(
    venue_id INT PRIMARY KEY,
    venue_name VARCHAR(200),
    city VARCHAR(100),
    country VARCHAR(100),
    capacity INT
);

CREATE TABLE players(
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(150),
    country VARCHAR(100),
    role VARCHAR(50),
    batting_style VARCHAR(100),
    bowling_style VARCHAR(100)
);

CREATE TABLE series(
    series_id INT PRIMARY KEY,
    series_name VARCHAR(200),
    host_country VARCHAR(100),
    match_type VARCHAR(50),
    start_date DATE,
    end_date DATE
);

CREATE TABLE matches(
    match_id BIGINT PRIMARY KEY,
    series_id INT,
    team1_id INT,
    team2_id INT,
    venue_id INT,
    winner_team_id INT,
    match_desc VARCHAR(100),
    format VARCHAR(20),
    match_date DATE,
    margin_value INT,
    margin_type VARCHAR(20)
);

CREATE TABLE batting_stats(
    batting_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    format VARCHAR(20),
    matches INT,
    innings INT,
    runs INT,
    highest_score INT,
    average DECIMAL(6,2),
    strike_rate DECIMAL(6,2),
    hundreds INT,
    fifties INT
);

CREATE TABLE bowling_stats(
    bowling_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    format VARCHAR(20),
    matches INT,
    wickets INT,
    economy DECIMAL(6,2),
    average DECIMAL(6,2)
);

CREATE TABLE innings (
    innings_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id BIGINT,
    batting_team_id INT,
    innings_number INT,
    total_runs INT,
    wickets_lost INT,
    overs DECIMAL(5,1)
);

CREATE TABLE batting_innings (
    batting_innings_id INT AUTO_INCREMENT PRIMARY KEY,

    match_id BIGINT,
    innings_id INT,

    player_id INT,
    batting_position INT,

    runs INT,
    balls INT,
    fours INT,
    sixes INT,
    strike_rate DECIMAL(6,2),

    dismissal_type VARCHAR(50)
);

CREATE TABLE bowling_innings (
    bowling_innings_id INT AUTO_INCREMENT PRIMARY KEY,

    match_id BIGINT,

    player_id INT,

    overs DECIMAL(5,1),
    maidens INT,
    runs_conceded INT,
    wickets INT,

    economy DECIMAL(5,2)
);

CREATE TABLE fielding_stats (
    fielding_id INT AUTO_INCREMENT PRIMARY KEY,

    match_id BIGINT,
    player_id INT,

    catches INT,
    stumpings INT,
    runouts INT
);

CREATE TABLE partnerships (
    partnership_id INT AUTO_INCREMENT PRIMARY KEY,

    innings_id INT,

    player1_id INT,
    player2_id INT,

    partnership_runs INT
);

CREATE TABLE toss_details (
    toss_id INT AUTO_INCREMENT PRIMARY KEY,

    match_id BIGINT,

    toss_winner_team_id INT,

    decision VARCHAR(20)
);

ALTER TABLE matches
ADD COLUMN match_status VARCHAR(100),
ADD COLUMN venue_country VARCHAR(100);

INSERT IGNORE INTO players(player_name, country, role, batting_style, bowling_style) 
VALUES 
    ("Virat Kohli","India","Batsman","Right Hand Bat","None"),
    ("Rohit Sharma","India","Batsman","Right Hand Bat","None"),
    ("Jasprit Bumrah","India","Bowler","Right Hand Bat","Right Arm Fast"),
    ("Joe Root","England","Batsman","Right Hand Bat","Off Spin"),
    ("Ben Stokes","England","All Rounder","Left Hand Bat","Fast Medium");
    
INSERT INTO batting_stats
(player_id,format,matches,innings,runs,highest_score,average,strike_rate,hundreds,fifties)
VALUES
(1,'ODI',300,288,13848,183,58.67,93.62,50,72),
(2,'ODI',260,252,10554,264,49.32,91.25,31,55),
(4,'ODI',180,170,6450,133,48.12,87.20,18,42),
(5,'ODI',120,110,3200,102,39.50,92.15,5,22);

INSERT INTO bowling_stats
(player_id,format,matches,wickets,economy,average)
VALUES
(3,'ODI',90,170,4.70,22.00),
(5,'ODI',120,85,5.90,35.00);

INSERT INTO teams VALUES
(1,'India','IND','India'),
(2,'England','ENG','England'),
(3,'Australia','AUS','Australia'),
(4,'Pakistan','PAK','Pakistan'),
(5,'South Africa','SA','South Africa');

INSERT INTO venues VALUES
(1,'Wankhede Stadium','Mumbai','India',33000),
(2,'Lord''s','London','England',31000),
(3,'MCG','Melbourne','Australia',100000),
(4,'Eden Gardens','Kolkata','India',68000),
(5,'Newlands','Cape Town','South Africa',25000);

INSERT INTO series VALUES
(101,'India Tour of England 2024','England','Test',
'2024-06-01','2024-07-30'),
(102,'ODI World Cup 2024','India','ODI',
'2024-10-01','2024-11-30'),
(103,'T20 World Cup 2024','USA','T20I',
'2024-06-01','2024-06-30');

INSERT INTO players
(player_name,country,role,batting_style,bowling_style)
VALUES
('KL Rahul','India','Wicket Keeper',
'Right Hand Bat','None'),
('Hardik Pandya','India','All Rounder',
'Right Hand Bat','Right Arm Medium'),
('Jos Buttler','England','Wicket Keeper',
'Right Hand Bat','None'),
('Mitchell Starc','Australia','Bowler',
'Left Hand Bat','Left Arm Fast');

INSERT INTO matches
(
match_id,
series_id,
team1_id,
team2_id,
venue_id,
winner_team_id,
match_desc,
format,
match_date,
margin_value,
margin_type,
match_status,
venue_country
)
VALUES

(
1001,
102,
1,
2,
1,
1,
'India vs England',
'ODI',
'2024-10-05',
45,
'Runs',
'Completed',
'India'
),

(
1002,
102,
3,
4,
3,
3,
'Australia vs Pakistan',
'ODI',
'2024-10-06',
6,
'Wickets',
'Completed',
'Australia'
),

(
1003,
103,
1,
3,
4,
1,
'India vs Australia',
'T20I',
'2024-06-10',
12,
'Runs',
'Completed',
'India'
);

INSERT INTO toss_details
(match_id,toss_winner_team_id,decision)
VALUES
(1001,1,'BAT'),
(1002,3,'BOWL'),
(1003,3,'BAT');

INSERT INTO innings
(
match_id,
batting_team_id,
innings_number,
total_runs,
wickets_lost,
overs
)
VALUES
(1001,1,1,320,8,50),
(1001,2,2,275,10,48),
(1002,4,1,240,10,49),
(1002,3,2,241,4,44),
(1003,1,1,185,6,20),
(1003,3,2,173,8,20);

INSERT INTO batting_innings
(
match_id,
innings_id,
player_id,
batting_position,
runs,
balls,
fours,
sixes,
strike_rate,
dismissal_type
)
VALUES
(1001,1,1,3,120,110,12,2,109.09,'Caught'),
(1001,1,2,1,80,95,8,1,84.21,'Bowled'),
(1001,1,6,5,65,55,5,3,118.18,'Caught');

INSERT INTO bowling_innings
(
match_id,
player_id,
overs,
maidens,
runs_conceded,
wickets,
economy
)
VALUES
(1001,3,10,1,42,4,4.20),
(1002,9,10,0,45,3,4.50),
(1003,3,4,0,24,2,6.00);

INSERT INTO fielding_stats
(
match_id,
player_id,
catches,
stumpings,
runouts
)
VALUES
(1001,1,2,0,0),
(1001,6,1,1,0),
(1002,9,1,0,1);

INSERT INTO partnerships
(
innings_id,
player1_id,
player2_id,
partnership_runs
)
VALUES
(1,2,1,200),
(2,4,7,110),
(5,1,6,120);

ALTER TABLE batting_innings MODIFY COLUMN strike_rate DECIMAL(7,2);

UPDATE batting_innings bi
JOIN innings i
ON bi.innings_id = i.innings_id
SET bi.match_id = i.match_id;

ALTER TABLE players
MODIFY player_name VARCHAR(150) NOT NULL;




















































































































































