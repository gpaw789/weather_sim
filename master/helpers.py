from math import exp

# additional helper functions

#global variables
places = {"Sydney": [-33.86, 151.2, 39],
          "Melbourne": [-37.73, 144.91, 78],
          "Adelaide": [-34.93, 138.58, 29],
          "Perth": [-31.92, 115.87, 25],
          "Darwin": [-12.42, 130.89, 30],
          "Brisbane": [-27.48, 153.04, 8],
          "Hobart": [-42.89, 147.33, 51],
          "Alice Springs": [-23.8, 133.89, 546],
          "Cairns": [-16.87, 145.75, 2],
          "Newman": [-23.45, 119.8, 524]}


def pressure(elevation):
    # https://en.wikipedia.org/wiki/Atmospheric_pressure
    pressure = 1013.25*exp(-(0.0001186*elevation))

    return pressure

def geolocation(location):
    # lat, long, ele
    places = {"Sydney": [-33.86, 151.2, 39],
              "Melbourne": [-37.73, 144.91, 78],
              "Adelaide": [-34.93, 138.58, 29],
              "Perth": [-31.92, 115.87, 25],
              "Darwin": [-12.42, 130.89, 30],
              "Brisbane": [-27.48, 153.04, 8],
              "Hobart": [-42.89, 147.33, 51],
              "Alice Springs": [-23.8, 133.89, 546],
              "Cairns": [-16.87, 145.75, 2],
              "Newman": [-23.45, 119.8, 524]}
    return places[location]