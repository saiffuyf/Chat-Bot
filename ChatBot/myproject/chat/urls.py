from django.urls import path
from .views import chatbot, chatbot_response

urlpatterns = [
    path("", chatbot, name="chatbot"),
    path("get-response/", chatbot_response, name="chatbot_response"),
]
