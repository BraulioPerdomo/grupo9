from pathlib import Path
is_rpi = Path("/etc/rpi-issue").exists()

if not is_rpi:
    from tkgpio import TkCircuit

    # initialize the circuit inside the GUI

    configuration = {
        "width": 300,
        "height": 200,
        "leds": [
            {"x": 50, "y": 40, "name": "LED 1", "pin": 14},
        ],
    }

    circuit = TkCircuit(configuration)
#@circuit.run
def main ():
    
    # now just write the code you would use on a real Raspberry Pi
    
    from gpiozero import LED, Button
    from time import sleep
    import leerConfiguracion 
    
    led1 = LED(14)
    led1.blink(leerConfiguracion.velocidadDeParpadeo, leerConfiguracion.velocidadDeParpadeo)

    while True:
        sleep(1)
        leerConfiguracion.leerConfiguracion()
        print(f"Velocidad: {leerConfiguracion.velocidadDeParpadeo}")
        led1.blink(leerConfiguracion.velocidadDeParpadeo, leerConfiguracion.velocidadDeParpadeo)

if is_rpi:
    main()
else:
    circuit.run(main)