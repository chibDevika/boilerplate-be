from django.urls import path
from leavestracker.apps.leaves.views import LeavesView

urlpatterns = [
    path('leaves/', LeavesView.as_view(), name="leaves"),
    path('leaves/<int:id>',LeavesView.as_view(), name="leaves"),
    path('leaves/<str:start>/<str:end>',LeavesView.as_view(), name="leaves"),
]
