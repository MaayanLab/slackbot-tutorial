from covid.api import CovId19Data
import requests
import csv
import json

api = CovId19Data(force=False)

res = api.get_stats()

# GLOBAL STATS
def get_stats():
    confirmed = str("{:,}".format(res['confirmed']))
    recovered = str("{:,}".format(res['recovered']))
    deaths = str("{:,}".format(res['deaths']))

    return ("*Latest COVID-19 Stats: Global* \n" 
            ":black_small_square: *Confirmed Cases:* " + confirmed + "\n" +
            ":black_small_square: *Recovered Cases:* " + recovered + "\n" +
            ":black_small_square: *Deaths:* " + deaths
            )

# STATS BY COUNTRY
def stats_country(country):
    res = api.filter_by_country(country)
    confirmed = str("{:,}".format(res['confirmed']))
    recovered = str("{:,}".format(res['recovered']))
    deaths = str("{:,}".format(res['deaths']))

    country = res['label']

    return ("*Latest COVID-19 Stats: " + country + "*\n" +
            ":black_small_square: *Confirmed Cases:* " + confirmed + "\n" +
            ":black_small_square: *Recovered Cases:* " + recovered + "\n" +
            ":black_small_square: *Deaths:* " + deaths
            )

##############################################################################
# STATS BY STATE
from states_info import *

def stats_us():
    response = requests.get('https://covidtracking.com//api/v1/us/current.json')
    data = json.loads(response.text)

    positive = str("{:,}".format(data['positiveIncrease']))
    death = str("{:,}".format(data['deathConfirmed']))
    hospital = str("{:,}".format(data['hospitalizedCumulative']))
    total = str("{:,}".format(data['positive']))

    return ("*Latest COVID-19 Stats: United States *\n" +
                ":black_small_square: *New Cases:* " + positive + "\n" +
                ":black_small_square: *Total Cases:* " + total + "\n" +
                ":black_small_square: *Total Hospitalized:* " + hospital + "\n" +
                ":black_small_square: *Total Deaths:* " + death
                )

def stats_state(text):

    input = text.lower()

    if input in us_state_abbrev.keys():
        state = (us_state_abbrev[input]).lower()

        response = requests.get('https://covidtracking.com/api/v1/states/' + state + '/current.json')
        data = json.loads(response.text)

        state_name = data['state']
        positive = str("{:,}".format(data['positiveIncrease']))
        death = str("{:,}".format(data['death']))
        hospital = str("{:,}".format(data['hospitalizedCumulative']))
        total = str("{:,}".format(data['positive']))

        link = input.replace(" ", "")

        return ("*Latest COVID-19 Stats: " + state_name + "*\n" +
                ":black_small_square: *New Cases:* " + positive + "\n" +
                ":black_small_square: *Total Cases:* " + total + "\n" +
                ":black_small_square: *Total Hospitalized:* " + hospital + "\n" +
                ":black_small_square: *Total Deaths:* " + death + "\n" +
                ":black_small_square: https://covidtracking.com/data/state/" + link
                )

    elif input in us_state_abbrev.values():
        state = input

        response = requests.get('https://covidtracking.com/api/v1/states/' + state + '/current.json')
        data = json.loads(response.text)

        state_name = data['state']
        positive = str("{:,}".format(data['positiveIncrease']))
        death = str("{:,}".format(data['death']))
        hospital = str("{:,}".format(data['hospitalizedCumulative']))
        total = str("{:,}".format(data['positive']))

        return ("*Latest COVID-19 Stats: " + state_name + "*\n" +
                ":black_small_square: *New Cases:* " + positive + "\n" +
                ":black_small_square: *Total Cases:* " + total + "\n" +
                ":black_small_square: *Total Hospitalized:* " + hospital + "\n" +
                ":black_small_square: *Total Deaths:* " + death + "\n" +
                ":black_small_square: https://covidtracking.com/data/state/" + input
                )

    else:
        return ("*ERROR: Invalid State Name*")



