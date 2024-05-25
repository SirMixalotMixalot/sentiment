import requests
import json
def sentiment_analyzer(text_to_analyse: str):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response =  requests.post(url, json=payload, headers=headers)
    print(response)
    print(response.text)
    print(response.status_code)
    if 200 <= response.status_code < 300:
        raise Exception("Something went wrong when analyzing that text... :(")
    sentiments =  json.loads(response.text)
    return {
        'label': sentiments['documentSentiment']['label'],
        'score': float(sentiments['documentSentiment']['score'])
    }
