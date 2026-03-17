from django.contrib import admin

from octofit_tracker.models import Activity, Leaderboard, Team, UserProfile, Workout

admin.site.register(Team)
admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
