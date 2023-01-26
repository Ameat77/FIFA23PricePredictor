import requests
from bs4 import BeautifulSoup
import sys
import time


r = requests.get('https://www.ea.com/fifa/ultimate-team/web-app/')

#Login Link?: https://signin.ea.com/p/juno/login?execution=e1583245206s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fhide_create%3Dtrue%26display%3Dweb2%252Flogin%26scope%3Dbasic.identity%2Boffline%2Bsignin%2Bbasic.entitlement%2Bbasic.persona%26release_type%3Dprod%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.ea.com%252Ffifa%252Fultimate-team%252Fweb-app%252Fauth.html%26accessToken%3D%26locale%3Den_US%26prompt%3Dlogin%26client_id%3DFIFA23_JS_WEB_APP
#USERNAME: lakshman.krishnaiyer@gmail.com
#PASSWORD: A1530590k!
# check status code for response received
# success code - 200
print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())