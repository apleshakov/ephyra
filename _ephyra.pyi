#
# SPDX-License-Identifier: Apache-2.0
#
# Copyright 2020 Andrey Pleshakov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# TODO: provide actual definitions <AP>

RT_AZIMUTHAL: int
RT_POLAR: int
FT_HORIZONTAL: int
FT_VERTICAL: int
FS_HORIZONTAL_PLUS: int
FS_VERTICAL_MINUS: int


class Parameters:
    pass


class FOVData:
    pass


class State:
    pass


class DataHelper:
    pass


class FullRotationCalculator:
    pass


class ScreenRatioCalculator:
    pass


class ScreenDistanceCalculator:
    pass


class DetailsCalculator:
    pass


def calculate_screen_width_height() -> None: ...


def calculate_fov() -> None: ...


def convert_fov_to_aspect_ratio() -> None: ...


def radians_per_unit_measure() -> None: ...


def rotation_ltr_measure() -> None: ...


def radians_for_ratio_from_center() -> None: ...


def screen_ratio_ltr_measure() -> None: ...


def radians_for_distance_from_center() -> None: ...


def screen_distance_ltr_measure() -> None: ...


def horizontal_4_to_3_fov_coefficient() -> None: ...


def horizontal_fov_to_80_coefficient() -> None: ...
