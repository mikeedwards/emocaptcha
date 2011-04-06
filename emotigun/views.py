# Create your views here.
from django.views.generic.base import TemplateView

class GameView(TemplateView):
    template_name = "emotigun/game.html"