#include <LedControl.h>
#define MAX 16
LedControl lc = LedControl(12, 11, 10, MAX);

String str;

void setup()
{
  Serial.begin(9600);
  for (int num = 0; num < MAX; num++)
  {
    lc.shutdown(num, false); // 절전모드 off
    lc.setIntensity(num, 2); // LED brightness set(0~15)
    lc.clearDisplay(num); // LED clear
  }
}

void loop()
{
  if(Serial.available())
  {
    char data = Serial.read();
    Serial.println(data);
    if(data == '2') str = ""; // start byte
    else if(data == '3') Serial.println(str); // end byte
    else str += data;
  }
  /*
  // 도트매트릭스의 LED를 첫번째 부터 1개씩 차례대로 ON
  for (int num = 0; num < MAX; num++)
  {
    for (int row = 7; row >= 0; row--)
    {
      for (int col = 0; col < 8; col++)
      {
        lc.setLed(num, col, row, true);
        delay(25);
      }
    }
  }

  // 도트매트릭스의 LED를 첫번째 부터 1개씩 차례대로 OFF
  for (int num = 0; num < MAX; num++)
  {
    for (int row = 7; row >= 0; row--)
    {
      for (int col = 0; col < 8; col++)
      {
        lc.setLed(num, col, row, false);
        delay(25);
      }
    }
  }
  */
}
