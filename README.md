# How to Build a Slack App!
This is a simple tutorial about how to program a slack app using **Python** and **Flask**. 

This serves as a walkthrough guide and example of the types of Slack apps you can build with Slack's Python SDK, python-slackclient, and Slack Events Adapter, which facilitates the handling of data from the Slack Events API in Python. We'll cover all the basic steps you'll need to have a fully functioning app that can listen and respond to events in slack, handle slash commands, and so much more!

## 1. Creating the Slack App
### **Create the App**

 First thing you will need to do is create an app. 
 - Follow the instructions [here](https://api.slack.com/)

### **Adding Scopes** 

So after creating the app, you will be brought to the app’s home page where you will find all the information about the app including settings and features. 
In order to start configuring the app, we have to decide what we want our app to be able to do, and we're going to do this by going to the **OAuth and Permissions section.**

If you scroll down on that part, you’ll find the scope’s sections. Scopes are essentially what give your app permission to perform functionality in your slack workspace. A Slack app's capabilities and permissions are governed by the scopes it requests.

We want to add **Bot Token Scopes**. In our case, we will want to add:
- **channels:history**: allows the bot to view messages/content in channels
- **chat:write**: allows bot to send messages
- **commands**: allows the addition of shortcuts and/or slash commands that people can use
- **im:history**: allows the bot to view messages/content in dms

Now that you have added scopes, you can **install your app** to your workspace!

## 2. Setting Up
### Retrieve Tokens

After you've installed the app, you will be brought back to the app's landing page. There will now be a **Bot User OAuth Access Token**. This is a very important piece of information that we will need later. This slack bot token allows you to call the methods described by the scopes you requested during installation. KEEP THIS SAFE!! It is an identifying sensitive piece of information about your bot!

The other piece of information that we will need is the **Slack Signing Secret**, which is used to enforce that all events are coming from Slack to keep your app secure. This can be found under the Basic Information section. 

### Creating Project Folder and Files
In terminal, you can create a new project folder and set up your virtual environment. 
```
$ mkdir Project_Name
$ cd Project_Name
$ python -m venv env/
$ source env/bin/activate
```

Next, open up your project in your code editor of choice! 

Now, create a file 'requirements.txt'. Add the following lines of code:
```
slackclient>=2.0.0
slackeventsapi>=2.1.0
Flask>=1.1.2
covid-data-api
```

You can now install these dependencies by running the following line in terminal:
```
$ pip3 install -r requirements.txt
```

## Start Programming the Bot
**Adding Tokens to Virtual Environment**
- Remember those tokens we copied before? Well now we need to add them to our virtua environment. You can do this in terminal by typing: 
```
$ export SLACK_BOT_TOKEN= ...
$ export SLACK_SIGNING_SECRET= ... 
```

**Create File: app.py**
- Create an `app.py` file to run the app.

The first thing we'll need to do is import the code our app needs to run.

- In `app.py` add the following code:

```Python
import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
```

- Next, let's create a Flask server, initialize the WebClient/SlackEventAdapter, and make the app runnable. Add the following lines to `app.py`:

```Python
# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# Make app runnable
if __name__ == "__main__":
   app.run(port=8080)
```

- Back in terminal, you can now run the app!
```
$ python app.py
```

**Yay! Now your app is running!!**

## 3. Responding to Slack Events
Now that your app is runnning, we can now program it to respond to slack events. When running locally, you will need to tunnel requests from a public URL to your machine. We recommend [ngrok](https://ngrok.com/) to set up a tunnel. After downloading this program, you can get a url by running the following line of code in terminal:

```
$ ./ngrok http 8080
```
- **Note**: number will be whatever port you are running the app on

Now you will be brought to the ngrok page in your terminal window. Copy the https URL.

### Event Subscriptions: Setting Up
You are all set up now to respond to slack events! 

Go back to your app homepage and go to the **Events Subscription** section. 
- Click **Enable Events**
- Under **Request URL** enter your ngrok https link with '/slack/events' at the end.

Your URL will look something like this:
```
https://adsfjadsf.ngrok.io/slack/events
```

- Slack will then send a challenge parameter to your app. If all goes well, it will say **verified**!

### Subscribe to Bot Events

Now we can subscribe to bot events. An event is essentially anything that happens in slack (message posted, file uploaded, member added, etc.). Subscribing to the events sets up the bot to “listen” for certain events. 

In our case, we want to subscribe to the following:
- **message.channels**: a message was posted to a channel
- **message.im**: a message was posted in a direct message channel

Now we can begin programming our bot to respond to events!

### Code to Get Bot to Respond to Events

Add the following code to app.py. This will allow the bot to listen for events and post in the channel.

```Python
@slack_events_adapter.on("message")
def message_sent(event_data):
    message = event_data["event"]
    channel = message["channel"]
    user = message["user"]

    if "<@insert your bot id>" in message.get("text"):
        slack_web_client.chat_postMessage(
                    channel= channel,
                    text= "Hi there <@" + user + ">!")
        return make_response("", 200)
```

This piece of code basically says that when you mention your app in a message, it will respond with 'Hi there @<your name>!'

This a very simple condition, but it gives you an idea of how the functions are laid out. For more information about the different events APIs, click [here](https://api.slack.com/methods). 

If this is your first app you are creating, do not worry! You'll get more familiar with this over time. Some tips are to pay attention to the data being sent to your application from slack, how you want that data manipulated, and what you want your bot to present back in slack!

## 4. Integrating Slash Commands
Next feature we will be exploring are slash commands. These are fairly simple to program. 

### Create Slash Command for App
First step, go to your app home page. Under **Slash Commands**, click create new command. 

Here you will have to name the command and enter a Request URL. This will be the ngrok url from before, but this time, append your slash command at the end!

- Let's say your slash command is called '/command', your URL will look like:
```
https://adsfjadsf.ngrok.io/command
```

### Program Slash Command
Back in your app.py file, add the following lines of code: 

```Python
@app.route('/command', methods=['POST'])
def my_first_slash_command():
    info = request.form
    channel = info['channel_id']

    slack_web_client.chat_postMessage(
        channel= channel,
        text= "Hi there!")
    return make_response("", 200)
```

When you type '/command' in the channel, your bot should respond with 'Hi there!'.

**Yay!** Now you know how to create slash commands for your apps!

Now we can try creating our very own application that integrates everything we have gone over!

## 5. Example App: COVID-Bot
For this tutorial, we will create a simple slack bot that responds to requests for up to date COVID-19 statistics through slash commands. Users can request information for specific countries or states as well. 

During the past couple months, many projects focusing on the collection and analysis of COVID-19 data have been started. For us, that means that there is a lot of data out there to analyze, and there are countless APIs that make this data easily accessible. 

For this bot, we will be using APIs from two projects. 

### The COVID Tracking Project
The COVID Tracking Project is an effort by [The Atlantic](https://www.theatlantic.com/) that aims to provide the pubic with the most complete data about COVID-19 in the US. In addition to their website, they also offer a publicly available [API](https://covidtracking.com/data/api) that can be used to retrieve up-to-date, state specific and US COVID-19 information. 

### JHU CSSE COVID-19 Dashboard Project
The [COVID-19 Dashboard](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) is a project by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University (JHU). What started as a project by a first-year grad student at the beginning of the year has become a familiar feature on news sites and on TV the world over, tracking the total number of confirmed COVID-19 cases, deaths, and recoveries globally. In addition to their website, they also offer a publicly available [API](https://covidtracking.com/data/api) that can be used to retrieve up-to-date, state specific and US COVID-19 information. 

### COVID-19 Slack Bot

For our bot, we can achieve our goals through the use of slash commands. Let's say someone uses a command '/state' or '/country' followed by their state or country of interest. The bot can then display stats based on the user input. We know how to do this! Let's follow some steps that we went through before.

#### Create an app (or modify the tutorial bot). 
#### Add slash commands. 
- Add the following code to your file

## Link to video presentation... 
