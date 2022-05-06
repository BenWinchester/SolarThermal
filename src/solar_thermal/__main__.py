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


def main(args: List[str]) -> None:
    """
    Main function for the SolarThermal package.

    Inputs:
        - args:
            Arguments to parse from the command-line interface.

    """


if __name__ == "__main__":
    main(sys.argv[1:])
