import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num


def plot_water_levels(station, dates, levels):
    """
    Function that plots a graph of the water level over time for a station.
    """
    plt.plot(dates, levels)

    # check to see if the station has typical low and high levels
    if station.typical_range:
        low, high = station.typical_range
        # plot low and high levels
        plt.axhline(low, color='r', linestyle='--')
        plt.axhline(high, color='r', linestyle='--')

    #formatting
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
