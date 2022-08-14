/*
Copyright 2012 Jun Wako <wakojun@gmail.com>
Copyright 2015 Jack Humbert

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#pragma once

#include "config_common.h"

/* USB Device descriptor parameter */
#ifndef PRODUCT_ID
#define PRODUCT_ID   0x3435
#endif
#ifndef DEVICE_VER
#define DEVICE_VER   0x0001
#endif
#ifndef MANUFACTURER
#define MANUFACTURER jkeyne
#endif

/* key matrix size */
// Rows are doubled-up
#define MATRIX_ROWS 10
#define MATRIX_COLS 5

// wiring of each half
// Arduino Pin Labels:    A4, A3, A2, A1, A0
#define MATRIX_ROW_PINS { F1, F4, F5, F6, F7 }
// #define MATRIX_COL_PINS { B5, B4, E6, D7, C6 }
// Arduino Pin Labels:    D4, D5, D2, D7, D9
#define MATRIX_COL_PINS { D4, C6, D1, E6, B5 }

#define DIODE_DIRECTION COL2ROW
