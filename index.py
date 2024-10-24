import requests

def get_ip_info():
    url = "https://ipapi.co/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        ip_info = response.json()

        # Extract relevant information
        public_ip = ip_info.get("ip","N/A")
        city = ip_info.get("city","N/A")
        region = ip_info.get("region","N/A")
        country = ip_info.get("country","N/A")
        isp = ip_info.get("org","N/A")
        asn = ip_info.get("asn","N/A")
        lat = ip_info.get("latitude", "N/A")
        lon = ip_info.get("longitude", "N/A")

        # Display the information
        print(f"Public IP: {public_ip}")
        print(f"Location: {city}, {region}, {country}")
        print(f"ISP: {isp}")
        print(f"ASN: {asn}")
        print(f"Latitude: {lat}, Longitude: {lon}")

    except requests.RequestException as e:
        print(f"Error retrieving IP information: {e}")

if __name__ == "__main__":
    get_ip_info()
