/* 
The following is an in-progress adaptation of the Beginner's Guide to PID 
Controllers algorithm from Brett Beauregard, in a straight-line conversion to Rust.
As of 4-20-19 it is not complete.
*/

/*working variables*/

let mut lastTime: u32; // unsigned long
let mut Input, Output, Setpoint : i64; // doubles
let mut ITerm, lastInput: i64; // doubles
let kp, ki, kd : i64; // doubles
let SampleTime: i32 = 1000; //int, 1 sec
let outMin, outMax: i64; // doubles

#define DIRECT 0
#define REVERSE 1
int controllerDirection = DIRECT;

fn Compute()
{
   let mut now: u32 = millis();
   let mut timeChange: i32 = (now - lastTime);
   if(timeChange>=SampleTime)
   {
      /*Compute all the working error variables*/
      	let mut error: i64 = Setpoint - Input;
     	if(ITerm > outMax) 
     		ITerm = outMax;
      	else if(ITerm < outMin) 
      		ITerm= outMin;
      	let mut dInput: i64 = (Input - lastInput);
 
      /*Compute PID Output*/
		Output = kp * error + ITerm - kd * dInput;
		if(Output > outMax) Output = outMax;
      	else if(Output < outMin) Output = outMin;

      /*Remember some variables for next time*/
      	lastInput = Input;
      	lastTime = now;
   }
}
 
fn SetTunings(Kp: i64, Ki: i64, Kd: i64)
{
  	let SampleTimeInSec: i64 = (SampleTime as i64)/1000;
   	kp = Kp;
   	ki = Ki * SampleTimeInSec;
   	kd = Kd / SampleTimeInSec;

   	if(controllerDirection == REVERSE)
   	{
      	kp = (0 - kp);
      	ki = (0 - ki);
      	kd = (0 - kd);
   	}
}
 
fn SetSampleTime(NewSampleTime: i32)
{
   if (NewSampleTime > 0)
   {
      	let mut ratio: i64  = (NewSampleTime as i64
                      / SampleTime as i64;
      	ki *= ratio;
      	kd /= ratio;
      	SampleTime = NewSampleTime as u32;
   }
}

fn SetOutputLimits(Min: i64, Max: i64) 
// this way the PID won't try values that are impossible for it to achieve
{
   if(Min > Max) return;
   outMin = Min;
   outMax = Max;
    
   if(Output > outMax) Output = outMax;
   else if(Output < outMin) Output = outMin;
 
   if(ITerm> outMax) ITerm= outMax;
   else if(ITerm< outMin) ITerm= outMin;
}

fn SetControllerDirection(int Direction)
{
   controllerDirection = Direction;
}
