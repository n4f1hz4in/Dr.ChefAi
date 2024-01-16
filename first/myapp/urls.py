from django.urls import path,include
from. import views
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.index ,name='index'),
    path('home/', views.home, name='home'),
    path("regPage/",views.regView,name='regPage'),
    path('regdata/',views.regData,name='regdata'),
    path('loginPage/',views.loginView,name='loginPage'),
    path('logindata/',views.loginData,name='logindata'),
    
    path('logout/',LogoutView.as_view(next_page='/'),name='logout'),

    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

    path('reset_password/',auth_views.PasswordResetView.as_view(),
         name='reset_password'),#template_name='password_reset_form.html'
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('chatbotPage/',views.chatbotView,name='chatbotPage'),

    path('faqPage/',views.faqView,name='faqPage'),

    path('aboutPage/',views.aboutView,name='aboutPage'),

    path('textPage/',views.textView,name='textPage'),

    

]
