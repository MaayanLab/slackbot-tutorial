# Creating the Slack App
## **Create the App**

 First thing you will need to do is create an app. 
 - Follow the instructions [here](https://api.slack.com/)
 
<img width="719" alt="Screen Shot 2020-07-15 at 3 31 52 PM" src="https://user-images.githubusercontent.com/66278476/87587629-56bd1f00-c6b0-11ea-880d-fb47234d9d50.png">

<img width="430" alt="Screen Shot 2020-07-15 at 3 30 51 PM" src="https://user-images.githubusercontent.com/66278476/87587526-34c39c80-c6b0-11ea-8d53-3d80f7961e2d.png">

## **Adding Scopes** 

So after creating the app, you will be brought to the app’s home page where you will find all the information about the app including settings and features. 
In order to start configuring the app, we have to decide what we want our app to be able to do, and we're going to do this by going to the **OAuth and Permissions section.**

<img width="719" alt="Screen Shot 2020-07-15 at 3 32 50 PM" src="https://user-images.githubusercontent.com/66278476/87587718-76ecde00-c6b0-11ea-848d-3e78840e0506.png">

If you scroll down on that part, you’ll find the scope’s sections. Scopes are essentially what give your app permission to perform functionality in your slack workspace. A Slack app's capabilities and permissions are governed by the scopes it requests.

<img width="256" alt="Screen Shot 2020-07-15 at 3 33 28 PM" src="https://user-images.githubusercontent.com/66278476/87587794-9257e900-c6b0-11ea-9592-6097530e7a37.png">

We want to add **Bot Token Scopes**. In our case, we will want to add:
- **channels:history**: allows the bot to view messages/content in channels
- **chat:write**: allows bot to send messages
- **commands**: allows the addition of shortcuts and/or slash commands that people can use
- **im:history**: allows the bot to view messages/content in dms

<img width="719" alt="Screen Shot 2020-07-15 at 3 34 18 PM" src="https://user-images.githubusercontent.com/66278476/87587864-af8cb780-c6b0-11ea-9574-c3f10686d95c.png">

Now that you have added scopes, you can **install your app** to your workspace! :tada: :sparkles: :tada:
