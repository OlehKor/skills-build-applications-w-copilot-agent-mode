from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, distance=2.5)
        self.assertEqual(activity.type, 'run')

    def test_workout_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        workout = Workout.objects.create(user=user, name='Test Workout', description='desc')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=42)
        self.assertEqual(leaderboard.points, 42)
