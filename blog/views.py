from django.views.generic import DetailView, ListView
from .models import Category


class CategoryListView(ListView):
    model = Category

    def get_same_level_category(self):
        if self.parent_category:
            return self.parent_category.category_set.all().exclude(id=self.id)


class CategoryDetailView(DetailView):
    model = Category

    def get_same_level_category(self):
        if self.parent_category:
            return self.parent_category.category_set.all().exclude(id=self.id)