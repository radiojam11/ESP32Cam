from machine import ADC

adc = ADC(Pin(32))          # create ADC object on ADC pin
adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v

adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)
adc.read()                  # read value using the newly configured attenuation and width


"""
ESP32 specific ADC class method reference:

ADC.atten(attenuation)
This method allows for the setting of the amount of attenuation on the input of the ADC. This allows for a wider possible input voltage range, at the cost of accuracy (the same number of bits now represents a wider range). The possible attenuation options are:

ADC.ATTN_0DB: 0dB attenuation, gives a maximum input voltage of 1.00v - this is the default configuration

ADC.ATTN_2_5DB: 2.5dB attenuation, gives a maximum input voltage of approximately 1.34v

ADC.ATTN_6DB: 6dB attenuation, gives a maximum input voltage of approximately 2.00v

ADC.ATTN_11DB: 11dB attenuation, gives a maximum input voltage of approximately 3.6v

Warning

Despite 11dB attenuation allowing for up to a 3.6v range, note that the absolute maximum voltage rating for the input pins is 3.6v, and so going near this boundary may be damaging to the IC!

ADC.width(width)
This method allows for the setting of the number of bits to be utilised and returned during ADC reads. Possible width options are:

ADC.WIDTH_9BIT: 9 bit data

ADC.WIDTH_10BIT: 10 bit data

ADC.WIDTH_11BIT: 11 bit data

ADC.WIDTH_12BIT: 12 bit data - this is the default configuration
 
"""