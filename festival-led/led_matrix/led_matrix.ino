#include <LedControl.h>
#define MAX 8
LedControl lc = LedControl(12, 11, 10, MAX);

void setup()
{
  for (int num = 0; num < MAX; num++)
  {
    lc.shutdown(num, false); // 절전모드 off
    lc.setIntensity(num, 8); // LED brightness set(0~15)
    lc.clearDisplay(num); // LED clear
  }
}

void loop()
{
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
