from django.urls import path
from . import views


urlpatterns = [
    path("soya1/<int:id1>", views.func_one),
    path("soya1/<int:id1>/<int:id2>", views.func_two),
    path("soya1/<int:id1>/<int:id2>/<int:id3>", views.func_three),
    path("soya1/<int:id1>/<int:id2>/<int:id3>/<int:id4>", views.func_four),
]



