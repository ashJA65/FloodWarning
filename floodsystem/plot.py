import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

from datetime import datetime, timedelta
from matplotlib.dates import date2num
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """
    Function that plots a graph of the water level over time for a station.
    """

    if len(levels) == 0:
        #plt.text(0,0.1,"NO DATA",fontsize=12,backgroundcolor="red")
        raise IndexError("Missing data")


    plt.plot(dates, levels)


    # check to see if the station has typical low and high levels
    if station.typical_range:
        low, high = station.typical_range
        # plot low and high levels
        plt.axhline(low, color='r', linestyle='--')
        plt.axhline(high, color='r', linestyle='--')

    #dont plot if missing data
    

    #formatting
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.tight_layout()

    
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level data and the best-fit polynomial for given station."""

    #get least-square fit of a polynomial of degree P for level history
    poly, d0 = polyfit(dates, levels, p)

    #plot history
    plt.plot(dates, levels)

    #plot typical range
    if station.typical_range:
        low, high = station.typical_range
        plt.axhline(low, color='r', linestyle='--')
        plt.axhline(high, color='r', linestyle='--')

    #plot best fit curve
    x = date2num(dates)
    plt.plot(x, poly(x - d0), color='m')

    #labels
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
