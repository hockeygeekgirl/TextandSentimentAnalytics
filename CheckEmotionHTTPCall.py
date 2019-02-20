# Useful related tutorials
# Detect Emotion Jupyter Notebook https://hub.mybinder.org/user/microsoft-cogni-vices-notebooks-v5jcn96f/notebooks/FaceAPI.ipynb
# Getting started with Python and VS Code https://code.visualstudio.com/docs/python/python-tutorial

# Before you can run this code you need to go to the Azure portal and create the Face API service
# Set subscription key to your own Azure subscription
# Change face_api_url to point to the correct data center

subscription_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
face_api_url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/detect'

# Import the requests library to simplify making an HTTP Call from Python
import requests

# Option 1 read image from URL
# The headers and the post request are different if you read from a URL vs reading from a local file
# image_url = 'https://nbcprohockeytalk.files.wordpress.com/2016/01/102039899-e1454119786238.jpg?w=1200'
# headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
# params = {
#     'returnFaceId': 'true',
#     'returnFaceLandmarks': 'false',
#     #If you want to see all the attributes that can be returned
#     'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
#     #If you just want whether they are smiling and emotion
#     # 'returnFaceAttributes': 'smile,emotion',
# }
# response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
#End of code to uncomment for Option 1

# Option 2 read image from local file
# Example 1: One person in photo looking happy
# image_path = "./TestImages/GoldInMoguls.jpg"
# Example 2: Two people in photo looking disappointed
image_path = "./TestImages/SilverSucks.jpg"

# Create image data object to pass to Computer Vision API
image_data = open(image_path, "rb").read()

# Set headers and parameters for HTTP Call to Computer Vision API
# When reading from file you need to specify content type of octet-stream
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
# If you want to see all the attributes that can be returned
    # 'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
# If you just want whether they are smiling and emotion
    'returnFaceAttributes': 'smile,emotion',
}

# #Call Computer Vision API
response = requests.post(face_api_url, headers=headers, params=params, data=image_data)
# End of code to uncomment for Option 2 Example of pointing to a local file

#read JSON returned by Computer Vision API
print("JSON returned")
faces = response.json()
print(faces)


#Iterate through the results to examine the attributes you want to see
print("\nEmotions:")
for face in faces:
    #If you just want to look at one emotion you can access it directly
    # fr = face["faceAttributes"]["emotion"]["happiness"]
    # print("Happiness is " + str(fr))
    #If you want to see the score for all emotions just loop through the results
    print("")
    for key in face["faceAttributes"]["emotion"]:
        value = face["faceAttributes"]["emotion"][key]
        print(str(key) + ": " + str(value))
input()

#Sample JSON Output if you return only smile & emotion attributes
# [{'faceId': '61e7513c-a970-49d9-8bf4-fe23e6eb5869', 
# 'faceRectangle': {'top': 127, 'left': 273, 'width': 120, 'height': 120},
# 'faceAttributes': {'smile': 0.0, 
# 'emotion': {'anger': 0.307, 'contempt': 0.0, 'disgust': 0.001, 'fear': 0.0, 'happiness': 0.0, 'neutral': 0.69, 'sadness': 0.001, 'surprise': 0.001}}},
# {'faceId': '98c13742-1f7e-4310-a388-44c79deb2e41',
# 'faceRectangle': {'top': 242, 'left': 833, 'width': 113, 'height': 113}, 
# 'faceAttributes': {'smile': 0.0, 
# 'emotion': {'anger': 0.001, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 0.0, 'neutral': 0.909, 'sadness': 0.089, 'surprise': 0.0}}}]

#Sample JSON output if you return full list of attributes
#[{'faceId': 'e84d4649-1de2-4125-b968-57050783babb', 
# 'faceRectangle': {'top': 127, 'left': 273, 'width': 120, 'height': 120}, 
# 'faceAttributes': {'smile': 0.0, 
# 'headPose': {'pitch': 0.0, 'roll': -15.0, 'yaw': 17.9}, 
# 'gender': 'male', 'age': 33.0, 
# 'facialHair': {'moustache': 0.4, 'beard': 0.4, 'sideburns': 0.4}, 
# 'glasses': 'NoGlasses', 
# 'emotion': {'anger': 0.307, 'contempt': 0.0, 'disgust': 0.001, 'fear': 0.0, 'happiness': 0.0, 'neutral': 0.69, 'sadness': 0.001, 'surprise': 0.001}, 
# 'blur': {'blurLevel': 'medium', 'value': 0.37}, 
# 'exposure': {'exposureLevel': 'goodExposure', 'value': 0.53}, 
# 'noise': {'noiseLevel': 'low', 'value': 0.26}, 
# 'makeup': {'eyeMakeup': False, 'lipMakeup': False}, 
# 'accessories': [], 
# 'occlusion': {'foreheadOccluded': False, 'eyeOccluded': False, 'mouthOccluded': False}, 
# 'hair': {'bald': 0.03, 'invisible': False, 
# 'hairColor': [{'color': 'brown', 'confidence': 0.99}, {'color': 'blond', 'confidence': 0.88}, {'color': 'red', 'confidence': 0.44}, {'color': 'black', 'confidence': 0.22}, {'color': 'gray', 'confidence': 0.09}, {'color': 'other', 'confidence': 0.06}]}}}, 
#
