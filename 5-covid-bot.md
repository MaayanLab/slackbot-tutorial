# Example App: COVID-Bot
For this tutorial, we will create a simple slack bot that responds to requests for up to date COVID-19 statistics through slash commands. Users can request information for specific countries or states as well. 

During the past couple months, many projects focusing on the collection and analysis of COVID-19 data have been started. For us, that means that there is a lot of data out there to analyze, and there are countless APIs that make this data easily accessible. 

For this bot, we will be using APIs from two projects. 

## The COVID Tracking Project
The COVID Tracking Project is an effort by [The Atlantic](https://www.theatlantic.com/) that aims to provide the pubic with the most complete data about COVID-19 in the US. In addition to their website, they also offer a publicly available [API](https://covidtracking.com/data/api) that can be used to retrieve up-to-date, state specific and US COVID-19 information. 

## JHU CSSE COVID-19 Dashboard Project
The [COVID-19 Dashboard](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) is a project by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University (JHU). What started as a project by a first-year grad student at the beginning of the year has become a familiar feature on news sites and on TV the world over, tracking the total number of confirmed COVID-19 cases, deaths, and recoveries globally. In addition to their website, they also offer a publicly available [API](https://covidtracking.com/data/api) that can be used to retrieve up-to-date, state specific and US COVID-19 information. 

## COVID-19 Slack Bot

For our bot, we can achieve our goals through the use of slash commands. Let's say someone uses a command '/state' or '/country' followed by their state or country of interest. The bot can then display stats based on the user input. We know how to do this! Let's follow some steps that we went through before.

#### Create an app (or modify the tutorial bot). 
#### Add slash commands. 
- Add the following code to your file (as found in the *covid_info.py* file).
#### Install app!!
**Now you have a fully functional and useful slack application!**
