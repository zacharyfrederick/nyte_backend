from django.urls import path
from . import views
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('Account/', views.AccountList.as_view()),
    path('Account/<int:pk>', views.AccountDetail.as_view()),
    path('AccountInformation/', views.AccountInformationList.as_view()),
    path('AccountInformation/<int:pk>', views.AccountInformationDetail.as_view()),
    path('Event/', views.EventList.as_view()),
    path('Event/<int:pk>', views.EventDetail.as_view()),
    path('Identity/', views.IdentityList.as_view()),
    path('Identity/<int:pk>', views.IdentityDetail.as_view()),
    path('MenuItem/', views.MenuItemList.as_view()),
    path('MenuItem/<int:pk>', views.MenuItemDetail.as_view()),
    path('NyteUser/', views.NyteUserList.as_view()),
    path('NyteUser/<int:pk>', views.NyteUserDetail.as_view()),
    path('Special/', views.SpecialList.as_view()),
    path('Special/<int:pk>', views.SpecialDetail.as_view()),
    path('Transaction/', views.TransactionList.as_view()),
    path('Transaction/<int:pk>', views.TransactionDetail.as_view()),
    path('UserSession/', views.UserSessionList.as_view()),
    path('UserSession/<int:pk>', views.UserSessionDetail.as_view()),
    path('Venue/', views.VenueList.as_view()),
    path('Venue/<int:pk>', views.VenueDetail.as_view()),
    path('WorksAt/', views.WorksAtList.as_view()),
    path('WorksAt/<int:pk>', views.WorksAtDetail.as_view()),
    path('Login/', drf_views.obtain_auth_token),
    path('CreateNyteUser/', views.CreateNyteUser.as_view()),
    path('ProtoMenuItem/', views.ProtoMenuItemList.as_view()),
    path('ProtoMenuItem/<int:pk>', views.ProtoMenuItemDetail.as_view()),
    path('ProtoOrder/', views.ProtoOrderList.as_view()),
    path('ProtoOrder/<int:pk>', views.ProtoOrderDetail.as_view()),
    path('FacebookLogin/', views.login_view),
    path('FacebookLogout/', views.fb_logout_view),
    path('Verification/', views.VerificationCreation.as_view()),
    path('VerificationUpdate/<int:pk>', views.VerificationUpdate.as_view()),
    path('VerificationID/', views.VerificationIdUpload.as_view())
]