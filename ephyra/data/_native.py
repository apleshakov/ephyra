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

try:
    from _ephyra import RT_AZIMUTHAL, RT_POLAR, FT_HORIZONTAL, FT_VERTICAL, FS_HORIZONTAL_PLUS, \
        FS_VERTICAL_MINUS, Parameters, FOVData, State
    from ._types import *
except ImportError:
    _READY = False
else:
    _READY = True
