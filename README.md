# Trekko_Software
<img src="https://github.com/sbcshop/Trekko_Software/raw/main/images/trekko_banner.jpg">


This Github provides a getting started guide and other working details for the Trekko - Pico GPS Logger.

### Features:

- Type C Power/UART

  
### Specifications:
- Board Supply Voltage: 5V
- Operating Pin Voltage: 3.3V


### Hardware Overview
#### Pinout
<img src="https://github.com/sbcshop/Trekko_Software/blob/main/images/trekko_pinout.jpg">

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
  * [Schematic](https://github.com/sbcshop/Trekko_Hardware)
  * [Hardware Files](https://github.com/sbcshop/Trekko_Hardware)
  * [Step File](https://github.com/sbcshop/Trekko_Hardware/blob/main/Mechanical%20Data/TREKKO.step)
  * [3D Casing File]()


## Related Products
  * [GPS External Antenna](https://shop.sb-components.co.uk/products/gps-external-antenna?_pos=1&_sid=7f1c5cecc&_ss=r) 
   
     ![GPS_External_Antenna](https://shop.sb-components.co.uk/cdn/shop/products/GPSAntenna_2.jpg?v=1640588714&width=300)   

  * [GPS HAT for Raspberry Pi](https://shop.sb-components.co.uk/products/gps-hat-for-raspberry-pi?_pos=6&_sid=7f1c5cecc&_ss=r) 
   
     ![gps-hat-for-raspberry-pi](https://shop.sb-components.co.uk/cdn/shop/products/GPSHATforRaspberryPi_5.png?v=1648553361&width=300) 

  * [IoTFi 4G/2G : IoT Board based on RP2040](https://shop.sb-components.co.uk/products/iotfi-2g-4g-iot-board-based-on-rp2040?variant=40430002307155) 
   
     ![IoTFi 4G/2G : IoT Board based on RP2040](https://shop.sb-components.co.uk/cdn/shop/products/Untitled-2_1.png?v=1679651257&width=300)
    
  * [UBlox GPS-RTK Breakout](https://shop.sb-components.co.uk/products/gps-rtk-hat-gps-rtk-hat-with-high-precision-rtk-gps-location-at-the-cm-level?_pos=3&_sid=7f1c5cecc&_ss=r) 
   
     ![UBlox GPS-RTK Breakout](https://shop.sb-components.co.uk/cdn/shop/products/03_32836ef3-a3d3-4039-bbd2-14d97fb53879.png?v=1675245485&width=300) 

 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
