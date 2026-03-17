from django.contrib import admin

from octofit_tracker.models import Activity, Leaderboard, Team, UserProfile, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ('name',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'team')
	search_fields = ('name', 'email')
	list_filter = ('team',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('user', 'activity_type', 'duration_minutes', 'calories_burned', 'performed_at')
	search_fields = ('user__name', 'activity_type')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
	list_display = ('user', 'points', 'rank')
	ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
	list_display = ('user', 'title', 'difficulty')
	search_fields = ('user__name', 'title', 'difficulty')
