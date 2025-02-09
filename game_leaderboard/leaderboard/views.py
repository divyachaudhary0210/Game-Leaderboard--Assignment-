from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.timezone import now, timedelta
from .models import Contestant, Game, Score
from .serializers import ContestantSerializer, GameSerializer, ScoreSerializer

class ContestantViewSet(viewsets.ModelViewSet):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request, game_id=None):
        scores = Score.objects.filter(game_id=game_id).order_by('-score')
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
