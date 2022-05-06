#!/usr/bin/python3.7
########################################################################################
# collector/glass.py - Represents the glass layer within a collector.                  #
#                                                                                      #
# Author: Ben Winchester                                                               #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 06/05/2022                                                             #
# License: Open source                                                                 #
########################################################################################

"""
The glass module for the collector component.

This module represents a glass layer within a collector.

"""

from .__utils__ import OpticalLayer

__all__ = ("Glass",)


class Glass(OpticalLayer):
    """
    Represents the glass (upper) layer of the collector.

    """
