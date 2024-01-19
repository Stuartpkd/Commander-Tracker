from django.views.generic.detail import DetailView
from home.models import Card


class CardDetailView(DetailView):
    model = Card
    template_name = 'home/card_detail.html'  # Replace with your template path
    context_object_name = 'card'
