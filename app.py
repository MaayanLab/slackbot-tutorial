import os
from flask import Flask, request, make_response
from slack import WebClient
from slackeventsapi import SlackEventAdapter


# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter((os.environ['SLACK_SIGNING_SECRET']), "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(os.environ['SLACK_BOT_TOKEN'])

# SLACK EVENTS
@slack_events_adapter.on("message")
def message_sent(event_data):
    message = event_data["event"]
    channel = message["channel"]
    user = message["user"]

    if "<@U016FRPR9QT>" in message.get("text"):
        slack_web_client.chat_postMessage(
                    channel= channel,
                    text= "Hi there <@" + user + ">!")
        return make_response("", 200)

################################################################################
from covid_info import *
from covid.api import CovId19Data

api = CovId19Data(force=False)

# SLASH COMMANDS
@app.route('/covid', methods=['POST'])
def covid_link():
    info = request.form
    message = "https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html"

    channel = info['channel_id']

    slack_web_client.chat_postMessage(
        channel= channel,
        text= message)
    return make_response("", 200)

@app.route('/stats', methods=['POST'])
def covid_stats():
    info = request.form
    channel = info['channel_id']

    message = get_stats()

    slack_web_client.chat_postMessage(
        channel= channel,
        text= message)
    return make_response("", 200)

@app.route('/country', methods=['POST'])
def covid_country():
    info = request.form
    text = info['text']

    message = stats_country(text)

    channel = info['channel_id']

    slack_web_client.chat_postMessage(
        channel= channel,
        text= message)
    return make_response("", 200)

@app.route('/state', methods=['POST'])
def covid_state():
    info = request.form
    text = info['text']

    message = stats_state(text)

    channel = info['channel_id']

    slack_web_client.chat_postMessage(
        channel= channel,
        text= message)
    return make_response("", 200)


if __name__ == "__main__":
    app.run(port=8080)
