from rest_framework import routers

from main import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'journals', views.JournalViewSet)

urlpatterns = [

]

urlpatterns += router.urls
