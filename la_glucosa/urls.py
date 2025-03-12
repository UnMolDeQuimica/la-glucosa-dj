from django.urls import path
from .views import *

urlpatterns = [
    path('glucose-records/', view=ListGlucoseRecord.as_view(), name="glucose_records"),
    path('glucose-create/', view=CreateGlucoseRecord.as_view(), name="glucose_create"),
    path('glucose-delete/<int:pk>', view=DeleteGlucoseRecord.as_view(), name="glucose_delete"),
    path('glucose-update/<int:pk>', view=UpdateGlucoseRecord.as_view(), name="glucose_update"),
]
