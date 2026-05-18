from machine import ADC
from machine import Pin
import uasyncio as asyncio

class Veleta:
    def __init__(self, pin):
        self.pin = ADC(Pin(pin))
        
    async def leer_direccion(self):
        await asyncio.sleep(0)  # Cede control
        valor_adc = self.pin.read_u16()
        
        if ((valor_adc < 4080) or (valor_adc > 61440)):
            return "Norte"
        elif (8192 <= valor_adc <= 12272):
            return "Noreste"
        elif (12288 <= valor_adc <= 20480):
            return "Este"
        elif (20480 <= valor_adc <= 28672):
            return "Sureste"
        elif (28672 <= valor_adc <= 36864):
            return "Sur"
        elif (36864 <= valor_adc <= 45056):
            return "Suroeste"
        elif (45056 <= valor_adc <= 53248):
            return "Oeste"
        else:
            return "Noroeste"