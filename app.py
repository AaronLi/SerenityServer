from flask import Flask, request
import sentiment, json
app = Flask(__name__)

@app.route('/')
def sentimentResponse():
    string = request.args.get('string')
    if string:
        analysis = sentiment.analyze_string(string)
        print("Rated",string,'with a score of',analysis)
        return json.dumps({'state':'ok', 'string':string, 'score':analysis})
    else:
        print("Invalid request")
        return json.dumps({'state':'invalid'})


if __name__ == "__main__":
    app.run(port=8080)