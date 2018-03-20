#include<Servo.h>
int spin=8;
Servo s;
String d;
 
void setup() {
  s.attach(spin);
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  
  s.write(90);
  if(Serial.available() >0 ){
   
  char c =Serial.read();
     d += c;
     }
      Serial.println(d);
  
    if(d[0] == 'a'){
      
      s.write(30);
      delay(500);
    }
    else if(d[0] == 'b') {
      s.write(150);
      delay(500);
      
    }
  d="";
  



  
Serial.flush();
}

