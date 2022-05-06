#!/usr/bin/python3.7
########################################################################################
# collector/eva.py - Represents the eva layer within a collector.                      #
#                                                                                      #
# Author: Ben Winchester                                                               #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 06/05/2022                                                             #
# License: Open source                                                                 #
########################################################################################

"""
The eva module for the collector component.

This module represents a eva layer within a PV-T panel.

"""

from .__utils__ import MicroLayer

__all__ = ("EVA",)


class EVA(MicroLayer):
    """
    Represents an EVA layer within the collector.

    """
