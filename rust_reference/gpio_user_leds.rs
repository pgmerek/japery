// #![deny(unsafe_code)]
#![deny(warnings)]
#![no_std]
#![no_main]
 
extern crate cortex_m;
#[macro_use(entry, exception)]
extern crate cortex_m_rt as rt;
extern crate f3;
extern crate panic_semihosting;
 
use f3::hal::delay::Delay;
use f3::hal::prelude::*;
use f3::hal::stm32f30x;
use f3::led::Led;
use rt::ExceptionFrame;
 
entry!(main);
 
fn main() -> ! {
    let cp = cortex_m::Peripherals::take().unwrap();
    let dp = stm32f30x::Peripherals::take().unwrap();
 
    let mut flash = dp.FLASH.constrain();
    let mut rcc = dp.RCC.constrain();
    let mut gpioe = dp.GPIOE.split(&mut rcc.ahb);
 
    // clock configuration using the default settings (all clocks run at 8 MHz)
    let clocks = rcc.cfgr.freeze(&mut flash.acr);
    // TRY this alternate clock configuration (all clocks run at 16 MHz)
    // let clocks = rcc.cfgr.sysclk(16.mhz()).freeze(&mut flash.acr);
 
    let mut led: Led0 = gpioe
        .pe8
        .into_push_pull_output(&mut gpioe.moder, &mut gpioe.otyper)
        .into();  
    let mut led: Led1 = gpioe
        .pe9
        .into_push_pull_output(&mut gpioe.moder, &mut gpioe.otyper)
        .into();
    let mut led: Led2 = gpioe
        .pe10
        .into_push_pull_output(&mut gpioe.moder, &mut gpioe.otyper)
        .into();
    let mut led: Led3 = gpioe
        .pe11
        .into_push_pull_output(&mut gpioe.moder, &mut gpioe.otyper)
        .into();
    let mut led: Led4 = gpioe
        .pe12
        .into_push_pull_output(&mut gpioe.moder, &mut gpioe.otyper)
        .into();
    let mut led: Led5 = gpioe
        .pe13
        .into_push_pull_output(&mut gpioe.moder, &mut gpioe.otyper)
        .into();
    let mut led: Led6 = gpioe
        .pe14
        .into_push_pull_output(&mut gpioe.moder, &mut gpioe.otyper)
        .into();
    let mut led: Led7 = gpioe
        .pe15
        .into_push_pull_output(&mut gpioe.moder, &mut gpioe.otyper)
        .into();   

        
    let mut delay = Delay::new(cp.SYST, clocks);
 
    loop {
        led0.on();
        delay.delay_ms(1_000_u16);
        led0.off();
        delay.delay_ms(1_000_u16);
        led1.on();
        delay.delay_ms(1_000_u16);
        led1.off();
        delay.delay_ms(1_000_u16);
        led2.on();
        delay.delay_ms(1_000_u16);
        led2.off();
        delay.delay_ms(1_000_u16);
        led3.on();
        delay.delay_ms(1_000_u16);
        led3.off();
        delay.delay_ms(1_000_u16);
        led4on();
        delay.delay_ms(1_000_u16);
        led4off();
        delay.delay_ms(1_000_u16);
        led5.on();
        delay.delay_ms(1_000_u16);
        led5.off();
        delay.delay_ms(1_000_u16);
        led6.on();
        delay.delay_ms(1_000_u16);
        led6.off();
        delay.delay_ms(1_000_u16);
        led7.on();
        delay.delay_ms(1_000_u16);
        led7.off();
        delay.delay_ms(1_000_u16);        
    }
}
 
exception!(HardFault, hard_fault);
 
fn hard_fault(ef: &ExceptionFrame) -> ! {
    panic!("{:#?}", ef);
}
 
exception!(*, default_handler);
 
fn default_handler(irqn: i16) {
    panic!("Unhandled exception (IRQn = {})", irqn);
}
