from gpiozero import CPUTemperature
import time

while True:
    temp = CPUTemperature()
    cpu_temp = round(temp.temperature, 1)

    print("Teplota CPU je " + str(cpu_temp) + "°C")
    
    time.sleep(1)  # Pauza 1 sekunda medzi každým meraním teploty
