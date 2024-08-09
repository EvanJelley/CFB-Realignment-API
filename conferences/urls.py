from django.urls import path
from .views import (
    AllConferenceByYearList, 
    ConferenceByYearDetail,
    ConferenceWithLogoList,
    SchoolWithLogoList
    )


urlpatterns = [
    path('conferencebyyear/', AllConferenceByYearList.as_view()),
    path('conferencebyyear/<int:pk>/', ConferenceByYearDetail.as_view()),
    path('conferences/', ConferenceWithLogoList.as_view()),
    path('schools/', SchoolWithLogoList.as_view())
]