# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:24:03 2020

@author: 612820232/Chris Brown
"""
import base64
import requests
from operator import itemgetter

def TwitterApi():
    #API keys to access Twitter API
    client_key = 'J7pw6H0pyXfN0x74Ux67rwWiw'
    client_secret = 'lKElI59qp5NH2nJ8XGaAyihD4RI7lEBY65KvprYxlOP6zxy6Km'
    
    #The twitter API requires a single key that is an encoded string seperated a colon
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')
    
    #Need to utilise the same base url for a few requests so made it a variable
    base_url = 'https://api.twitter.com/'
    
    #This is the auth endpoint used for obtaining a Bearer Token
    auth_url = '{}oauth2/token'.format(base_url)
    
    #Need to submit the request in .json format
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    
    auth_data = {
        'grant_type': 'client_credentials'
    }
    
    #Makes the request with all the relevant information, and checks the response
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    
    #used for degbugging
    auth_resp.status_code
    
    #Just want to access the Keys provided by twitter, particularly the access token
    auth_resp.json().keys()
    
    access_token = auth_resp.json()['access_token']
    
    #Information of the user that we are searching for in json format, making sure to include our access token
    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)    
    }
    
    search_params = {
        'screen_name': 'HighwaysEAST',
        'exclude_replies' : 'true'
    }
    
    #This is where we need to make the search request too utlising the base url
    search_url = '{}1.1/statuses/user_timeline.json'.format(base_url)
    
    #Make our request and check the status code
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    
    search_resp.status_code
    
    #Save our response as a variable so we can iterate over it, and make the response readable, this was mostly for debugging
    tweet_data = search_resp.json()
    
    mentions = 0
    closed = 0
    wind = 0
    opened = 0
    global Twitter_OB
    
    #Iterate over the statuses we have collected to see if they mention the Orwell Bridge, and then other key words
    for status in tweet_data:
        if 'Orwell Bridge' in status['text']:
            mentions += 1
            if 'closed' in status['text']:
                closed += 1
            elif 'wind' in status['text']:
                wind += 1
            elif 'open' in status['text']:
                opened += 1
   #Finally we check the finally counts, and provide a simple print statement 
    else:
        if opened > 1:
            Twitter_OB = 'The Orwell Bridge has reopened'
        elif closed > 1:
            Twitter_OB = 'The Orwell Bridge is closed'
        elif wind > 1:
            Twitter_OB = 'High winds are expected over the Orwell Bridge, bridge may close, but is not closed yet'
        elif mentions == 0:
            Twitter_OB = 'HighwaysEAST has not tweeted about the Orwell Bridge recently, so the bridge should be open'
        
def WeatherAPI():
    #Makes the call to the API
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=52.02707&lon=1.16689&units=imperial&appid=72954df937d3a26ed5d0f1eaa4eb6e43")
   
    #Saves the results in JSON Format
    response_data = response.json()
    
    #Saves only the needed information
    wind = response_data['wind']
    
    #Create global variables so I can provide the value outside of the function
    global speed
    global Weather_OB
    
    #Converts the two needed values from the json to python variables
    speed, deg = itemgetter('speed', 'deg')(wind)
    
    #Logic to ascertain whether the speed is too great for the bridge to remain open 
    if speed >= 60:
        Weather_OB = "The wind speed around the Orwell Bridge is " + str(speed) + " miles per hour, so the bridge is, or will be, closed"
    elif speed >= 50 and speed < 60:
        if deg >= 330 or (deg >= 0 and deg <= 30):
            Weather_OB = "The wind speed directly across the Orwell Bridge is " + str(speed) + " miles per hour, and the so the bridge is, or will be, closed shortly"
        elif deg >= 150 and deg <= 210:
           Weather_OB = "The wind speed directly across the Orwell Bridge is " + str(speed) + " miles per hour, and the so the bridge is, or will be, closed shortly" 
        else:
            Weather_OB = "The wind speed near the Orwell Bridge is " + str(speed) + " miles per hour, so the bridge should be open"
    else:
        Weather_OB = "The wind speed near the Orwell Bridge is " + str(speed) + " miles per hour, so the bridge should be open"

#Calls the two functions
TwitterApi()
WeatherAPI()

#Print statements to confirm that the script has worked, would remove these if it wasn't for the project
print(Twitter_OB)
print(Weather_OB)

#Final statement to confirm whether the bridge is closed or open.
if 'closed' in Twitter_OB and 'closed' in Weather_OB:
    print('The bridge is defintely closed')
elif 'closed' in Twitter_OB and 'closed' not in Weather_OB:
    print("@HighwaysEast have stated that the Orwell Bridge is closed")
elif 'closed' in Weather_OB and 'closed' not in Twitter_OB:
    print("The wind speed is expected to be " + str(speed) + " miles per hour, but @HighwaysEast haven't closed the bridge yet, expect it to close imminently")
elif 'closed' not in Twitter_OB and 'closed' not in Weather_OB:
    print("The Orwell Bridge is open, and you should be able to cross it")
else:
    print('An error has occured, I do apologise, please contact me so that I can look into it')
    
    

        


