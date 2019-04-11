# Motor Measurements

To characterize a [dc motor](https://www.pololu.com/product/3262/specs), two experiments were conducted. The first experiment makes use of a Prony brake, where torque is calculated though measured force. A relationship between torque & angular speed, and torque & current is then observed. Further, we can determine the torque coefficient of the motor. In the second experiment, other motor parameters are determined such as the armature resistance, the armature inductance, and the electromotive force (emf) coefficient.

## Prony Brake

### Equations

The driving torque $T_{em}​$ of a dc motor is given by
$$
T_{em} = k_m \Phi_p i_a
\tag{1}
$$
where, $k_m$ is the torque coefficient, $\Phi_{p}$ is the excitation flux, and $i_{a}$ is the armature current.



The back emf of a dc motor is given by
$$
E = k_e \Phi_p \omega
\tag{2}
$$
where, $k_e$ is the emf coefficient, and $\omega$ is the angular speed of the shaft.



Assuming that the excitation flux $\Phi_p$ is constant, $K_m = k_m \Phi_p$ and $K_e = k_e \Phi_p​$ can be made in eq. (1) and (2) respectively, without lack of generality.



Recall the relationship between torque and force. That is,
$$
T_{em} = r F_{net}
\tag{3}
$$
where, $r​$ is the radius of the drive wheel.

### Materials

* two 20-Newton spring scales
* shoelace
* tachometer
* power supply
* ammeter

### Procedure

Using the rated voltage of the motor, connect the leads to a power supply such that the drive wheel rotates in the clockwise direction. Using the tachometer and ammeter, record the angular speed and current, respectively. These measurements correspond to the no-load speed and no-load current, respectively. Note that under no load, the driving torque $T_{em}=0$.

Attach each end of the shoelace to the Newton spring scales. Both ends should be under equal tension when placed under the stationary drive wheel (see setup1.png). Record the speed, current, and the driving torque. The driving torque is calculated using eq. (3). Note that the net force $F_{net} = F_{2} - F_{1}$, where $F_{2}$ and $F_{1}$ are the measured forces from the spring scales. Increase the prony brake height in 1cm increments and record the speed, current, and torque. For higher driving torques, the prony brake height can be increased in 0.5cm increments.

Repeat the process for the counter-clockwise direction of the motor.

Plot speed vs torque and current vs torque. Using eq. (1), calculate the torque coefficient $K_m$ of the motor.

## Other Measurements

### Equations

A dc motor consists of an armature resistance $R_{a}​$ and inductance $L_{a}​$. When rotating, the motor produces a back emf which is proportional to the angular speed of the shaft, given in eq. (2). The electrical equation of a dc motor is given by
$$
v_{a} = R_{a}i_{a}+L_{a} \frac{di_{a}}{dt} + E
\tag{4}
$$
where, $v_{a}$ is the applied armature voltage, $i_{a} $ is the armature current, and $E$ is the back emf.

### Materials

* multimeter
* power supply
* tachometer

### Procedure

Using the multimeter, measure the armature resistance and inductance. Starting at the rated dc voltage of the motor, measure the speed and current using the tachometer and ammeter, respectively. Calculate the back emf $E$ using eq. (4). Note that for a dc applied voltage, $di_{a}/dt=0​$. Decrement the voltage in steps of 1V-2V and record the speed, current, and emf.

Repeat the process for the drive wheel rotating in the opposite direction.

Using eq. (2), calculate the emf coefficient $K_e​$ of the motor.

## References

* [Make a Prony Brake to Analyze Motor Performance](http://www.gearseds.com/files/sample_lesson2.pdf)
* [Digital Control of Electrical Drives](https://www.springer.com/us/book/9780387259857)