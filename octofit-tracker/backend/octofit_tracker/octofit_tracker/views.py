from rest_framework import viewsets

from octofit_tracker.models import Activity, Leaderboard, Team, UserProfile, Workout
from octofit_tracker.serializers import (
    ActivitySerializer,
    LeaderboardSerializer,
    TeamSerializer,
    UserProfileSerializer,
    WorkoutSerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('name')
    serializer_class = UserProfileSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-performed_at')
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all().order_by('rank')
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all().order_by('title')
    serializer_class = WorkoutSerializer
