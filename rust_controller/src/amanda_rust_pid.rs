/* 
The following is an in-progress adaptation of the Beginner's Guide to PID 
Controllers algorithm from Brett Beauregard, in a straight-line conversion to Rust.
As of 4-20-19 it is not complete.

references: 

https://github.com/japaric/zen/ -- embedded TWIP with PID on stm32 board
https://github.com/johsnick/rust_pid/blob/master/src/lib.rs - example rust PID
https://github.com/adeschamps/pid-controller/blob/master/src/lib.rs - example rust PID
*/

#![no_std]
#![no_main]

/* crates go here */
// extern crate panic_halt; 
// extern crate chrono; // for the millisecond function
/**/

// use cortex_m::asm;
// use cortex_m_rt::entry;

/*work_ing variables*/
// NOTE: stm32 and i64 variables?
// NOTE: preludes?
// NOTE: add getters

pub struct PIDController {

last_time: u32, // unsigned long
input: i64, 
output: i64,
setpoint: i64, // doubles
i_term: i64, 
last_input: i64, // doubles
k_p: i64, 
k_i: i64, 
k_d : i64, // doubles
sample_time: u32, //int, 1 sec
out_min: i64,
out_max: i64, // doubles
forward: bool,
reverse: bool,
controller_direction: bool,

}

pub trait Controller {

  fn Compute(&mut self);
  fn set_tunings(&mut self, k_p: i64, k_i: i64, k_d: i64);
  fn set_sample_time(&mut self, new_sample_time: i32);
  fn set_output_limits(&mut self, min: i64, max: i64);
  fn set_controller_direction(&mut self, direction: bool);

}

impl PIDController {
    /// Creates a new PID Controller.
    pub fn new(k_p: i64, k_i: i64, k_d: i64) -> PIDController {
        PIDController{
        last_time: 0,// unsigned long
        input : 0,
        output: 0,
        setpoint: 0,// doubles
        i_term: 0,
        last_input: 0,// doubles
        k_p: k_p, 
        k_i: k_i,
        k_d: k_d, // doubles
        sample_time: 1000, //int, 1 sec
        out_min: 0,
        out_max: 0, // doubles
        forward : true,
        reverse : false,
        controller_direction : true,
        }
    }
  }

impl Controller for PIDController{

  fn Compute(&mut self)
  {
     // let mut now: u32 = millis(); Time is tracked externally
     let mut now: u32 = 0; // THIS IS A BIG OLD PLACEHOLDER
     let mut time_change: u32 = now - self.last_time;
     if time_change >= self.sample_time
     {
        /*Compute all the work_ing error variables*/
        let mut error: i64 = self.setpoint - self.input;
        if self.i_term > self.out_max 
        { 
          self.i_term = self.out_max;
        }
        else if self.i_term < self.out_min
        {
          self.i_term = self.out_min;
        }

        let mut dinput: i64 = self.input - self.last_input;
   
        /*Compute PID output*/
        self.output = self.k_p * error + self.i_term - self.k_d * dinput;
        
        if self.output > self.out_max
        { 
          self.output = self.out_max;
        }
        
        else if self.output < self.out_min 
        {
         self.output = self.out_min;
        }

        /*Remember some variables for next time*/
        self.last_input = self.input;
        self.last_time = now;
     }
  }
   
  fn set_tunings(&mut self, k_p: i64, k_i: i64, k_d: i64)
  {
      let sample_time_in_sec: i64 = (self.sample_time as i64) / 1000;
      self.k_p = k_p;
      self.k_i = k_i * sample_time_in_sec;
      self.k_d = k_d / sample_time_in_sec;
      //The above code is for going forward, the below is for backward
      if self.controller_direction == self.reverse 
      {
          self.k_p = 0 - self.k_p;
          self.k_i = 0 - self.k_i;
          self.k_d = 0 - self.k_d;
      }
  }
   
  fn set_sample_time(&mut self, new_sample_time: i32) 
  // this is called externally, rather than tracking time by itself
  {
     if new_sample_time > 0
     {
          let mut ratio: i64  = new_sample_time as i64
                        / self.sample_time as i64;
          self.k_i *= ratio;
          self.k_d /= ratio;
          self.sample_time = new_sample_time as u32;
     }
  }

  fn set_output_limits(&mut self, min: i64, max: i64) 
  // this way the PID won't try values that are impossible for it to achieve
  {
    if min > max
    { 
      return;
    }
    self.out_min = min;
    self.out_max = max;
      
    if self.output > self.out_max
    {
      self.output = self.out_max;
    }
    else if self.output < self.out_min 
    {
      self.output = self.out_min;
    }
    if self.i_term > self.out_max
    {
      self.i_term = self.out_max;
    }
    else if self.i_term < self.out_min 
    {
      self.i_term= self.out_min;
    }
  }

  //Going backwards or forwards
  fn set_controller_direction(&mut self, direction: bool)
  {
     self.controller_direction = direction;
  }


}
