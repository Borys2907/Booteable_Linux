import os
import subprocess
import pyusb

# Identificar el dispositivo USB
busses = pyusb.USB.busses()
for bus in busses:
    for device in bus.devices:
        if device.idVendor == 0x0951 and device.idProduct == 0x1666:
            target_device = device
            break

# Utilizar "dd" para copiar la imagen del SO al dispositivo USB
subprocess.run(['dd', 'if=/home/borys/Descargas/Win10_22H2_Spanish_x64.iso', 'of=/media/borys/Parrot htb 5_1_2' + target_device.filename()])

# Avisar al usuario que la operación ha finalizado
print("La imagen del sistema operativo ha sido copiada en el dispositivo USB.")
