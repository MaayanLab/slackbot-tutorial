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

Next, 



## 3. Responding to Slack Events

## 4. Integrating Slash Commands

## 5. Example App: COVID-Bot
For this tutorial, I have included code for a simple slack bot that responds to requests for up to date COVID-19 statistics through slash commands. Users can request information for specific countries or states as well. 

## 6. Running the App

## Link to video presentation... 
