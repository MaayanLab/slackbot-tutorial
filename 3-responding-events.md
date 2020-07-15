# Responding to Slack Events
Now that your app is runnning, we can now program it to respond to slack events. When running locally, you will need to tunnel requests from a public URL to your machine. We recommend [ngrok](https://ngrok.com/) to set up a tunnel. After downloading this program, you can get a url by running the following line of code in terminal:

```
$ ./ngrok http 8080
```
- **Note**: number will be whatever port you are running the app on

Now you will be brought to the ngrok page in your terminal window. Copy the https URL.

<img width="500" alt="Screen Shot 2020-07-15 at 3 38 05 PM" src="https://user-images.githubusercontent.com/66278476/87588171-3477d100-c6b1-11ea-9fd6-853018a82d41.png">

## Event Subscriptions: Setting Up
You are all set up now to respond to slack events! 

Go back to your app homepage and go to the **Events Subscription** section. 
- Click **Enable Events**
- Under **Request URL** enter your ngrok https link with '/slack/events' at the end.

Your URL will look something like this:
```
https://adsfjadsf.ngrok.io/slack/events
```

- Slack will then send a challenge parameter to your app. If all goes well, it will say **verified**!

<img width="719" alt="Screen Shot 2020-07-15 at 3 39 20 PM" src="https://user-images.githubusercontent.com/66278476/87588286-612be880-c6b1-11ea-92ac-d640b3bab7f9.png">

## Subscribe to Bot Events

Now we can subscribe to bot events. An event is essentially anything that happens in slack (message posted, file uploaded, member added, etc.). Subscribing to the events sets up the bot to “listen” for certain events. 

In our case, we want to subscribe to the following:
- **message.channels**: a message was posted to a channel
- **message.im**: a message was posted in a direct message channel

<img width="500" alt="Screen Shot 2020-07-15 at 3 40 03 PM" src="https://user-images.githubusercontent.com/66278476/87588344-7c96f380-c6b1-11ea-94f4-6b9765db6821.png">

Now we can begin programming our bot to respond to events!

## Code to Get Bot to Respond to Events

### Respond to Message Event
Add the following code to app.py. This will allow the bot to listen for events and post in the channel.

```Python
@slack_events_adapter.on("message")
def message_sent(event_data):
    message = event_data["event"]
    channel = message["channel"]

  
    slack_web_client.chat_postMessage(
        channel= channel,
        text= "Hi there!")
    return make_response("", 200)
```

Now the bot will respond when a message event occurs. The problem with this is that it will get stuck in a loop and keep posting this forever. We do not want this!

![Jul-13-2020 15-03-30](https://user-images.githubusercontent.com/66278476/87588603-f0390080-c6b1-11ea-8dd2-711deb2b2618.gif)

### Add Conditions for Bot

Like any other function, we can add conditions. The following piece of code basically says that when you mention your app in a message, it will respond with 'Hi there @<your name>!'

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

This a very simple condition, but it gives you an idea of how the functions are laid out. For more information about the different events APIs, click [here](https://api.slack.com/methods). As you can see, now the bot only responds when it is mentioned!

![Jul-13-2020 15-17-38](https://user-images.githubusercontent.com/66278476/87589004-938a1580-c6b2-11ea-8097-7f67c7a58d93.gif)

If this is your first app you are creating, do not worry! You'll get more familiar with this over time. Some tips are to pay attention to the data being sent to your application from slack, how you want that data manipulated, and what you want your bot to present back in slack!

---

**Next section: [4. Integrating Slash Commands](4-slash-commands.md).**

**Previous section: [2. Setting Up](2-setting-up.md).**

**Back to the [Table of contents](README.md#table-of-contents).**
