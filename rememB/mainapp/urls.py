from django.urls import path
from . import views

<<<<<<< Updated upstream:rememB/mainapp/urls.py
urlpatterns=[
    
]
=======

urlpatterns = [
    path('<int:userpk>/',views.UserLetterView.as_view()), #userpk의 편지만 조회
]
>>>>>>> Stashed changes:rememB/partyroomapp/urls.py
