import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from octofit_tracker.views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    UserProfileViewSet,
    WorkoutViewSet,
)

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workouts')


API_ENDPOINTS = {
    'users': '/api/users/',
    'teams': '/api/teams/',
    'activities': '/api/activities/',
    'leaderboard': '/api/leaderboard/',
    'workouts': '/api/workouts/',
}


@api_view(['GET'])
def api_root(request):
    return Response({name: f'{base_url}{path}' for name, path in API_ENDPOINTS.items()})

urlpatterns = [
    path('', api_root, name='root-api'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
