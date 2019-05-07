from django.urls import path
from . import views

urlpatterns = [
    path('Account/', views.AccountDetail),
    path('Account/<int:pk>', views.AccountList),
    path('AccountInformation/', views.AccountInformationDetail),
    path('AccountInformation/<int:pk>', views.AccountInformationList),
    path('Event/', views.EventDetail),
    path('Event/<int:pk>', views.EventList),
    path('Identity/', views.IdentityDetail),
    path('Identity/<int:pk>', views.IdentityList),
    path('MenuItem/', views.MenuItemDetail),
    path('MenuItem/<int:pk>', views.MenuItemList),
    path('NyteUser/', views.NyteUserDetail),
    path('NyteUser/<int:pk>', views.NyteUserList),
    path('Special/', views.SpecialDetail),
    path('Special/<int:pk>', views.SpecialList),
    path('Transaction/', views.TransactionDetail),
    path('Transaction/<int:pk>', views.TransactionList),
    path('UserSession/', views.UserSessionDetail),
    path('UserSession/<int:pk>', views.UserSessionList),
    path('Venue/', views.VenueDetail),
    path('Venue/<int:pk>', views.VenueList),
    path('WorksAt/', views.WorksAtDetail),
    path('WorksAt/<int:pk>', views.WorksAtList),
]