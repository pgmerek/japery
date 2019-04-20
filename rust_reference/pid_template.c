/*
This is taken directly from Brett Beauregard's "Improving The Beginner's PID" tutorial, and uses his suggestions 
on how to smooth and improve the algorithm. It does not implement interrupts or manual PID override.

http://brettbeauregard.com/blog/2011/04/improving-the-beginners-pid-introduction/
*/


/*working variables*/
unsigned long lastTime;
double Input, Output, Setpoint;
double ITerm, lastInput;
double kp, ki, kd;
int SampleTime = 1000; //1 sec
double outMin, outMax;

#define DIRECT 0
#define REVERSE 1
int controllerDirection = DIRECT;

void Compute()
{
   unsigned long now = millis();
   int timeChange = (now - lastTime);
   if(timeChange>=SampleTime)
   {
      /*Compute all the working error variables*/
      	double error = Setpoint - Input;
     	if(ITerm > outMax) 
     		ITerm = outMax;
      	else if(ITerm < outMin) 
      		ITerm= outMin;
      	double dInput = (Input - lastInput);
 
      /*Compute PID Output*/
		Output = kp * error + ITerm - kd * dInput;
		if(Output > outMax) Output = outMax;
      	else if(Output < outMin) Output = outMin;

      /*Remember some variables for next time*/
      	lastInput = Input;
      	lastTime = now;
   }
}
 
void SetTunings(double Kp, double Ki, double Kd)
{
  	double SampleTimeInSec = ((double)SampleTime)/1000;
   	kp = Kp;
   	ki = Ki * SampleTimeInSec;
   	kd = Kd / SampleTimeInSec;

   	if(controllerDirection ==REVERSE)
   	{
      	kp = (0 - kp);
      	ki = (0 - ki);
      	kd = (0 - kd);
   	}
}
 
void SetSampleTime(int NewSampleTime)
{
   if (NewSampleTime > 0)
   {
      	double ratio  = (double)NewSampleTime
                      / (double)SampleTime;
      	ki *= ratio;
      	kd /= ratio;
      	SampleTime = (unsigned long)NewSampleTime;
   }
}

void SetOutputLimits(double Min, double Max) 
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

void SetControllerDirection(int Direction)
{
   controllerDirection = Direction;
}
