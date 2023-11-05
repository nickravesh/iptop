import sys
import json
import urllib3

# Create a connection pool for making HTTP requests
http = urllib3.PoolManager()

# Send an HTTP GET request to fetch the public IP address
response = http.request("GET", "https://api.seeip.org/geoip/")

# Check if the request was unsuccessful
if response.status != 200:
    print(f"Failed to retrieve the IP address. Status code: {response.status}")
else:
    # Decode the response content as text
    ipInfo = json.loads(response.data.decode('utf-8'))

    # Print the flag based on the ip location
    with open(f"flags/{ipInfo['country']}", "r") as file:
        sys.stdout.write(f"\n{file.read().strip()} ")
        sys.stdout.write(f"\033[2C\033[s \033[9A IP: {ipInfo['ip']}")
        sys.stdout.write(f"\033[u\033[8A  Continent: {ipInfo['continent_code']}")
        sys.stdout.write(f"\033[u\033[7A  Country: {ipInfo['country']}")
        sys.stdout.write(f"\033[u\033[6A  Region: {ipInfo['region']}")
        sys.stdout.write(f"\033[u\033[5A  City: {ipInfo['city']}")
        sys.stdout.write(f"\033[u\033[4A  ISP: {ipInfo['organization']}")
        sys.stdout.write(f"\033[u\033[3A  Timezone: {ipInfo['timezone']}")
        sys.stdout.write(f"\033[u\033[2A  Latitude: {ipInfo['latitude']}")
        sys.stdout.write(f"\033[u\033[1A  Longitude: {ipInfo['longitude']}")
        sys.stdout.write(f"\033[u  ASN: {ipInfo['asn']}")
        sys.stdout.write(f"\033[u \033[10A --------------------")
        sys.stdout.write(f"\033[u \n\n")
