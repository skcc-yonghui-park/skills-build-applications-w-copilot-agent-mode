from bson import ObjectId
from djongo import models


class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=80)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    performed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'


class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'


class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=120)
    difficulty = models.CharField(max_length=40)
    recommendation_notes = models.TextField()

    class Meta:
        db_table = 'workouts'
