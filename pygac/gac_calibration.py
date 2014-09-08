#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Martin Raspaud

# Author(s):

#   Martin Raspaud <martin.raspaud@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Calibration coefficients and generic calibration functions
"""
import numpy as np

coeffs = {
    'metop02': {'ah': [0.1665, 0.1905, 0.217],
                'al': [0.0555, 0.0635, 0.031],
                'bh': [1.797, 2.149, 4.11],
                'bl': [1.797, 2.149, 4.11],
                'c_dark': [40.43, 39.75, 41.8],
                'c_s': [501.0, 500.0, 502.0],
                'ch': [-0.352, -0.225, 0.0],
                'cl': [-0.352, -0.225, 0.0],
                'l_date': 2006.77},
    'noaa07': {'ah': [0.111206, 0.107664, 0.0],
               'al': [0.111206, 0.107664, 0.0],
               'bh': [8.8581, 20.7843, 0.0],
               'bl': [8.8581, 20.7843, 0.0],
               'c_dark': [36.0, 37.0, 39.0],
               'ch': [-1.11938, -4.32167, 0.0],
               'cl': [-1.11938, -4.32167, 0.0],
               'l_date': 1981.4764,
               'd': np.array([[0, 0, 0, 0, 0],
                              [277.099, 5.048E-2, 2.823E-6, 0, 0],
                              [276.734, 5.069E-2, 2.493E-6, 0, 0],
                              [276.876, 5.148E-2, 1.040E-6, 0, 0],
                              [276.160, 5.128E-2, 1.414E-6, 0, 0]]),
               'n_s': [0.0, -5.16, -4.28],
               'c_wn': [2684.5233, 928.23757, 841.52137],
               'a': [1.94882690, 0.52807997, 0.40557027],
               'b': [1.0 / 1.0029260, 1.0 / 1.0014039, 1.0 / 1.0011789],
               'b1': [1.0, 0.89783, 0.93683],
               'b2': [0.0, 0.0004819, 0.0002425],
               'b0': [0.0, 5.25, 3.93],
               },
    'noaa09': {'ah': [0.109312, 0.11601, 0.0],
               'al': [0.109312, 0.11601, 0.0],
               'bh': [5.66526, 3.93889, 0.0],
               'bl': [5.66526, 3.93889, 0.0],
               'c_dark': [38.0, 40.0, 38.0],
               'ch': [0.27152, -0.258047, 0.0],
               'cl': [0.27152, -0.258047, 0.0],
               'l_date': 1984.948,
               'd': np.array([[0, 0, 0, 0, 0],
                              [277.018000, 0.051280, 0.0, 0, 0],
                              [276.750000, 0.051280, 0.0, 0, 0],
                              [276.862000, 0.051280, 0.0, 0, 0],
                              [276.546000, 0.051280, 0.0, 0, 0]]),

               'n_s': [0.0, -5.530, -3.06],
               'c_wn': [2690.0451, 930.50230, 845.75000],
               'a': [1.8832662, 0.5115335, 0.3882150],
               'b': [1.0 / 1.0028978, 1.0 / 1.0013570, 1.0 / 1.0011210],
               'b1': [1.0, 0.88643, 0.95311],
               'b2': [0.0, 0.0006033, 0.0002198],
               'b0': [0.0, 5.24, 2.42],
               },
    'noaa10': {'ah': [0.114803, 0.13268199999999999, 0.0],
               'al': [0.114803, 0.13268199999999999, 0.0],
               'bh': [3.4345599999999998, 0.00926103, 0.0],
               'bl': [3.4345599999999998, 0.00926103, 0.0],
               'c_dark': [39.439999999999998,
                          39.399999999999999,
                          37.509999999999998],
               'ch': [-0.384635, 0.13733300000000001, 0.0],
               'cl': [-0.384635, 0.13733300000000001, 0.0],
               'l_date': 1986.712,
               'd': np.array([[0, 0, 0, 0, 0],
                              [276.659, 0.051275, 1.363e-06, 0, 0],
                              [276.659, 0.051275, 1.363e-06, 0, 0],
                              [276.659, 0.051275, 1.363e-06, 0, 0],
                              [276.659, 0.051275, 1.363e-06, 0, 0]])
               },
    'noaa11': {'ah': [0.114786, 0.115219, 0.0],
               'al': [0.114786, 0.115219, 0.0],
               'bh': [-1.8297399999999999, -1.3949499999999999, 0.0],
               'bl': [-1.8297399999999999, -1.3949499999999999, 0.0],
               'c_dark': [40.0, 40.0, 40.0],
               'ch': [0.412551, 0.23697799999999999, 0.0],
               'cl': [0.412551, 0.23697799999999999, 0.0],
               'l_date': 1988.7064,
               'd': np.array([[0, 0, 0, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0]])
               },
    'noaa12': {'ah': [0.118059, 0.135684, 0.0],
               'al': [0.118059, 0.135684, 0.0],
               'bh': [4.8884800000000004, 4.6709800000000001, 0.0],
               'bl': [4.8884800000000004, 4.6709800000000001, 0.0],
               'c_dark': [41.0, 40.0, 40.0],
               'ch': [-0.34776899999999999, -0.399447, 0.0],
               'cl': [-0.34776899999999999, -0.399447, 0.0],
               'l_date': 1991.3669,
               'd': np.array([[0, 0, 0, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0]])

               },
    'noaa14': {'ah': np.array([0.121408, 0.144515, 0.0]),
               'al': np.array([0.121408, 0.144515, 0.0]),
               'bh': np.array([4.07313, 0.885331, 0.0]),
               'bl': np.array([4.07313, 0.885331, 0.0]),
               'c_dark': np.array([41.0, 41.0, 39.0]),
               'ch': np.array([-0.375215, 0.233727, 0.0]),
               'cl': np.array([-0.375215, 0.233727, 0.0]),
               'l_date': 1994.9699,
               'd': np.array([[0, 0, 0, 0, 0],  # reset prt
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0],
                              [276.597, 0.051275, 1.363e-06, 0, 0]]),
               'n_s': np.array([0.0069, -4.05, -2.29]),
               'c_wn': np.array([2654.25, 928.349, 833.040]),
               'a': np.array([1.885330, 0.308384, 0.022171]),
               'b': np.array([1.0 / 1.003839, 1.0 / 1.001443, 1.0 / 1.000538]),
               'b1': np.array([1.00359, 0.92378, 0.96194]),
               'b2': np.array([0.0, 0.000382, 0.0001742]),
               'b0': np.array([-0.0031, 3.72, 2.00])},
    'noaa15': {'ah': [0.18149999999999999,
                      0.20250000000000001,
                      0.18459999999999999],
               'al': [0.060499999999999998, 0.067500000000000004, 0.0275],
               'bh': [0.44700000000000001, 0.035000000000000003, 0.0],
               'bl': [0.44700000000000001, 0.035000000000000003, 0.0],
               'c_dark': [39.0, 40.0, 39.0],
               'c_s': [500.0, 500.0, 500.0],
               'ch': [-0.059999999999999998, 0.0070000000000000001, 0.0],
               'cl': [-0.059999999999999998, 0.0070000000000000001, 0.0],
               'l_date': 1998.3641,
               'd': np.array([[0, 0, 0, 0, 0],
                              [276.60157, 0.051045, 1.36328E-06, 0.0, 0.0],
                              [276.62531, 0.050909, 1.47266E-06, 0.0, 0.0],
                              [276.67413, 0.050907, 1.47656E-06, 0.0, 0.0],
                              [276.59258, 0.050966, 1.47656E-06, 0.0, 0.0]])
               },
    'noaa16': {'ah': [0.168, 0.174, 0.2013],
               'al': [0.056, 0.058, 0.0288],
               'bh': [0.306, 0.586, -0.810],
               'bl': [0.30599999999999999,
                      0.58599999999999997,
                      -0.81000000000000005],
               'c_dark': [39.299999999999997,
                          38.899999999999999,
                          38.399999999999999],
               'c_s': [498.95999999999998,
                       500.17000000000002,
                       499.43000000000001],
               'ch': [0.025000000000000001, 0.035999999999999997, 0.0],
               'cl': [0.025000000000000001, 0.035999999999999997, 0.0],
               'l_date': 2000.7228,
               'd': np.array([[0, 0, 0, 0, 0],
                              [276.355, 5.562E-02, -1.590E-05,
                                  2.486E-08, -1.199E-11],
                              [276.142, 5.605E-02, -1.707E-05,
                                  2.595E-08, -1.224E-11],
                              [275.996, 5.486E-02, -1.223E-05,
                                  1.862E-08, -0.853E-11],
                              [276.132, 5.494E-02, -1.344E-05,
                                  2.112E-08, -1.001E-11]])

               },
    'noaa17': {'ah': [0.17249999999999999,
                      0.19500000000000001,
                      0.21529999999999999],
               'al': [0.057500000000000002,
                      0.065000000000000002,
                      0.030800000000000001],
               'bh': [1.7070000000000001, 3.117, 4.0599999999999996],
               'bl': [1.7070000000000001, 3.117, 4.0599999999999996],
               'c_dark': [39.990000000000002,
                          39.090000000000003,
                          42.090000000000003],
               'c_s': [501.12, 500.73000000000002, 501.37],
               'ch': [-0.151, -0.26500000000000001, -0.37],
               'cl': [-0.151, -0.26500000000000001, -0.37],
               'l_date': 2002.47912,
               'd': np.array([[0, 0, 0, 0, 0],
                              [276.628, 0.05098, 1.371E-06, 0.0, 0.0],
                              [276.538, 0.05098, 1.371E-06, 0.0, 0.0],
                              [276.761, 0.05097, 1.369E-06, 0.0, 0.0],
                              [276.660, 0.05100, 1.348E-06, 0.0, 0.0]])

               },
    'noaa18': {'ah': [0.1665,
                      0.1785,
                      0.1849],
               'al': [0.0555,
                      0.0595,
                      0.0262],
               'bh': [3.068, 4.541, 0.0],
               'bl': [3.068, 4.541, 0.0],
               'c_dark': [39.44,
                          39.40,
                          37.51],
               'c_s': [500.54, 500.40, 500.56],
               'ch': [-0.443, -0.611, 0.0],
               'cl': [-0.443, -0.611, 0.0],
               'l_date': 2005.18891,
               'd': np.array([[0, 0, 0, 0, 0],
                              [276.601, 0.05090, 1.657E-06, 0.0, 0.0],
                              [276.683, 0.05101, 1.482E-06, 0.0, 0.0],
                              [276.565, 0.05117, 1.313E-06, 0.0, 0.0],
                              [276.615, 0.05103, 1.484E-06, 0.0, 0.0]])

               },
    'noaa19': {'ah': np.array([0.1680, 0.1755, 0.1880]),
               'al': np.array([0.0560, 0.0585, 0.0272]),
               'bh': np.array([-5.985, 2.263, 0.0]),
               'bl': np.array([-5.985, 2.263, 0.0]),
               'c_dark': np.array([38.8, 39.00, 39.4]),
               'c_s': np.array([496.43, 500.37, 496.11]),
               'ch': np.array([-8.687, 0.748, 0.0]),
               'cl': np.array([-8.687, 0.748, 0.0]),
               'l_date': 2009.096,
               'd': np.array([[0, 0, 0, 0, 0],  # reset prt
                              [276.6067, 0.051111, 1.405783e-06, 0, 0],
                              [276.6119, 0.051090, 1.496037e-06, 0, 0],
                              [276.6311, 0.051033, 1.496990e-06, 0, 0],
                              [276.6268, 0.051058, 1.493110e-06, 0, 0]]),
               'n_s': np.array([0.0, -5.49, -3.39]),
               'c_wn': np.array([2670.2425, 927.92374, 831.28619]),
               'a': np.array([1.6863857, 0.39419031, 0.26364620]),
               'b': np.array([1.0 / 1.0025955,
                              1.0 / 1.0013299,
                              1.0 / 1.0009546]),
               'b0': np.array([0.0, 5.70, 3.58]),
               'b1': np.array([1 - 0.0, 1 - 0.11187, 1 - 0.05991]),
               'b2': np.array([0.0, 0.00054668, 0.00024985])}}


class Calibrator(object):

    def __init__(self, spacecraft):
        self.__dict__.update(coeffs[spacecraft])


def calibrate_solar(counts, chan, year, jday, spacecraft, corr=1):
    """Do the solar calibration and return reflectance (between 0 and 100).
    """
    cal = Calibrator(spacecraft)

    t = (year + jday / 365.0) - cal.l_date
    stl = (cal.al[chan] * (100.0 + cal.bl[chan] * t +
                           cal.cl[chan] * t * t)) / 100.0
    sth = (cal.ah[chan] * (100.0 + cal.bh[chan] * t +
                           cal.ch[chan] * t * t)) / 100.0
    try:
        return np.where(counts <= cal.c_s[chan],
                        (counts - cal.c_dark[chan]) * stl,
                        (cal.c_s[chan] - cal.c_dark[chan]) * stl
                        + (counts - cal.c_s[chan]) * sth)
    except AttributeError:
        return (counts - cal.c_dark[chan]) * stl * corr


def calibrate_thermal(counts, prt, ict, space, line_numbers, channel, spacecraft):
    """Do the thermal calibration and return brightness temperatures (K).
    """
    cal = Calibrator(spacecraft)

    chan = channel - 3

    lines, columns = counts.shape[:2]

    offset = 0

    for i, prt_val in enumerate(prt):
        if prt_val < 50:
            offset = i
            break

    iprt = (line_numbers - line_numbers[0] + 5 - offset) % 5

    tprt = (cal.d[iprt, 0] + prt *
            (cal.d[iprt, 1] + prt *
             (cal.d[iprt, 2] + prt *
              (cal.d[iprt, 3] + prt *
               (cal.d[iprt, 4])))))

    zeros = iprt == 0
    nonzeros = np.logical_not(zeros)

    tprt[zeros] = np.interp((zeros).nonzero()[0],
                            (nonzeros).nonzero()[0],
                            tprt[nonzeros])

    # convolving and smoothing PRT, ICT and SPACE values
    if lines > 51:
        wlength = 51
    else:
        wlength = 3

    weighting_function = np.ones(wlength, dtype=float) / wlength
    tprt_convolved = np.convolve(tprt, weighting_function, 'same')
    ict_convolved = np.convolve(ict, weighting_function, 'same')
    space_convolved = np.convolve(space, weighting_function, 'same')
    # take care of the beginning and end
    tprt_convolved[0:(wlength - 1) / 2] = tprt_convolved[(wlength - 1) / 2]
    ict_convolved[0:(wlength - 1) / 2] = ict_convolved[(wlength - 1) / 2]
    space_convolved[0:(wlength - 1) / 2] = space_convolved[(wlength - 1) / 2]
    tprt_convolved[-(wlength - 1) / 2:] = tprt_convolved[-((wlength + 1) / 2)]
    ict_convolved[-(wlength - 1) / 2:] = ict_convolved[-((wlength + 1) / 2)]
    space_convolved[-(wlength - 1) / 2:] = \
        space_convolved[-((wlength + 1) / 2)]

    new_tprt = np.transpose(np.tile(tprt_convolved, (columns, 1)))
    new_ict = np.transpose(np.tile(ict_convolved, (columns, 1)))
    new_space = np.transpose(np.tile(space_convolved, (columns, 1)))

    # calibrating thermal channel

    tBB = new_tprt
    tsBB = cal.a[chan] + cal.b[chan] * tBB
    nBB_num = (1.1910427 * 0.000010) * cal.c_wn[chan] ** 3
    nBB = nBB_num / (np.exp((1.4387752 * cal.c_wn[chan]) / tsBB) - 1.0)

    Nlin = (cal.n_s[chan] +
            (((nBB - cal.n_s[chan])
              * (new_space - counts))
             / (new_space - new_ict)))
    Ncor = cal.b0[chan] + Nlin * (cal.b1[chan] + cal.b2[chan] * Nlin)
    Ne = Ncor
    tsE = ((1.4387752 * cal.c_wn[chan])
           / np.log(1.0 + nBB_num / Ne))
    bt = (tsE - cal.a[chan]) / cal.b[chan]

    return bt