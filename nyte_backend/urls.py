"""nyte_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as drf_views
from django.conf import settings
from django.conf.urls.static import static
from api.views import NyteUserViewset, UserReloadsViewset, UserOrdersViewset, VenueViewset, VenueMenuItemViewset, VenueOptionsViewset, VenueOrdersViewset, VenueTransactionsViewsets
from rest_framework_nested import routers as nested_routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

scheme_view = schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

user_router = nested_routers.DefaultRouter()
user_router.register("users", NyteUserViewset)
user_reload_router = nested_routers.NestedDefaultRouter(user_router, 'users', lookup='users')
user_reload_router.register('reloads', UserReloadsViewset, base_name="user-reloads")
user_orders_router = nested_routers.NestedDefaultRouter(user_router, 'users', lookup='users')
user_orders_router.register('orders', UserOrdersViewset, base_name='UserOrdersViewset')

venue_router = nested_routers.DefaultRouter()
venue_router.register('venues', VenueViewset)
venue_menu_item_router = nested_routers.NestedDefaultRouter(venue_router, 'venues', lookup='venues')
venue_menu_item_router.register("menu_items", VenueMenuItemViewset, base_name="venue-menu-items")
venue_options_router = nested_routers.NestedDefaultRouter(venue_router, 'venues', lookup='venues')
venue_options_router.register("options", VenueOptionsViewset, base_name="venue-options")
venue_orders_router = nested_routers.NestedDefaultRouter(venue_router, 'venues', lookup='venues')
venue_orders_router.register("orders", VenueOrdersViewset, base_name="venue-orders")
venue_transactions_router = nested_routers.NestedDefaultRouter(venue_router, 'venues', lookup='venues')
venue_transactions_router.register("transactions", VenueTransactionsViewsets, base_name="venue-transactions")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('api/', include('api.urls')),
    path("api/v1/", include(user_router.urls)),
    path("api/v1/", include(user_reload_router.urls)),
    path("api/v1/", include(user_orders_router.urls)),
    path("api/v1/", include(venue_router.urls)),
    path("api/v1/", include(venue_menu_item_router.urls)),
    path("api/v1/", include(venue_options_router.urls)),
    path("api/v1/", include(venue_orders_router.urls)),
    path("api/v1/", include(venue_transactions_router.urls)),
]
