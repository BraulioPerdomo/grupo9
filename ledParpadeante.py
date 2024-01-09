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
    from ledParpadeante import velocidadDeParpadeo
    
    #print(f"Valocidad: {velocidadDeParpadeo}")
    led1 = LED(14)
    led1.blink(velocidadDeParpadeo, velocidadDeParpadeo)

    while True:
        sleep(1)

if is_rpi:
    main()
else:
    circuit.run(main)