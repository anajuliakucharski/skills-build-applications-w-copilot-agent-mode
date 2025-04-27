from django.core.management.base import BaseCommand
import pymongo

class Command(BaseCommand):
    help = 'Popula o banco de dados MongoDB com dados de teste.'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['octofit_db']
        users = [
            {"email": "alice@example.com", "name": "Alice", "team": "Team A"},
            {"email": "bob@example.com", "name": "Bob", "team": "Team B"}
        ]
        teams = [
            {"name": "Team A", "members": ["alice@example.com"]},
            {"name": "Team B", "members": ["bob@example.com"]}
        ]
        activity = [
            {"activity_id": 1, "user": "alice@example.com", "type": "run", "duration": 30},
            {"activity_id": 2, "user": "bob@example.com", "type": "walk", "duration": 45}
        ]
        leaderboard = [
            {"leaderboard_id": 1, "team": "Team A", "points": 100},
            {"leaderboard_id": 2, "team": "Team B", "points": 80}
        ]
        workouts = [
            {"workout_id": 1, "user": "alice@example.com", "description": "Morning run"},
            {"workout_id": 2, "user": "bob@example.com", "description": "Evening walk"}
        ]
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activity)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)
        self.stdout.write(self.style.SUCCESS('Banco de dados populado com dados de teste.'))
