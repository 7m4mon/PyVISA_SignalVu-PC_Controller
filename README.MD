# PyVISA_SignalVu-PC_Controller

'PyVISA_SignalVu-PC Controller' adds a Virtual Numeric Keypad Controoler for Tektronix SignalVu-PC.

[image]

---
**SignalVu-PC application has a Numeric Keypad !**  
**Check its Toolbar menu, 'View' -> 'Numeric Keypad'**

[image]

---

## How to use:
1. Get the VISA Address of SignalVu-PC application.  
- SignalVu-PC application has a virtual GPIB Addres.
You can check it by "Open Choice Instrument Manager".  
[Image]
- You can also use by Socket Server.
It will enabled by "TekVISA LAN Server Control"  
[Image]
2. Enter SignalVu's VISA address to Textbox.
3. Press "*IDN?" button to open instrument.
4. Press a button of left row and enter number, then press button of right row.

---

This program used libraries, PySimpleGUI(LGPL) and PyVISA(MIT).