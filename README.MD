# PyVISA_SignalVu-PC_Controller

'PyVISA_SignalVu-PC Controller' adds a Virtual Numeric Keypad for Tektronix SignalVu-PC.

![](https://github.com/7m4mon/PyVISA_SignalVu-PC_Controller/blob/main/PyVISA_SignalVu-PC_Controller_sc.png)  

---

**SignalVu-PC application has a Numeric Keypad !**  
**Check its Toolbar menu, 'View' -> 'Numeric Keypad'**

---

## How to use:
1. Get the VISA Address of SignalVu-PC application.  
- SignalVu-PC application has a virtual GPIB Addres.
You can check it by "Open Choice Instrument Manager".  
![](https://github.com/7m4mon/PyVISA_SignalVu-PC_Controller/blob/main/signalvu-address.png)  
- You can also use by Socket Server.
It will be enabled by "TekVISA LAN Server Control"  
![](https://github.com/7m4mon/PyVISA_SignalVu-PC_Controller/blob/main/start_socketserver.png)  
2. Enter SignalVu's VISA address to Textbox.
3. Press "*IDN?" button to open instrument.
4. Press a button of left row and enter number, then press button of right row.

---

This program was used libraries, PySimpleGUI(LGPL) and PyVISA(MIT).
