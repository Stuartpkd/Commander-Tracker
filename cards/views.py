from django.views.generic.detail import DetailView
from home.models import Card
from profiles.models import Category


class CardDetailView(DetailView):
    model = Card
    template_name = 'card_detail/card_detail.html'
    context_object_name = 'card'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add categories to the context
        if self.request.user.is_authenticated:
            context['categories'] = Category.objects.filter(user=self.request.user)
        return context
