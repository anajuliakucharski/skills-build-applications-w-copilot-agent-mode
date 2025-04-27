from django.core.management.base import BaseCommand
from octofit_tracker import test_data
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Popula o banco de dados MongoDB com dados de teste.'

    def handle(self, *args, **options):
        # Limpa as coleções antes de inserir
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Popula usuários
        for user in test_data.users:
            User.objects.create(**user)
        # Popula times
        for team in test_data.teams:
            Team.objects.create(**team)
        # Popula atividades
        for activity in test_data.activities:
            Activity.objects.create(**activity)
        # Popula leaderboard
        for entry in test_data.leaderboard:
            Leaderboard.objects.create(**entry)
        # Popula workouts
        for workout in test_data.workouts:
            Workout.objects.create(**workout)

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
