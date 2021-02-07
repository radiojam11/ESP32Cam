import esp32

esp32.hall_sensor()     # read the internal hall sensor
esp32.raw_temperature() # read the internal temperature of the MCU, in Farenheit
esp32.ULP()             # access to the Ultra-Low-Power Co-processor