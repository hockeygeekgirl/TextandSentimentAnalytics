# Analyzing emotion and sentiment
The code in this repository uses a variety of approaches to analyze emotion and sentiment.

The examples were created using [Python and Visual Studio code](https://code.visualstudio.com/docs/python/python-tutorial)

## Analyzing text sentiment

Language used: Python

Services used: Azure Cognitive Service Text Analytics - Sentiment API

Related tutorials and resources:
* [How to sign up for the Text Analytics API](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-signup)
* [Text analytics Python quickstart](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python)

Files:
* **AnalyzeTextSentiment.py** code to analyze text and return a score from 0.0 to 1.0 indicating whether the sentiment is negative (0.0) or positive (1.0)

## Analyzing emotion and faces
Language used: Python

Services used: Azure Face API

Related tutorials and resources: 
* [What is the Azure Face API](https://docs.microsoft.com/en-us/azure/cognitive-services/face/overview)
* [Face API Notebook](https://hub.mybinder.org/user/microsoft-cogni-vices-notebooks-v5jcn96f/notebooks/FaceAPI.ipynb)
* [Analyze a local image using REST API and Python](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts/python-disk)
* [Analyze a remote image using REST API and Python](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts/python-analyze)


Files
* **CheckEmotionHTTPCall.py** code to locate faces in an image and return facial characteristics and a score from 0.0 to 1.0 for an assortment of emotions

## Generating a word cloud with Power BI and Text Analytics
Language used: F#

Services used: Azure Cognitive Services Text Analytics - Key Phrases API

Related tutorials and resources: 
* [Tutorial Power BI Word Cloud with Text Analytics](https://docs.microsoft.com/en-us/azure/cognitive-services/Text-Analytics/Tutorials/tutorial-power-bi-key-phrases)
* [How to extract key phrases using Text Analytics](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-keyword-extraction)
* [Power BI for report designers](https://docs.microsoft.com/en-us/power-bi/power-bi-creator-landing)
* [BI Desktop Quickstart learn DAX basics](https://docs.microsoft.com/en-us/power-bi/desktop-quickstart-learn-dax-basics)

Files
* **CirqueDeSoleilReviews.csv** csv file containing reviews of the Cirque de Soleil show Love you can use to extract keyphrases and generate a word cloud