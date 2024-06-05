#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4); // Address, cols, rows

void setup() {
  lcd.init(); // Initialize the LCD
  lcd.backlight(); // Turn on backlight
  lcd.setCursor(0, 0); // Set cursor to row 0, column 0
  lcd.print("Hello, World!"); // Display message
}

void loop() {
  // ... (rest of your program)
}