#!/usr/bin/python3.7
########################################################################################
# collector/tedlar.py - Represents the tedlar layer within a collector.                #
#                                                                                      #
# Author: Ben Winchester                                                               #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 06/05/2022                                                             #
# License: Open source                                                                 #
########################################################################################

"""
The tedlar module for the collector component.

This module represents a tedlar layer within a collector.

"""

from .__utils__ import MicroLayer

__all__ = ("Tedlar",)


class Tedlar(MicroLayer):
    """
    Represents a tedlar layer within the panel.

    """
