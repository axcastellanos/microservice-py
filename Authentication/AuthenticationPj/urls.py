"""AuthenticationPj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from ApiAuth.views import userViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('loginUser/',TokenObtainPairView.as_view()),
    path('refreshToken/',TokenRefreshView.as_view()),

    path('createUser/',userViews.UserCreateView.as_view()),
    path('detailSingleUser/<int:pk>/',userViews.UserDetailView.as_view()),
    path('detailListUser/<int:pk>/',userViews.UserListView.as_view()),
    path('updateUser/<int:pk>/',userViews.UserUpdateView.as_view()),
    path('deleteUser/<int:pk>/',userViews.UserDeleteView.as_view()),

]
