# Create Text Analytics service in Azure
import requests

# Set Subscription key and URL based on properties of your Text Analytics service
subscription_key = "3eeb229c488941a384c697adc22295df"
text_analytics_base_url = "https://canadacentral.api.cognitive.microsoft.com/text/analytics/v2.0/"

# Point to keyphrases API of Text Analytics service
key_phrase_api_url = text_analytics_base_url + "keyPhrases"

# Provide text to extract key phrases from
# These are lyrics by Megdeth, the lead singer is a character, so thoguht it would be fun to examine his lyrics
# 
documents = {'documents' : [
  {'id': '1', 'language' : 'en', 'text': 'Just like the Pied Piper Led rats through the streets We dance like marionettes Swaying to the symphony of destruction'},
  {'id': '2', 'language' : 'en', 'text': 'Acting like a robot Its metal brain corrodes You try to take its pulse Before the head explodes, explodes'},  
  {'id': '3', 'language' : 'en', 'text': 'The earth starts to rumble World powers fall A warring for the heavens A peaceful man stands tall, tall'}
]}

#Make HTTP Call to Text Analytics service
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()

# Display raw JSON returned
print(key_phrases)

# Display the keywords extracted
for document in key_phrases["documents"]:
    for keyphrase in document["keyPhrases"]:  
        print (keyphrase)
input()