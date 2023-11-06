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
        print(f"Failed to retrieve the IP address. Status code: {response.status}")
    else:
        # Decode the response content as text
        ipInfo = json.loads(response.data.decode('utf-8'))
        #print(ipInfo)
        # Print the flag based on the ip location
        with open(f"flags/{ipInfo['country']}", "r") as file:
            sys.stdout.write(f"\n{file.read().strip()} ")
            sys.stdout.write(f"\033[2C\033[s \033[9A IP: {ipInfo['ip']}")
            sys.stdout.write(f"\033[u\033[8A  Continent: {ipInfo['continent_code']}")
            sys.stdout.write(f"\033[u\033[7A  Country: {ipInfo['country']}")
            sys.stdout.write(f"\033[u\033[6A  Region: {ipInfo['country']}")
            sys.stdout.write(f"\033[u\033[5A  City: {ipInfo['country']}")
            sys.stdout.write(f"\033[u\033[4A  ISP: {ipInfo['organization']}")
            sys.stdout.write(f"\033[u\033[3A  Timezone: {ipInfo['timezone']}")
            sys.stdout.write(f"\033[u\033[2A  Latitude: {ipInfo['latitude']}")
            sys.stdout.write(f"\033[u\033[1A  Longitude: {ipInfo['longitude']}")
            sys.stdout.write(f"\033[u  ASN: {ipInfo['asn']}")
            sys.stdout.write(f"\033[u \033[10A --------------------")
            sys.stdout.write(f"\033[u \n\n")


# Check if the -ip switch is used
if args.ip != None:
    IPcheck(isIPspecified=True)
    exit()

IPcheck()


# TODO: fix the space in the name of the countries: replace them with underscore
# TODO: write a message for when the response code is 401: {"code":401,"message":"Input string is not a valid IP address"}
# TODO: print the help when the "-ip" switch is used but no ip has given
# TODO: fix the case when the ip does not have some of the fields like region or etc... in the database and print "Unknown" instead of it
# TODO: choose better fields for the ip info
