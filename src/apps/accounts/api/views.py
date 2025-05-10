from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login


@api_view(["GET"])
def getRoutes(request):
    routes = ["GET /api/login", "GET /api/register", "GET /api/logout"]
    return Response(routes)


@api_view(["POST"])
def register(request):
    form = UserCreationForm(request.data)
    if form.is_valid():
        user = form.save()
        return Response({"message": "User created successfully"}, status=201)
    return Response({"message": "User creation failed"}, status=400)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return Response({"message": "Login successful"}, status=200)
    return Response({"message": "Login failed"}, status=401)
