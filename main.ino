#include<SoftwareSerial.h>
#define rxPin 11
#define txPin 12
//char arr[] = "CMD,,026,,0x800,,0x8,,0x100,,0x5ac5,,0xc90c,,0x80e,,0x9b0c,,CMD";
//char arr[] = "anant";
//char arr[] = "1234567890";
//char arr = 'H';
//char arr[] = "93, 0, 41, 57, 63222, 75.587248, 28.362069, 295.300000, 16, 27, 21, 368.363098, 96978.093750, 31.450001";
//char arr[] = "<0x420>";
// char arr[] = "CMD,10,0,20,18,68196,75.587259,28.36205,284,16,5,41,-420.690002,-420.690002,-4END";
char arr[35];

SoftwareSerial xbee = SoftwareSerial(rxPin, txPin);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(19200);
  //pinMode(rxPin, INPUT);
  //pinMode(txPin, OUTPUT);
  xbee.begin(19200);

}

void loop() {
  // put your main code here, to run repeatedly:
//xbee.print('A');
//xbee.write(arr);
while (Serial.available()>0){
String s=Serial.readString();
strcpy (arr,s.c_str());
Serial.print("\n");
}
xbee.write(arr);
Serial.print(arr);
//Serial.println(arr);
delay(1000);
}
