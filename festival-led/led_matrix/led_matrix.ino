#include <LedControl.h>
#define MAX 8
LedControl lc = LedControl(12, 11, 10, MAX);

String str;

void setup()
{
  Serial.begin(115200);
  for (int num = 0; num < MAX; num++)
  {
    lc.shutdown(num, false); // 절전모드 off
    lc.setIntensity(num, 2); // LED brightness set(0~15)
    lc.clearDisplay(num); // LED clear
  }
  pinMode(13, OUTPUT);
}

void loop()
{
  if(Serial.available())
  {
    char data = Serial.read();
    Serial.println(data);
    if(data == 0x02) str = ""; // start byte
    else if(data == 0x03) 
    {
      if(str == "1111") digitalWrite(13, HIGH);
      else if(str == "0000") digitalWrite(13, LOW);
      
      lc.setLed(atoi(str[0]), atoi(str[1]), atoi(str[2]), atoi(str[3]));
    }
    else str += data;
  }
  
  // 도트매트릭스의 LED를 첫번째 부터 1개씩 차례대로 ON
  for (int num = 0; num < MAX; num++)
  {
    for (int row = 0; row < 8; row++)
    {
      for (int col = 0; col < 8; col++)
      {
        lc.setLed(num, row, col, true);
        delay(25);
      }
    }
  }

  // 도트매트릭스의 LED를 첫번째 부터 1개씩 차례대로 OFF
  for (int num = 0; num < MAX; num++)
  {
    for (int row = 0; row < 8; row++)
    {
      for (int col = 0; col < 8; col++)
      {
        lc.setLed(num, row, col, false);
        delay(25);
      }
    }
  }
  
}
