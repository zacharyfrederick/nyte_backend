from django.urls import path
from . import views
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('Account/', views.AccountDetail.as_view()),
    path('Account/<int:pk>', views.AccountList.as_view()),
    path('AccountInformation/', views.AccountInformationDetail.as_view()),
    path('AccountInformation/<int:pk>', views.AccountInformationList.as_view()),
    path('Event/', views.EventDetail.as_view()),
    path('Event/<int:pk>', views.EventList.as_view()),
    path('Identity/', views.IdentityDetail.as_view()),
    path('Identity/<int:pk>', views.IdentityList.as_view()),
    path('MenuItem/', views.MenuItemDetail.as_view()),
    path('MenuItem/<int:pk>', views.MenuItemList.as_view()),
    path('NyteUser/', views.NyteUserDetail.as_view()),
    path('NyteUser/<int:pk>', views.NyteUserList.as_view()),
    path('Special/', views.SpecialDetail.as_view()),
    path('Special/<int:pk>', views.SpecialList.as_view()),
    path('Transaction/', views.TransactionDetail.as_view()),
    path('Transaction/<int:pk>', views.TransactionList.as_view()),
    path('UserSession/', views.UserSessionDetail.as_view()),
    path('UserSession/<int:pk>', views.UserSessionList.as_view()),
    path('Venue/', views.VenueDetail.as_view()),
    path('Venue/<int:pk>', views.VenueList.as_view()),
    path('WorksAt/', views.WorksAtDetail.as_view()),
    path('WorksAt/<int:pk>', views.WorksAtList.as_view()),
]