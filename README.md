# Trekko_Software
<img src="">


This Github provides a getting started guide and other working details for the Trekko - Pico GPS Logger.

### Features:

- Type C Power/UART

  
### Specifications:
- Board Supply Voltage: 5V
- Operating Pin Voltage: 3.3V


### Hardware Overview
#### Pinout
<img src="">

### Interfacing Details
- GPS module interfacing
  
  | Pico RP2040 | GPS L76 Module | Function |
  |---|---|---|
  |UART0 TX | RX | Serial UART connection |
  |UART0 RX | TX  | Serial UART connection |


## Getting Started with Trekko 
### 1. How to Install Boot Firmware in Pico of Trekko

- Mostly, Trekko will be provided with firmware pre-installed, so you can skip this step if firmware is already present and directly jump start programming by following the below Step 2.
- How to know whether firmware is already present: for this, just connect your Trekko to your laptop, and if no extra device is detected, that means firmware is present.
- And if you connect the Trekko to a laptop without pressing the boot button, if it shows mass storage device named as "RPI-RP2" like the one below, then the firmware is not installed.
- In this case, you need to add **MicroPython firmware** in Trekko. First, you need to *Press and Hold* the **BOOT** button, and then, without releasing the button, connect it to PC/laptop using Type C cable. Check below image for reference,

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the MicroPython firmware file provided in this repo above as ["Trekko_Firmware.uf2"](https://github.com/sbcshop/Trekko_Software/blob/main/Trekko_Firmware.uf2)
or to download the latest firmware file from the official site, [visit here](https://micropython.org/download/RPI_PICO/)     
     
- Drag and drop the MicroPython UF2 - ["Trekko_Firmware.uf2"](https://github.com/sbcshop/Trekko_Software/blob/main/Trekko_Firmware.uf2) file provided in this github onto the RPI-RP2 volume. Reference image shown below how to transfer any UF2 file or you can copy paste as well. Device will reboot and you are now running MicroPython on Trekko. 
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/firmware_installation.gif" />



## Resources
  * [Schematic]()
  * [Hardware Files]()
  * [Step File]()
  * [3D Casing File]()



## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
  
