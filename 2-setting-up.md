# Setting Up
## Retrieve Tokens

After you've installed the app, you will be brought back to the app's landing page. There will now be a **Bot User OAuth Access Token**. This is a very important piece of information that we will need later. This slack bot token allows you to call the methods described by the scopes you requested during installation. KEEP THIS SAFE!! It is an identifying sensitive piece of information about your bot!

<img width="719" alt="Screen Shot 2020-07-15 at 3 36 42 PM" src="https://user-images.githubusercontent.com/66278476/87588048-04303280-c6b1-11ea-8b57-ac908de0f0a3.png">

The other piece of information that we will need is the **Slack Signing Secret**, which is used to enforce that all events are coming from Slack to keep your app secure. This can be found under the Basic Information section. 

## Creating Project Folder and Files
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
### Adding Tokens to Virtual Environment
- Remember those tokens we copied before? Well now we need to add them to our virtua environment. You can do this in terminal by typing: 
```
$ export SLACK_BOT_TOKEN= ...
$ export SLACK_SIGNING_SECRET= ... 
```

### Create File: app.py
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

**Yay! Now your app is running!!** :tada: :tada:

---

**Next section: [03 - Responding to Slack events](3-responding-events.md).**

**Previous section: [01 - Creating the Slack app](1-create-slack-app.md).**

**Back to the [Table of contents](README.md#table-of-contents).**
