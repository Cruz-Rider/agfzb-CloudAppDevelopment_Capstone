import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)

def get_dealers_from_cf(url, **kwargs):
    results = []
    json_result = get_request(url)
    if json_result:
        dealers = json_result
        for dealer in dealers:
            dealer_doc = dealer
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"], state=dealer_doc["state"], 
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results

def get_dealer_by_id(url, **kwargs):
    result =[]
    json_result = get_request(url, id=dealer_id)
    if json_result:
        dealers = json_result
        for dealer in dealers:
            dealer_doc = dealer
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"], state=dealer_doc["state"], 
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)
    
    return results

def get_dealer_by_state(url, **kwargs):
    result = []
    json_result = get_request(url, state=state)
    if json_result:
        dealers = json_result
        for dealer in dealers:
            dealer_doc = dealer
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"], state=dealer_doc["state"], 
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)
    
    return results

def get_dealer_reviews_from_cf(url, **kwargs):
    results = []
    dealer_id = kwargs['dealer_id']
    json_result = get_request(url, id=dealer_id)
    if json_result:
        dealer_reviews = json_result
        for dealer_review in dealer_reviews:
            dealer_doc = dealer_review
            dealer_obj = DealerReview(name=dealer_doc["name"], dealership=dealer_doc["dealership"], review=dealer_doc["review"],
                                   id=dealer_doc["id"], purchase=dealer_doc["purchase"], purchase_date=dealer_doc["purchase_date"],
                                   car_make=dealer_doc["car_make"], car_model=dealer_doc["car_model"], 
                                   car_year=dealer_doc["car_year"])
            dealer_obj.sentiment = analyze_review_sentiments(dealer_obj.review)
            results.append(dealer_obj)
    
    return results

def analyze_review_sentiments(dealer_review):
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/5b62aed3-bdd1-4d2a-8f0a-d41f4c7f1f72"
    api_key = "dmVrOJvFaOsZh_oTvmW5faOJj1TFa-_Hgr0wj8OWNSXa"
    params= {
        "text": "dealer_review",
        "version":"2019-07-12",
        "features": {
            "sentiment": {}
        },
        "return_analyzed_text": "true"
    }
    response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                auth=HTTPBasicAuth('apikey', api_key))
    sentiment_data = response.json()
    return sentiment_data
