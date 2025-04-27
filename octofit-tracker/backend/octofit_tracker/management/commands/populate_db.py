from django.core.management.base import BaseCommand
from octofit_tracker import test_data
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste.'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Limpa as coleções
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        # Insere os dados de teste
        db.users.insert_many(test_data.users)
        db.teams.insert_many(test_data.teams)
        db.activity.insert_many(test_data.activity)
        db.leaderboard.insert_many(test_data.leaderboard)
        db.workouts.insert_many(test_data.workouts)
        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
