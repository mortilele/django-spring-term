from rest_framework import routers

from main import views

router = routers.DefaultRouter()
router.register(r'todos', views.ToDoGroupViewSet)

urlpatterns = [

]

urlpatterns += router.urls
