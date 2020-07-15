# Integrating Slash Commands
Next feature we will be exploring are slash commands. These are fairly simple to program. 

## Create Slash Command for App
First step, go to your app home page. Under **Slash Commands**, click create new command. 

Here you will have to name the command and enter a Request URL. This will be the ngrok url from before, but this time, append your slash command at the end!

- Let's say your slash command is called '/command', your URL will look like:
```
https://adsfjadsf.ngrok.io/command
```
<img width="454" alt="Screen Shot 2020-07-15 at 3 49 44 PM" src="https://user-images.githubusercontent.com/66278476/87589161-d350fd00-c6b2-11ea-93f4-38c8b5475171.png">

## Program Slash Command
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
