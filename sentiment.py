import datetime
import os, argparse

from google.cloud import language_v1

client = language_v1.LanguageServiceClient()

def analyze_string(s):

    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = 'en'

    document = {'content': s, 'type_': type_, 'language':language}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request={'document':document, 'encoding_type':encoding_type})

    # Get overall sentiment of the input document
    return (response.document_sentiment.score+1)/2


if __name__ == "__main__":
    strings = ["This sucks"
    , "Nahh", "this is great wow amazing", "Who wants some chicken nuggets"
            
    ]

    for string in strings:
        print(string, analyze_string(string))