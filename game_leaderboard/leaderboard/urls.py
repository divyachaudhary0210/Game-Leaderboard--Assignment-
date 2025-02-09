from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContestantViewSet, GameViewSet, ScoreViewSet, LeaderboardViewSet

router = DefaultRouter()
router.register(r'contestants', ContestantViewSet)
router.register(r'games', GameViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('leaderboard/<int:game_id>/', LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard'),
]
