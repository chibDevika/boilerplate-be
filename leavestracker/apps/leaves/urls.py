from django.urls import path
from leavestracker.apps.leaves.views import LeavesView

urlpatterns = [
    path('leaves-data/', LeavesView.as_view(), name="leaves-data"),
    path('leaves-data/<int:id>',LeavesView.as_view(), name="leaves-data"),
]
