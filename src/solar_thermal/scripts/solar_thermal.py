#!/usr/bin/python3
########################################################################################
# solar_thermal.py - Primary entry point for the solar-thermal package.                #
#                                                                                      #
# Author: Ben Winchester                                                               #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 06/05/2022                                                             #
# License: Open source                                                                 #
########################################################################################
"""
heatpanel.py - Primary entry point for the solar-thermal package.

"""

import sys

from ..__main__ import main as solar_thermal


def main():
    """
    Main function of the SolarThermal entry-point script.

    """

    solar_thermal(sys.argv[1:])
