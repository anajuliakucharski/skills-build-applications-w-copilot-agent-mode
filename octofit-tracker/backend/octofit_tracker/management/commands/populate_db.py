from django.core.management.base import BaseCommand
import pymongo
from octofit_tracker.test_data import users, teams, activity, leaderboard, workouts

class Command(BaseCommand):
    help = 'Popula o banco de dados octofit_db com dados de teste.'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['octofit_db']
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
