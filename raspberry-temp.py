import subprocess
import re
import time

while True:
    try:
        # Spustím príkaz "vcgencmd measure_temp" a získam výsledok
        result = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")

        # Analyzujem výsledok pomocou regulárneho výrazu na získanie teploty
        match = re.search(r'temp=(\d+\.\d+)', result)
        if match:
            cpu_temp = round(float(match.group(1)), 1)
            print("Teplota CPU je " + str(cpu_temp) + "°C")
        else:
            print("Nepodarilo sa získať teplotu.")
            
        # Pauza 1 sekunda medzi každým meraním teploty
        time.sleep(1)  
    except KeyboardInterrupt:
        print("Program ukončený.")
        break
