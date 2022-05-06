#!/usr/bin/python3
########################################################################################
# __main__.py - Main module for SolarThermal                                           #
#                                                                                      #
# Author: Ben Winchester                                                               #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 06/05/2022                                                             #
# License: Open source                                                                 #
########################################################################################
"""
The main module for the SolarThermal package.

The SolarThermal package is capable of simulating a wide variety of solar-thermal
panels.

"""

import sys

from typing import List

__all__ = ("main",)


# SolarThermal header string:
#   Text to display when instantiating the SolarThermal model.
SOLAR_THERMAL_HEADER_STRING = """
\033[38;5;214m
                                       ,
                                       ,
                          ,           ,,,           ,
                           ,,         ,,,         ,,
                            ,,,.     .,,,,      ,,,
                             ,,,,.            ,,,,.
                 ,,.              ,,,,,,,,,,,    ,         .,,.
                    ,,,,,,.   ,,,,,,,,,,,,,,,,,,,   .,,,,,,.
                       ,,,  ,,,,,,,,,,,,,,,,,,,,,,,  ,,,.
                           ,,,,,,,,,,,,,,,,,,,,,,,,,
                          ,,,,,,,,,,,,,,,,,,,,,,,,,,,
           .,,,,,,,,,,,,  ,,,,,,,,,.,.,,,,,,,,,,,,,,,  ,,,,,,,,,,,,,
\033[0m

         _____       _         _______ _                               _
        / ____|     | |       |__   __| |                             | |
       | (___   ___ | | __ _ _ __| |  | |__   ___ _ __ _ __ ___   __ _| |
        \\___ \\ / _ \\| |/ _` | '__| |  | '_ \\ / _ \\ '__| '_ ` _ \\ / _` | |
        ____) | (_) | | (_| | |  | |  | | | |  __/ |  | | | | | | (_| | |
       |_____/ \\___/|_|\\__,_|_|  |_|  |_| |_|\\___|_|  |_| |_| |_|\\__,_|_|


                           Solar Thermal Panel Model
                      Copyright Benedict Winchester, 2022

              For more information, contact Benedict Winchester at
                         benedict.winchester@gmail.com

"""


def main(args: List[str]) -> None:
    """
    Main function for the SolarThermal package.

    Inputs:
        - args:
            Arguments to parse from the command-line interface.

    """

    print(SOLAR_THERMAL_HEADER_STRING)


if __name__ == "__main__":
    main(sys.argv[1:])
