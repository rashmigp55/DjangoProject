from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import UserDetails  # Ensure this is your custom user model
from .serializers import UserDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = UserDetails.objects.get(email=email)
            # Check the hashed password
            if check_password(password, user.password):
                #messages.success(request, "Login successful!")
                return render(request, 'success.html')  # Redirect to a success page
            else:
                messages.error(request, "Invalid email or password.")
        except UserDetails.DoesNotExist:
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if email already exists
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'signup.html')

        # Create new user with hashed password
        hashed_password = make_password(password)
        new_user = UserDetails(username=username, email=email, password=hashed_password)
        new_user.save()
        messages.success(request, 'Signup successful! You can now log in.')
        return render(request, 'login.html')  # Redirect to the login page after successful signup

    return render(request, 'signup.html')

def success_view(request):
    return render(request, 'success.html')  # Ensure this template exists

from django.http import JsonResponse

@api_view(['GET'])
def get_all_users(request):
    users = UserDetails.objects.all()
    serializer = UserDetailsSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)  # Set safe=False to allow non-dict objects (lists)


@api_view(['GET'])
def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)  # Retrieve user by email
        serializer = UserDetailsSerializer(user)
        return JsonResponse(serializer.data, safe=False)  # Return user data as JSON
    except UserDetails.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

# Create a new user (CREATE)
@api_view(['POST'])
def create_user(request):
    serializer = UserDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update User Details
@csrf_exempt
def update_user(request, pk):
    if request.method == 'PUT':
                try:
                    user= UserDetails.objects.get(pk=pk)#get primary key data single user baed on primery key
                    input_data=json.loads(request.body)
                    serializer_data=UserDetailsSerializer(user,data=input_data)
                    if serializer_data.is_valid():
                        serializer_data.save()#saving to database
                        return JsonResponse({
                            "Success":True,
                            "message":"Data saved successfully",
                            "data":serializer_data.data
                            },status=200)
                    else:
                        return JsonResponse(serializer_data.errors,status=400)
                except Exception as e:
                    return JsonResponse(
                    {
                        "ERROR": str(e)
                    },status=500
                )
        



# Delete a user by email (DELETE)
# Delete User
@api_view(['DELETE'])
def delete_user(request, email):
    if request.method == 'DELETE':
        try:
            user = UserDetails.objects.get(email=email)  # Get user by email
            user.delete()  # Delete the user from the database
            return JsonResponse({"message": "User deleted successfully"}, status=204)  # Successful deletion
        except UserDetails.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)  # User not found error
        except Exception as e:
            return JsonResponse({"ERROR": str(e)}, status=500)  # General error handling
