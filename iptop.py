import sys
import json
import urllib3
import argparse

# Setup argparse
parser = argparse.ArgumentParser(description="iptop, The CLI tool for inspecting your IP info")
parser.add_argument("-ip", type=str, nargs="+", help="Lookup a specific IP address instead of yours.")
args = parser.parse_args()


def IPcheck(isIPspecified: bool=False):
    # Create a connection pool for making HTTP requests
    http = urllib3.PoolManager()

    # Send an HTTP GET request to fetch the public IP address
    if isIPspecified == True:
        response = http.request("GET", f"https://api.seeip.org/geoip/{args.ip[0]}")
    else:
        response = http.request("GET", "https://api.seeip.org/geoip/")

    # Check if the request was unsuccessful
    if response.status != 200:
        if json.loads(response.data.decode('utf-8'))['code'] == 401:
            print(f"Input string is not a valid IP address. Status code: 401")
        else:
            print(f"Failed to retrieve the IP address. Status code: {response.status}")
    else:
        # Decode the response content as text
        ipInfo:dict = json.loads(response.data.decode('utf-8'))

        # Print the flag based on the ip location
        with open(f"flags/{ipInfo.get('country', 'Unknown').replace(' ', '_')}", "r") as file:
            sys.stdout.write(f"\n{file.read().strip()} ")
            sys.stdout.write(f"\033[2C\033[s \033[9A IP: {ipInfo.get('ip', 'unknown')}")
            sys.stdout.write(f"\033[u\033[8A  Continent: {ipInfo.get('continent_code', 'unknown')}")
            sys.stdout.write(f"\033[u\033[7A  Country: {ipInfo.get('country', 'unknown').replace('_', ' ')}")
            sys.stdout.write(f"\033[u\033[6A  Region: {ipInfo.get('region', 'unknown')}")
            sys.stdout.write(f"\033[u\033[5A  City: {ipInfo.get('city', 'unknown')}")
            sys.stdout.write(f"\033[u\033[4A  ISP: {ipInfo.get('organization', 'unknown')}")
            sys.stdout.write(f"\033[u\033[3A  Timezone: {ipInfo.get('timezone', 'unknown')}")
            sys.stdout.write(f"\033[u\033[2A  Latitude: {ipInfo.get('latitude', 'unknown')}")
            sys.stdout.write(f"\033[u\033[1A  Longitude: {ipInfo.get('longitude', 'unknown')}")
            sys.stdout.write(f"\033[u  ASN: {ipInfo.get('asn', 'unknown')}")
            sys.stdout.write(f"\033[u \033[10A --------------------")
            sys.stdout.write(f"\033[u \n\n")


# Check if the -ip switch is used
if args.ip != None:
    IPcheck(isIPspecified=True)
    exit()

IPcheck()


# TODO: choose better fields for the ip info
