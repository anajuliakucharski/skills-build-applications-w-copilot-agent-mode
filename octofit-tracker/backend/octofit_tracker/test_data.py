# Test data for OctoFit Tracker (adaptado do exemplo Monafit)
users = [
    {"email": "alice@example.com", "name": "Alice", "team": "Team A"},
    {"email": "bob@example.com", "name": "Bob", "team": "Team B"},
    {"email": "carol@example.com", "name": "Carol", "team": "Team A"}
]
teams = [
    {"name": "Team A", "members": ["alice@example.com", "carol@example.com"]},
    {"name": "Team B", "members": ["bob@example.com"]}
]
activity = [
    {"activity_id": 1, "user": "alice@example.com", "type": "run", "duration": 30},
    {"activity_id": 2, "user": "bob@example.com", "type": "walk", "duration": 45},
    {"activity_id": 3, "user": "carol@example.com", "type": "bike", "duration": 60}
]
leaderboard = [
    {"leaderboard_id": 1, "team": "Team A", "points": 150},
    {"leaderboard_id": 2, "team": "Team B", "points": 80}
]
workouts = [
    {"workout_id": 1, "user": "alice@example.com", "description": "Morning run"},
    {"workout_id": 2, "user": "bob@example.com", "description": "Evening walk"},
    {"workout_id": 3, "user": "carol@example.com", "description": "Afternoon bike ride"}
]
