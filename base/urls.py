"""
apppppppppppppppppppppppplication urls
"""
from django.urls import path
from base.views import MyTokenObtainPairView, addProducts, myProducts, register, APIViews, deleteProd
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('login', MyTokenObtainPairView.as_view()),
    path('register', register),
    path('myProducts', myProducts),
    path('addProducts', addProducts),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload_image/', APIViews.as_view()),
    path('deleteProd/<int:id>', deleteProd)
]