''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# Import the sentiment_analyzer function from the package created: TODO

#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    text_to_analyse = request.args['textToAnalyze']
    try:
        analysis = sentiment_analyzer(text_to_analyse)
    except Exception as e:
        print(e)
        return 'Could not analyze text', 500
    return f'The given text has been identified as {analysis["label"]} with a score of {analysis["score"]}'


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    
    app.run(port=5000)
