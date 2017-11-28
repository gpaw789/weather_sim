import random
import datetime
from time import sleep
import pickle
import helpers
import pandas as pd

# structure
# main() is text interface
# build_position() is the function that builds the lat/long coodinates
# running() is the function that runs while loop indefinitely and print the datastream
# generate() is the function that generates the data

def generate(location, time, temperature, humidity):

    latlongele = helpers.geolocation(location)

    weather = ["Rain", "Snow", "Sunny"]
    # print data

    location_int = location
    lat = latlongele[0]
    long = latlongele[1]
    elevation = latlongele[2]
    position = "{},{},{}".format(lat,long,elevation)
    local_time = "{}Z".format(time.isoformat(timespec='seconds'))
    conditions_int = weather[random.randrange(3)]
    temperature = "%+d" % temperature
    pressure = helpers.pressure(elevation)
    humidity = humidity

    stream = "{}|{}|{}|{}|{}|{}|{}".format(location_int, position, local_time, conditions_int, temperature, pressure, humidity)

    return stream, float(temperature)

def build_position(positions_number):
    # purpose: for a given position number, ask user to type in each value
    # input: value in terms of string
    # output: e.g. ["-100,200", "-500, 200"]

    array_positions = [0]*int(positions_number)

    for i in range(0, len(array_positions)):
        long = input("Position {} Long: ".format(i))
        lat = input("Position {} Lat: ".format(i))
        foo = "{},{}".format(long,lat)
        array_positions[i] = foo

    return array_positions



def running(elements):
    # purpose: run the while loop forever, using variables
    # input: [variable1, variable2, variable3]
    # output: None

    # setting up values
    start_time_status = elements[0]
    data_per_second = elements[1]
    array_positions = elements[2]

    # examples of places
    places_list = ["Sydney", "Melbourne", "Adelaide", "Perth", "Darwin",
              "Brisbane", "Hobart", "Alice Springs", "Cairns", "Newman"]
    weather = ["Rain", "Snow", "Sunny"]

    # epoch time
    epoch = datetime.datetime(1970,1,1)
    i = datetime.datetime.now()
    seconds = int((i-epoch).total_seconds())

    # seed the initial values using neural network prediction
    array_input = []
    n = pickle.load(open("n_fit.p", "rb"))
    for i in helpers.places:
        # feed_input is lat, long, ele dictionary
        feed_input = {"lat": helpers.places[i][0], "long": helpers.places[i][1], "ele": helpers.places[i][2]}
        array_input.append(feed_input)

    temperature = [n.predict(pd.DataFrame(feed,index=[0])) for feed in array_input]
    # temperature = [random.randrange(-20,50) for x in range(10)]
    humidity = [random.randrange(0, 100) for x in range(10)]

    # set the time
    time = datetime.datetime.now()

    # run loop indefinitely
    while True:
        for location in range(0, len(places_list)):
            stream, temp_output = generate(places_list[location], time, temperature[location], humidity[location])
            print(stream)

            # storing data and making the next variable prediction
            # temperature is limited to -20 and +50 C, and its move either up or down based on a random number generator
            # humidity is limited to 0 and 100 % and its move either up or down based on a random number generator
            time = datetime.datetime.now() + datetime.timedelta(hours=1)
            # temperature[location] = min(max(temp_output + round(random.uniform(-1,1), 2), -20), 50)
            seconds = int((time - epoch).total_seconds())
            feed_input = {"lat": helpers.places[places_list[location]][0],
                          "long": helpers.places[places_list[location]][1],
                          "ele": helpers.places[places_list[location]][2]}
            temperature[location] = n.predict(pd.DataFrame(feed_input,index=[0]))
            humidity[location] = min(max(humidity[location] + random.randrange(-1, 1, 1), 0), 100)
        sleep(1/data_per_second)

    return 0


def main():
    # purpose: Run through text to ask user questions
    # input: None
    # output: None

    try:
        print("Welcome! Key in the number for options\n")
        print("Would you like to customise? (1) Customise  (2) Just show me what you got!")
        custom_status = int(input("Enter Value: "))
        if custom_status == 1:
            print("What is start time? (1) Now\n")
            start_time_status = int(input("Enter Value: "))
            print("How many data per second?\n")
            data_per_second = int(input("Enter Value: "))
            print("How many weather positions?\n")
            positions_number = int(input("Enter Value: "))
            array_positions = build_position(positions_number)
            elements = [start_time_status, data_per_second, array_positions]
            running(elements)

        elif custom_status == 2:
            start_time_status = 1; data_per_second = 2; array_positions = [0]
            elements = [start_time_status, data_per_second, array_positions]
            running(elements)

        else:
            print("Invalid Number, Try again\n")
            main()
            return 0
    except KeyboardInterrupt:       # press ctrl + c to cancel
        pass


    return 0


main()