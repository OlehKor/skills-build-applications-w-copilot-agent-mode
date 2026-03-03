from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Очистка колекцій
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Створення команд
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Створення користувачів
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', first_name='Peter', last_name='Parker', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass', first_name='Diana', last_name='Prince', team=dc),
        ]

        # Створення активностей
        activities = [
            app_models.Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            app_models.Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20),
            app_models.Activity.objects.create(user=users[2], type='swim', duration=45, distance=2),
            app_models.Activity.objects.create(user=users[3], type='walk', duration=90, distance=8),
        ]

        # Створення тренувань
        workouts = [
            app_models.Workout.objects.create(user=users[0], name='Chest Day', description='Bench press, push-ups'),
            app_models.Workout.objects.create(user=users[2], name='Leg Day', description='Squats, lunges'),
        ]

        # Створення leaderboard
        app_models.Leaderboard.objects.create(user=users[0], points=100)
        app_models.Leaderboard.objects.create(user=users[1], points=80)
        app_models.Leaderboard.objects.create(user=users[2], points=120)
        app_models.Leaderboard.objects.create(user=users[3], points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
