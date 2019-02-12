# Create Text Analytics service in Azure
# QuickStart https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python
# Import the requests library to simplify making an HTTP call from Python code
import requests

# Enter the subscription key and URL for your Text Analytics service
subscription_key = "3eeb229c488941a384c697adc22295df"
text_analytics_base_url = "https://canadacentral.api.cognitive.microsoft.com/text/analytics/v2.0/"

# Modify the URL to call the language detection API
language_api_url = text_analytics_base_url + "languages"

# Create JSON containing the text to analyze
documents = {'documents' : [
  {'id': '1', 'text': 'I love the Sens!  They have such pretty uniforms. Red is my favorite colour.'},
  {'id': '2', 'text': 'Le match de hockey a été incroyable j''aime les sénateurs d''Ottawa'},  
  {'id': '3', 'text': 'Ich habe ein schneeball auf mein kopf'}
]}

# Call the Text Analytics API
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()

# Print the RAW JSON returned by the API call
print(languages)

print("\n Original text analyzed \n")
#Print out the text you are analyzing for display purposes
for doc in documents["documents"]:
  print(str(doc["id"]) + ": " + str(doc["text"]))

print("\n Languages detected \n")
#Loop through the output and display the detected language
for document in languages["documents"]:
  for detectedLanguage in document["detectedLanguages"]: 
    print (str(document["id"]) + ": " + detectedLanguage["name"])
input()

#Sample JSON OUtput
# {'documents':  [
# {'id': '1', 
# 'detectedLanguages': 
#  [{'name': 'English', 'iso6391Name': 'en', 'score': 1.0}]}, 
# {'id': '3', 
# 'detectedLanguages': 
# [{'name': 'French', 'iso6391Name': 'fr', 'score': 1.0}]}, 
# {'id': '4', 
# 'detectedLanguages': [{'name': 'German', 'iso6391Name': 'de', 'score': 1.0}]}], 'errors': []}