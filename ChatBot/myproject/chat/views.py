from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import re

def chatbot(request):
    return render(request, "chatbot.html")

def chatbot_response(request):
    user_input = request.GET.get("message", "").strip().lower()

    if user_input == "hello":
        response = "Hi there! How can I help you today?"
    elif user_input == "integer":
        response = "Please enter a list of integers (comma-separated):"
    elif re.match(r"^\d+(,\s*\d+)*$", user_input):  # Check if input is a list of integers
        numbers = list(map(int, user_input.split(",")))
        response = f"Sum: {sum(numbers)}\nMaximum: {max(numbers)}\nReversed List: {list(reversed(numbers))}"
    elif user_input in ["thanks", "thank you"]:
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm sorry, I didn't understand that. Can you rephrase?"

    return JsonResponse({"response": response})
