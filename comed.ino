int endstop = 53;

void setup() {
pinMode(12, OUTPUT);
pinMode(endstop, INPUT);
digitalWrite(12,LOW);

Serial.begin(9600);

}
void loop () {
if (Serial.available()) {
char c = Serial.read(); 
if (c == 'H') { 
  digitalWrite(12, HIGH);
  delay(3000); 
  
 /* if (digitalRead(endstop)==LOW){
    digitalWrite(12, LOW); 
    delay(1000);
  }  
*/
 while (digitalRead(endstop)==HIGH){
    delay(5);
  }
  digitalWrite(12, LOW); 
    delay(1000);
    

}
}
}
