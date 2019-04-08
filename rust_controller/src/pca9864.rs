//! Simple I2C driver to interface with the Adafruit PWM motor driver shield 
//! The shield uses the PCA9685 PWM driver.
//! Author: Patrick Gmerek

#![no_std]

extern crate cast;
extern crate embedded_hal as hal;
extern crate generic_array;

use core::mem;

use cast::u16;
use generic_array::typenum::consts::*;
use generic_array::{ArrayLength, GenericArray};
use hal::blocking::i2c::{Write, WriteRead};

mod pwm_frequency;
mod duty_cycle_m1;
mod duty_cycle_m2;

// PCA9685 driver
pub struct Pca9685<I2C> {
    i2c: I2C;
}

impl<I2C, E> Pca9685<I2C>
where
    I2C: WriteRead<Error = E> + Write<Error = E>,
{
    // Create a new driver from an I2C address
    pub fn new(i2c: I2C) -> Result<self, E> {
        let mut pca9685 = Pca9685 { i2c };

        // Reset all registers


