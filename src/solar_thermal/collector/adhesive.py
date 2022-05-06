#!/usr/bin/python3.7
########################################################################################
# pvt_collector/adhesive_.py - Represents adhesive layer within a collector.
#                                                                                      #
# Author: Ben Winchester                                                               #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 06/05/2022                                                             #
# License: Open source                                                                 #
########################################################################################

"""
The adhesive_ module for the collector component.

This module represents a adhesive layer within a solar-thermal collector panel.

In addition to the upper glass cover represnted, there is scope for a small adhesive
layer placed in direct contact with the upper surface of the solar-thermal absorber
module.

"""

from .__utils__ import MicroLayer

__all__ = ("Adhesive",)


class Adhesive(MicroLayer):
    """
    Represents an Adhesive layer within the panel.

    """
