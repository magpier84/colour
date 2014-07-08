# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Showcases some **Colour** package *derivation* related examples.
"""

from numpy import matrix
import colour

# Retrieving *normalised primary matrix* from *ACES RGB* colourspace to *CIE XYZ* colourspace.
print(colour.get_normalised_primary_matrix(matrix([[0.73470, 0.26530],
                                                  [0.00000, 1.00000],
                                                  [0.00010, -0.07700]]),
                                          (0.32168, 0.33767)))

# Retrieving *normalised primary matrix* from *ACES RGB* colourspace to *CIE XYZ* colourspace.
print(colour.get_normalised_primary_matrix(colour.ACES_RGB_COLOURSPACE.primaries, colour.ACES_RGB_COLOURSPACE.whitepoint))

# Retrieving *normalised primary matrix* from *CIE XYZ* colourspace to *ACES RGB* colourspace.
print(colour.get_normalised_primary_matrix(colour.ACES_RGB_COLOURSPACE.primaries,
                                          colour.ACES_RGB_COLOURSPACE.whitepoint).getI())