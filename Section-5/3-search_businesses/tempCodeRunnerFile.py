try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for HTTP issues
    print(response.json())  # Print the JSON response
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
