from django.urls import path
from uiapp.views import HomeView, modal, check_comment, list_comment, delete_comment

app_name = 'uiapp'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]

htmx_urlpatterns = [
    path('modal/', modal, name="display-modal"),
    path('list_comment/', list_comment, name='list-comment'),
    path('check_comment/', check_comment, name='check-comment'),
    path('delete_comment/<int:pk>/', delete_comment, name='delete-comment'),
]

urlpatterns += htmx_urlpatterns