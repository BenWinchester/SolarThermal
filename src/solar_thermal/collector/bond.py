#!/usr/bin/python3.7
########################################################################################
# collector/bond.py - Represents the bond layer within a collector.                    #
#                                                                                      #
# Author: Ben Winchester                                                               #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 06/05/2022                                                             #
# License: Open source                                                                 #
########################################################################################

"""
The bond module for the collector component model.

This module represents a bond layer within a solar-thermal collector.

"""

from dataclasses import dataclass

from .__utils__ import MicroLayer

__all__ = ("Bond",)


@dataclass
class Bond(MicroLayer):
    """
    Represents a bond layer within the collector.

    .. attribute:: width
        The width of the bond, measured in meters.

    """

    width: float
