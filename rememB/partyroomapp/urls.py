from django.urls import path
from . import views

<<<<<<< HEAD:rememB/mainapp/urls.py
<<<<<<< Updated upstream:rememB/mainapp/urls.py
urlpatterns=[
    
]
=======

urlpatterns = [
    path('<int:userpk>/',views.UserLetterView.as_view()), #userpk의 편지만 조회
]
>>>>>>> Stashed changes:rememB/partyroomapp/urls.py
=======

urlpatterns = [
]
>>>>>>> develop:rememB/partyroomapp/urls.py
