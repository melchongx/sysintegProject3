import requests

def get_ip_info():
    url = "https://ipapi.co/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        ip_info = response.json()

        # Extract relevant information
        public_ip = ip_info.get("ip")
        city = ip_info.get("city")
        region = ip_info.get("region")
        country = ip_info.get("country")
        isp = ip_info.get("org")
        asn = ip_info.get("asn")

        # Display the information
        print(f"Public IP: {public_ip}")
        print(f"Location: {city}, {region}, {country}")
        print(f"ISP: {isp}")
        print(f"ASN: {asn}")

    except requests.RequestException as e:
        print(f"Error retrieving IP information: {e}")

if __name__ == "__main__":
    get_ip_info()
