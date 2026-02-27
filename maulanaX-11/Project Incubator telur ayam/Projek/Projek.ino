#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Inisialisasi DHT11
#define DHTPIN 3
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Inisialisasi LCD I2C (alamat umum: 0x27 atau 0x3F)
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Relay pin
const int relayLampu = 7; // Relay 1 untuk lampu
const int relayFan   = 8; // Relay 2 untuk kipas

// Batas suhu
const float suhuAtas = 30.0;
const float suhuBawah = 30.0;  

void setup() {
  Serial.begin(9600);
  dht.begin();

  // Setup LCD
  lcd.init();
  lcd.backlight();
  ; 
  digitalWrite(relayFan, HIGH); 
  // Setup relay sebagai output
  pinMode(relayLampu, OUTPUT);
  pinMode(relayFan, OUTPUT);

  // Awal: matikan keduanya (aktif LOW)
  digitalWrite(relayLampu, HIGH);
}

void loop() {
  delay(100); // Delay antar pembacaan sensor

  float suhu = dht.readTemperature(); // Celsius
  float kelembaban = dht.readHumidity();

  // Cek jika pembacaan valid
  if (isnan(suhu) || isnan(kelembaban)) {
    Serial.println("Gagal membaca sensor DHT11!");
    lcd.setCursor(0, 0);
    lcd.print("Sensor Error    ");
    return;
  }

  // Tampilkan ke Serial Monitor
  Serial.print("Suhu: ");
  Serial.print(suhu);
  Serial.print(" C | Kelembaban: ");
  Serial.print(kelembaban);
  Serial.println(" %");

  // Tampilkan ke LCD
  lcd.setCursor(0, 0);
  lcd.print("Suhu: ");
  lcd.print(suhu, 1);
  lcd.print((char)223); // Derajat
  lcd.print("C     ");

  lcd.setCursor(0, 1);
  lcd.print("Kelembaban: ");
  lcd.print(kelembaban, 0);
  lcd.print("%         ");

  // Logika kontrol relay
  if (suhu > suhuAtas) {
    // Terlalu panas
    digitalWrite(relayLampu, HIGH); // Lampu mati
    digitalWrite(relayFan, LOW);    // Fan nyala
  } else if (suhu < suhuBawah) {
    // Terlalu dingin
    digitalWrite(relayLampu, LOW);  // Lampu nyala
    digitalWrite(relayFan, HIGH);   // Fan mati
  }
  // Jika suhu antara 37 - 39, kondisi tidak berubah
}