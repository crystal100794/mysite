
from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('hero/all', views.hero_wiew, name='hero_view_list'),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls',))
]