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
    lc.setIntensity(num, 8); // LED brightness set(0~15)
    lc.clearDisplay(num); // LED clear
  }
}

void loop()
{
  if (Serial.available())
  {
    char data = Serial.read();
    Serial.println(data);

    // led matrix control protocol
    // 0x02 num row col 0x03

    if (data == 0x02) str = "";
    else if (data == 0x03)
    {
      if (str == "")
      {
        for (int num = 0; num < MAX; num++)
          lc.clearDisplay(num); // LED clear
      }
      lc.setLed(atoi(str[0]), atoi(str[1]), atoi(str[2]), true);
    }
    else str += data;
  }
}
