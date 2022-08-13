/* USB Device descriptor parameter */
#define PRODUCT_ID   0x3435
#define DEVICE_VER   0x0001
#define MANUFACTURER tshort

/* key matrix size */
// Rows are doubled-up
#define MATRIX_ROWS 10
#define MATRIX_COLS 5

// wiring of each half
// Arduino Pin Labels:    A4, A3, A2, A1, A0
#define MATRIX_ROW_PINS { F1, F4, F5, F6, F7 }
// Arduino Pin Labels:    D4, D5, D2, D7, D9
#define MATRIX_COL_PINS { D4, C6, D1, E6, B5 }

#define DIODE_DIRECTION COL2ROW

#define USE_SERIAL
//#define USE_I2C

/* Select hand configuration */
#define MASTER_LEFT
//#define MASTER_RIGHT

#define EE_HANDS
