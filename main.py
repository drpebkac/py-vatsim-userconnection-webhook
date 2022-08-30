# Libraries for HTTP requests
import requests
import json
import time
import sys
from datetime import datetime

#Global variables
#Pilot CID in scope of webhook
# Discord webhook url
# Displayname for the bot on Discord
cid = sys.argv[1]
url = sys.argv[2]
username = sys.argv[3]

def create_Body():
  if flightplan is None:
    #Content body
    jsoncontent = {
      "username": username,
      "content": "@everyone ATTN CONTROLLERS! " + "***" + name + "***" + " has connected to VATSIM AT " + formatted_time_in_utc,
      "embeds": [
        {
          "fields": [
            {
              "name": "No flight plan has been pre-filed by this user.",
              "value": "Flight details will only show if a flight plan is prefiled through simbrief"
            },
            {
              "name": "Callsign",
              "value": callsign
            }
          ],
          "title": "Flight information"
        }
      ]
    }
  else:
    #Content body
    jsoncontent = {
      "username": username,
      "content": "ATTN CONTROLLERS! " + "***" + name + "***" + " has connected to VATSIM AT " + formatted_time_in_utc,
      "embeds": [
        {
          "fields": [
            {
              "name": "Callsign",
              "value": callsign
            },
            {
              "name": "Aircraft",
              "value": aircraft
            },
            {
              "name": "Departure",
              "value": dep
            },
            {
              "name": "Arrival",
              "value": arr
            },
            {
              "name": "Alternative",
              "value": alternative
            },
            {
              "name": "Cruise Alt",
              "value": cruising_alt
            },
            {
              "name": "RMKS",
              "value": rmks
            },
            {
              "name": "Route",
              "value": route
            }
          ],
          "title": "Flight information"
        }
      ]
    }

  # Send body to webhook
  requests.post(url, json = jsoncontent)

################################################################################

#Declare anti loop function variable
functionstatus = "Offline"

while True:

  # Fetch live Vatsim data
  rawvatdata = requests.get("https://data.vatsim.net/v3/vatsim-data.json")

  # Convert response type to json
  outputtojson = json.loads(rawvatdata.content)

  # Expand into json array of pilots
  pilotarray = outputtojson['pilots']

  for x in pilotarray:
    cidnumber = x['cid']

    if cid in str(cidnumber):
      print(cid + " Is online")

      if functionstatus == "Offline":
        name = x['name']
        callsign = x['callsign']
        flightplan = x['flight_plan']
        squawk = x['transponder']
        functionstatus = "Online"

        if flightplan is not None:
          aircraft = flightplan['aircraft']
          dep = flightplan['departure']
          arr = flightplan['arrival']
          alternative = flightplan['alternate']
          cruising_alt = flightplan['altitude']
          rmks = flightplan['remarks']
          route = flightplan['route']

        #UTC time now
        time_in_utc = datetime.utcnow()
        formatted_time_in_utc = time_in_utc.strftime("%H%Mz")
        create_Body()
    else: 
      functionstatus == "Offline"
  time.sleep(15.0)
