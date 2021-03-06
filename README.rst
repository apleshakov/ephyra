Ephyra
========

.. contents::

Introduction
------------

Ephyra is a library to help with mouse input configuration; includes both Python and native C
(CPython, tested with Windows 10 and Visual Studio 2019 tools) implementations. It supports full rotation and same screen
ratio/distance approaches.

Installation
------------

Releases are available from PyPI at https://pypi.org/project/ephyra/

Usage
-----

This code shows how to get sensitivity coefficients and values for a new application or a different view within same
application as well as characteristic of a particular setup. See tests for more examples. ::

    from fractions import Fraction
    from math import radians

    from ephyra import DataHelper, FT_HORIZONTAL, FS_HORIZONTAL_PLUS, FS_VERTICAL_MINUS, RT_AZIMUTHAL, \
        FullRotationCalculator, ScreenRatioCalculator, DetailsCalculator
    from ephyra.formula import horizontal_4_to_3_fov_coefficient, horizontal_fov_to_80_coefficient

    dh1 = DataHelper(screen_aspect_ratio=Fraction(16, 10), fov=radians(90), fov_aspect_ratio=Fraction(4, 3),
                     fov_type=FT_HORIZONTAL, fov_scaling=FS_HORIZONTAL_PLUS, rt=RT_AZIMUTHAL,
                     ltr_coefficient_transformation_formula=horizontal_4_to_3_fov_coefficient,
                     radians_per_count=radians(0.022), counts_per_unit=800, screen_diagonal=24)

    dh2 = DataHelper(screen_aspect_ratio=Fraction(16, 10), fov=radians(100), fov_aspect_ratio=Fraction(16, 10),
                     fov_type=FT_HORIZONTAL, fov_scaling=FS_VERTICAL_MINUS, rt=RT_AZIMUTHAL,
                     ltr_coefficient_transformation_formula=horizontal_fov_to_80_coefficient,
                     radians_per_count=radians(2.2278481012658227), counts_per_unit=800, screen_diagonal=24)

    frc = FullRotationCalculator(dh1.primary_state, dh1.parameters, dh2.parameters)

    fr_c, fr_sens = frc.sensitivity_for(s1_sens=2, s2=dh2.primary_state)

    print(f'Full rotation & different applications, coefficient: {fr_c:.4f}, sensitivity: {fr_sens:.4f}')

    src = ScreenRatioCalculator(ratio1=.10, s1=dh2.primary_state, p1=dh2.parameters)

    dh2_s2 = dh2.get_state_for_fov(radians(40))

    src_c, src_sens = src.sensitivity_for(s1_sens=.0158, s2=dh2_s2)

    print(f'Screen ratio & same application, coefficient: {src_c:.4f}, sensitivity: {src_sens:.4f}')

    dc = DetailsCalculator(dh1.primary_state, dh1.parameters)

    print(f'Details, full rotation distance: {dc.full_rotation_units(sens=2):.4f}')

License
-------

Ephyra is released under version 2.0 of the `Apache License`_.

.. _Apache License: http://www.apache.org/licenses/LICENSE-2.0