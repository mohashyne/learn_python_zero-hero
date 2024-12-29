

import requests
import config

url = "https://api.yelp.com/v3/businesses/search"



headers = { 
    "Authorization": f"Bearer {config.api_key}"  # Add a space after "Bearer"
}

params = {
    "term": "food",
    "location": "San Francisco"
}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an error for HTTP issues
    print(response.json())  # Print the JSON response
    businesses = response.json()["businesses"] # Get the businesses
    # for business in businesses:
    #     print(business["name"])
    # refactoring the code
    names = [business["name"]
             for business in businesses if business["rating"] > 4.5]
    print(names)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

