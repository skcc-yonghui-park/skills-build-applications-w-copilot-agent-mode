from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, Leaderboard, Team, UserProfile, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        marvel_team = Team.objects.create(name='marvel 팀', description='Marvel 슈퍼히어로 팀')
        dc_team = Team.objects.create(name='dc 팀', description='DC 슈퍼히어로 팀')

        heroes = [
            {'name': 'Iron Man', 'email': 'ironman@octofit.dev', 'team': marvel_team},
            {'name': 'Captain America', 'email': 'captain@octofit.dev', 'team': marvel_team},
            {'name': 'Thor', 'email': 'thor@octofit.dev', 'team': marvel_team},
            {'name': 'Batman', 'email': 'batman@octofit.dev', 'team': dc_team},
            {'name': 'Superman', 'email': 'superman@octofit.dev', 'team': dc_team},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@octofit.dev', 'team': dc_team},
        ]

        user_objects = []
        for hero in heroes:
            user_objects.append(
                UserProfile.objects.create(
                    name=hero['name'],
                    email=hero['email'],
                    team=hero['team'],
                )
            )

        for idx, user in enumerate(user_objects, start=1):
            Activity.objects.create(
                user=user,
                activity_type='Running',
                duration_minutes=30 + idx,
                calories_burned=250 + (idx * 15),
            )
            Activity.objects.create(
                user=user,
                activity_type='Strength Training',
                duration_minutes=20 + idx,
                calories_burned=180 + (idx * 10),
            )

            Workout.objects.create(
                user=user,
                title='Hero HIIT Routine',
                difficulty='Medium',
                recommendation_notes=f'{user.name} 전용 인터벌 루틴',
            )

            Leaderboard.objects.create(
                user=user,
                points=1200 - (idx * 50),
                rank=idx,
            )

        self.stdout.write(self.style.SUCCESS('테스트 데이터 입력이 완료되었습니다.'))
