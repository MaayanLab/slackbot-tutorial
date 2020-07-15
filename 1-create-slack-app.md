# Creating the Slack App
## **Create the App**

 First thing you will need to do is create an app. 
 - Follow the instructions [here](https://api.slack.com/)

## **Adding Scopes** 

So after creating the app, you will be brought to the app’s home page where you will find all the information about the app including settings and features. 
In order to start configuring the app, we have to decide what we want our app to be able to do, and we're going to do this by going to the **OAuth and Permissions section.**

If you scroll down on that part, you’ll find the scope’s sections. Scopes are essentially what give your app permission to perform functionality in your slack workspace. A Slack app's capabilities and permissions are governed by the scopes it requests.

We want to add **Bot Token Scopes**. In our case, we will want to add:
- **channels:history**: allows the bot to view messages/content in channels
- **chat:write**: allows bot to send messages
- **commands**: allows the addition of shortcuts and/or slash commands that people can use
- **im:history**: allows the bot to view messages/content in dms

Now that you have added scopes, you can **install your app** to your workspace!
