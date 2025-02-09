from celery import shared_task
from django.utils.timezone import now, timedelta
from .models import Game, Score

@shared_task
def update_popularity_scores():
    yesterday = now() - timedelta(days=1)
    games = Game.objects.all()
    
    max_daily_players = max_concurrent_players = max_upvotes = max_session_length = max_daily_sessions = 1
    
    for game in games:
        w1 = Score.objects.filter(game=game, timestamp__date=yesterday.date()).count()
        w2 = Score.objects.filter(game=game).count()
        w3 = game.upvotes
        w4 = 10  # Placeholder
        w5 = Score.objects.filter(game=game, timestamp__date=yesterday.date()).count()

        score = (0.3 * (w1 / max_daily_players) +
                 0.2 * (w2 / max_concurrent_players) +
                 0.25 * (w3 / max_upvotes) +
                 0.15 * (w4 / max_session_length) +
                 0.1 * (w5 / max_daily_sessions))

        print(f"Popularity score for {game.name}: {score}")
