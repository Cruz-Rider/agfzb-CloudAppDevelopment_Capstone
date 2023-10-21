from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarMake, CarModel, CarDealer, DealerReview
from .restapis import get_request, get_dealers_from_cf, get_dealer_reviews_from_cf
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

logger = logging.getLogger(__name__)


def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)

def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
    else:
        return render(request, 'djangoapp/index.html', context)

def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

def get_dealerships(request):
    if request.method == "GET":
        context = {}
        url = "https://u1999shishir-3000.theiadocker-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealerships/get"
        dealerships = get_dealers_from_cf(url)
        context = {'dealerships': dealerships}
        return render(request, 'djangoapp/index.html', context)

def about(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/about.html', context)

def contact(request):
    if request.method == 'GET':
        return render(request, 'djangoapp/contact.html')

def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        context = {}
        url = "https://u1999shishir-5000.theiadocker-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/api/get_reviews"
        dealer_details = get_dealer_reviews_from_cf(url, dealer_id=dealer_id)
        context = {'dealer_details': dealer_details}
        # dealer_reviews = ' '.join([detail.review for detail in dealer_details])
        # review_sentiment = [detail.sentiment for detail in dealer_details]
        # sentiment_score = review_sentiment[0]['score'] # print(review_sentiment[0]['score'])
        # sentiment_label = review_sentiment[0]['label'] # print(review_sentiment[0]['label'])

        #result = "Review: " + dealer_reviews + ", " \
                #"Sentiment: " + sentiment_label 
        return render(request, 'djangoapp/dealer_details.html', context) 

@login_required
def add_review(request, dealer_id):
    if request.method == 'POST':
        url = "https://u1999shishir-5000.theiadocker-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/api/post_review"
        if request.user.is_authenticated:
            print("AUthenticated User")
            
            review = {
                'id': 6,
                'name': 'Shishir Shukla', 
                'dealership': dealer_id, 
                'review': 'Lovely car with large capacity and seating space. Best-suited for big families!', 
                'purchase': true, 
                'purchase_date': datetime.date.today(), 
                'car_make': 'Lamborghini', 
                'car_model': 'Gallado', 
                'car_year': 2012
            }
            json_payload = {
                'review': review
            }

            post_review = post_request(url, json_payload)
            return HttpResponse(post_review)
        else:
            print("Unauthenticated")
