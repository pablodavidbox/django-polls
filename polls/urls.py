from django.urls import path
from . import views


app_name = 'polls'  # 👈 ¡Esta línea es clave!

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("owner", views.owner, name="owner"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
