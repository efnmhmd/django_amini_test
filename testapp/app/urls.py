from django.urls import path
from .views import test,test2,test3,Test4,Test5,Test6,Test7,Test8,APITest1,APITest2,APITest3,APITest4,APITest5,APITest6,APITest7
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
   path('',test),
   path('time/',test),
   path ('test2/',test2),
   path ('test3/<str:adad>/',test3),
   path ('test4/',Test4.as_view()),
   path ('test5/',Test5.as_view()),
   path ('test6/',Test6.as_view()),
   path ('test7/',Test7.as_view()),
   path ('test8/',Test8.as_view()),


   path ('api_test1/',APITest1.as_view()),
   path ('api_test2/',APITest2.as_view()),
   path ('api_test3/',APITest3.as_view()),
   path ('api_test4/',APITest4.as_view()),
   path ('api_test5/<int:pk>/',APITest5.as_view()),
   path ('api_test6',APITest6.as_view()),
   path ('api_test7/<int:pk>/',APITest7.as_view()),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]