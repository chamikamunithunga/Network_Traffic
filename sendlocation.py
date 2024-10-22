import requests

def send_location(phone_number, latitude, longitude):
    url = "http://127.0.0.1:5000/send_location"
    data = {
        "phone_number": phone_number,
        "latitude": latitude,
        "longitude": longitude
    }
    
    try:
        
        response = requests.post(url, json=data, proxies={"http": None, "https": None})
        response.raise_for_status()  
        print("Location sent successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error sending location:", e)


phone_number = "+94123456789"  
latitude = "6.9271"  
longitude = "79.9612"  

send_location(phone_number, latitude, longitude)
