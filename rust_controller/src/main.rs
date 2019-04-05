fn main() {
    println!("Hello, world!");
}
/* TWIP Controller in Rust for the STM32F303 Discovery Board
@author A Voegtlin
Last revision: 4/4/2019
*/

// include libraries
extern crate pg; // make my life easier
use core:: iter; // to use timers
use pg::led::LEDS; // for LEDs
use pg::peripheral; // so I can refer to registers by name and use functions


// define names

// PID tilt values

// PID yaw variables (no integral value)

// curr, previous, diff

// iteration counter for checking if we're just starting up

// motor output variables

// bluetooth variables

// on-board mpu variables

// If using GPIO pins, initialize your output pins. All pins are inputs by default
// -- Remember to turn on the clock for the peripheral in order for it to be powered on. 


/* Setup section */

/* loop section 

// startup portion



// post-startup portion

*/

/* HELPER FUNCTIONS */

// initialize PWM 

// get info from MPU (on-board or attached) to inititialize yaw-pitch-roll

// Get info from bluetooth buffer to update yaw-pitch-roll

