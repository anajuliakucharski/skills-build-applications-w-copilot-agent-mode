# Test data for OctoFit Tracker (baseado no exemplo Monafit)
users = [
    {"email": "thundergod@mhigh.edu", "name": "Thor Odinson", "team": "Blue Team"},
    {"email": "metalgeek@mhigh.edu", "name": "Tony Stark", "team": "Gold Team"},
    {"email": "zerocool@mhigh.edu", "name": "Dade Murphy", "team": "Blue Team"},
    {"email": "crashoverride@hmhigh.edu", "name": "Kate Libby", "team": "Gold Team"},
    {"email": "sleeptoken@mhigh.edu", "name": "Sleep Token", "team": "Blue Team"},
]
teams = [
    {"name": "Blue Team", "members": ["thundergod@mhigh.edu", "zerocool@mhigh.edu", "sleeptoken@mhigh.edu"]},
    {"name": "Gold Team", "members": ["metalgeek@mhigh.edu", "crashoverride@hmhigh.edu"]},
]
activity = [
    {"activity_id": 1, "user": "thundergod@mhigh.edu", "type": "Cycling", "duration": 60},
    {"activity_id": 2, "user": "metalgeek@mhigh.edu", "type": "Crossfit", "duration": 120},
    {"activity_id": 3, "user": "zerocool@mhigh.edu", "type": "Running", "duration": 90},
    {"activity_id": 4, "user": "crashoverride@hmhigh.edu", "type": "Strength", "duration": 30},
    {"activity_id": 5, "user": "sleeptoken@mhigh.edu", "type": "Swimming", "duration": 75},
]
leaderboard = [
    {"leaderboard_id": 1, "team": "Blue Team", "points": 285},
    {"leaderboard_id": 2, "team": "Gold Team", "points": 150},
]
workouts = [
    {"workout_id": 1, "user": "thundergod@mhigh.edu", "description": "Cycling Training"},
    {"workout_id": 2, "user": "metalgeek@mhigh.edu", "description": "Crossfit"},
    {"workout_id": 3, "user": "zerocool@mhigh.edu", "description": "Running Training"},
    {"workout_id": 4, "user": "crashoverride@hmhigh.edu", "description": "Strength Training"},
    {"workout_id": 5, "user": "sleeptoken@mhigh.edu", "description": "Swimming Training"},
]