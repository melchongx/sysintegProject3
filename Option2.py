import requests

def get_ip_info():
    # Using ipapi.co API to fetch public IP information
    ip_api_url = "https://ipapi.co/json/"
    response = requests.get(ip_api_url)
    
    if response.status_code == 200:
        ip_data = response.json()
        ipv4 = ip_data.get("ip", "N/A")
        city = ip_data.get("city", "N/A")
        region = ip_data.get("region", "N/A")
        country = ip_data.get("country_name", "N/A")
        isp = ip_data.get("org", "N/A")
        asn = ip_data.get("asn", "N/A")
        lat = ip_data.get("latitude", "N/A")
        lon = ip_data.get("longitude", "N/A")

        # Displaying the results
        print(f"IPv4 Address: {ipv4}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"ISP: {isp}")
        print(f"ASN: {asn}")
        print(f"Latitude: {lat}, Longitude: {lon}")
        
    else:
        print("Error: Unable to retrieve IP information.")

if __name__ == "__main__":
    get_ip_info()
