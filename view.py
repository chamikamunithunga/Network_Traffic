import requests
import webbrowser

def view_location_on_maps(phone_number):
    url = f'http://127.0.0.1:5000/view_location/{phone_number}'
    response = requests.get(url)
    
    if response.status_code == 200:
        location = response.json()
        latitude = location['latitude']
        longitude = location['longitude']
        
        
        maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(f"Opening location in Google Maps: {maps_url}")
        
        
        webbrowser.open(maps_url)
    else:
        print("Location not found for this phone number.")


phone_number = "+94123456789"
view_location_on_maps(phone_number)
