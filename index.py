import requests

def fetch_ip_info(api_url="https://ipinfo.io/json"):
    """Fetch IP information from the ipinfo.io API."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching IP information: {e}")
        return None

def save_ip_info_to_file(ip_info, file_name="ip_info_log.txt"):
    """Save the IP information to a file."""
    try:
        with open(file_name, "a") as file:
            file.write(f"Public IP: {ip_info.get('ip', 'N/A')}\n")
            file.write(f"Location: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}\n")
            file.write(f"ISP: {ip_info.get('org', 'N/A')}\n")
            file.write(f"ASN: {ip_info.get('org', 'N/A')}\n")  # ASN information is in 'org' field for ipinfo.io
            file.write(f"Latitude: {ip_info.get('loc', '').split(',')[0]}\n")
            file.write(f"Longitude: {ip_info.get('loc', '').split(',')[1]}\n")
            file.write("-----------------------------------------\n")
    except Exception as e:
        print(f"Error saving IP information to file: {e}")

def get_ip_info():
    """Retrieve and display IP information, and save it to a file."""
    try:
        ip_info = fetch_ip_info()
        if ip_info is None:
            print("Unable to fetch IP information.")
            return

        # Extract relevant information
        public_ip = ip_info.get("ip", "N/A")
        city = ip_info.get("city", "N/A")
        region = ip_info.get("region", "N/A")
        country = ip_info.get("country", "N/A")
        isp = ip_info.get("org", "N/A")
        asn = ip_info.get("org", "N/A")  # ASN is often embedded in the 'org' field
        loc = ip_info.get("loc", "N/A").split(',')

        lat = loc[0] if len(loc) > 0 else "N/A"
        lon = loc[1] if len(loc) > 1 else "N/A"

        # Display the information
        print(f"Public IP: {public_ip}")
        print(f"Location: {city}, {region}, {country}")
        print(f"ISP: {isp}")
        print(f"ASN: {asn}")
        print(f"Latitude: {lat}, Longitude: {lon}")

        # Save the information to a file
        save_ip_info_to_file(ip_info)

    except Exception as e:
        # General error message for any unexpected failures
        print(f"Error: {e}")

if __name__ == "__main__":
    get_ip_info()
