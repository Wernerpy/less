#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,19,3);  // Устанавливаем дисплей
void setup()
{
  lcd.init();                     
  lcd.backlight();// Включаем подсветку дисплея
  lcd.print("iarduino.ru");
  lcd.setCursor(8, 1);
  lcd.print("LCD 1602");
  lcd.setCursor(19, 3);
  lcd.print("1");
}
void loop()
{
  // Устанавливаем курсор на вторую строку и нулевой символ.
  lcd.setCursor(0, 1);
  // Выводим на экран количество секунд с момента запуска ардуины
  lcd.print(millis()/1000);
}