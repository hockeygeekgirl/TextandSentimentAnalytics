# Analyzing text, emotion and sentiment
The code in this repository uses a variety of approaches to analyze text, emotion and sentiment.

The examples were created using [Python and Visual Studio code](https://code.visualstudio.com/docs/python/python-tutorial)

## Analyzing text sentiment

Language used: Python

Services used: Azure Cognitive Service Text Analytics

Related tutorials and resources:
* [Text analytics Python quickstart](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python)

Files:
* AnalyzeTextSentiment.py code to analyze text and return a score from 0.0 to 1.0 indicating whether the sentiment is negative (0.0) or positive (1.0)

## Analyzing emotion and faces
Language used: Python

Services used: Azure Computer Vision API

Related tutorials and resources: 
* [Face API Notebook](https://hub.mybinder.org/user/microsoft-cogni-vices-notebooks-v5jcn96f/notebooks/FaceAPI.ipynb)
* [Analyze a local image using REST API and Python](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts/python-disk)
* [Analyze a remote image using REST API and Python](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts/python-analyze)


Files
* CheckEmotionHTTPCall.py code to locate faces in an image and return facial characteristics and a score from 0.0 to 1.0 for an assortment of emotions

## Detecting Language
Language used: Python

Services used: Azure Cognitive Service Text Analytics

Related tutorials and resources: 
* [Text analytics Python QuickStart](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python)

Files
* DetectLanguage.py code to detect the language in a string of text. e.g. is the text in English, French, or German