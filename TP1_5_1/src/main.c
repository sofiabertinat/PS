/*
 * main.c
 *
 *  Created on: Jul 24, 2022
 *      Author: sofia Bertinat
 *
 */


#include "sapi.h"
#include "arm_math.h"


uint16_t printQ7(q7_t n,char *buf)
{
   int i;
   float ans=(n&0x80)?-1:0;
   for(i=1;i<8;i++)
   {
      if(n&(0x80>>i)){
         ans+=1.0/(1U<<i);
      }
   }
   return sprintf(buf,"q7: %i float:%.20f\r\n",n,ans);
}

q15_t multiQ7(q7_t a,q7_t b)
{
   q15_t ans;
   ans=a*b;
   ans<<=1;
   return ans>>8;
}

int main ( void ) {
   uint16_t sample = 0;
   int16_t len;
   char buf [ 200 ];

   boardConfig (                  );
   uartConfig  ( UART_USB, 115200 );
   adcConfig   ( ADC_ENABLE       );
   cyclesCounterInit ( EDU_CIAA_NXP_CLOCK_SPEED );

   q7_t a=0x40;
   q7_t b=0x23;

   q7_t m=0x00;

   while(1) {
      cyclesCounterReset();

      len=printQ7(a,buf);
      uartWriteByteArray ( UART_USB ,buf ,len);
      len=printQ7(b,buf);
      uartWriteByteArray ( UART_USB ,buf ,len);

      m=multiQ7(a,b);
      len=printQ7(m,buf);
      uartWriteByteArray ( UART_USB ,buf ,len);

      gpioToggle ( LED1 );

      while(cyclesCounterRead()< EDU_CIAA_NXP_CLOCK_SPEED/1)
         ;
   }
}

