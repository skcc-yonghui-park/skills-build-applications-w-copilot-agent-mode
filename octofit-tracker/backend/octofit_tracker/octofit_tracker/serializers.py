from rest_framework import serializers

from octofit_tracker.models import Activity, Leaderboard, Team, UserProfile, Workout


class ObjectIdStringRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return str(value.pk)


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description']

    def get_id(self, obj):
        return str(obj.id)


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = ObjectIdStringRelatedField(queryset=Team.objects.all(), allow_null=True, required=False)

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'team']

    def get_id(self, obj):
        return str(obj.id)


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = ObjectIdStringRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'performed_at']
        read_only_fields = ['performed_at']

    def get_id(self, obj):
        return str(obj.id)


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = ObjectIdStringRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'points', 'rank']

    def get_id(self, obj):
        return str(obj.id)


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = ObjectIdStringRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Workout
        fields = ['id', 'user', 'title', 'difficulty', 'recommendation_notes']

    def get_id(self, obj):
        return str(obj.id)
