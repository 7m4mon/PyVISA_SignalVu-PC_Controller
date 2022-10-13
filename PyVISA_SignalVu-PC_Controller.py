# PyVISA_SignalVu-PC Controller
# Date: 2022.Nov.1
# Author: 7M4MON (https://github.com/7m4mon/ , http://nomulabo.com)
# License: LGPL (Same as PySimpleGUI)
# Repository URL: https://github.com/7m4mon/PyVISA_SignalVu-PC_Controller
# Description: This program adds a Virtual Numeric Keypad Controoler for Tektronix SignalVu-PC.

import PySimpleGUI as sg
sg.theme('DarkTeal6')
import pyvisa
import os

cmdStr = ''
cmdCenterStr = 'SPEC:FREQ:CENT '
cmdSpanStr = 'SPEC:FREQ:SPAN '
cmdRlevStr = 'INP:RLEV '

HeightBtn = 2
WidthWideBtn = 12
WidthNumBtn = 5
WidthAddressInput = 39

rm = pyvisa.ResourceManager()
inst = 0

defaultAddr = 'GPIB8::1::INSTR'     # Virtual GPIB, or Socket Server 'TCPIP0::127.0.0.1::4000::SOCKET'
addressTxtFileName = 'VISA_DEFAULT_ADDRESS'
if os.path.isfile(addressTxtFileName):
    f= open(addressTxtFileName)
    defaultAddr = f.read()
    f.close()

layout = [[sg.Text('Address'), sg.InputText(defaultAddr, size=(WidthAddressInput,1), key='InpAddr'), sg.Button('*IDN?', key='BtnIdn')],
          [sg.Text('Please open instrument with IDN Button', key='TextRcv')],
          [sg.Text('Here is the Command String', key='TextCmd')],
          [sg.Button('Center', size=(WidthWideBtn,HeightBtn), key='BtnCenter'), sg.Button('7', size=(WidthNumBtn,HeightBtn), key='BtnNum7'), sg.Button('8', size=(WidthNumBtn,HeightBtn), key='BtnNum8'), sg.Button('9', size=(WidthNumBtn,HeightBtn), key='BtnNum9'), sg.Button('GHz, dBm', size=(WidthWideBtn,HeightBtn), key='BtnGHzdBm')],
          [sg.Button('Span', size=(WidthWideBtn,HeightBtn), key='BtnSpan'), sg.Button('4', size=(WidthNumBtn,HeightBtn), key='BtnNum4'), sg.Button('5', size=(WidthNumBtn,HeightBtn), key='BtnNum5'), sg.Button('6', size=(WidthNumBtn,HeightBtn), key='BtnNum6'), sg.Button('MHz', size=(WidthWideBtn,HeightBtn), key='BtnMHz')],
          [sg.Button('Amplitude', size=(WidthWideBtn,HeightBtn), key='BtnAmplitude'), sg.Button('1', size=(WidthNumBtn,HeightBtn), key='BtnNum1'), sg.Button('2', size=(WidthNumBtn,HeightBtn), key='BtnNum2'), sg.Button('3', size=(WidthNumBtn,HeightBtn), key='BtnNum3'), sg.Button('kHz', size=(WidthWideBtn,HeightBtn), key='BtnKHz')],
          [sg.Button('BackSpace', size=(WidthWideBtn,HeightBtn), key='BtnBackSpace'), sg.Button('0', size=(WidthNumBtn,HeightBtn), key='BtnNum0'), sg.Button('.', size=(WidthNumBtn,HeightBtn), key='BtnNum.'), sg.Button('-', size=(WidthNumBtn,HeightBtn), key='BtnNum-'), sg.Button('Hz', size=(WidthWideBtn,HeightBtn), key='BtnHz')]]

window = sg.Window('PyVISA SignalVu-PC Controller', layout, icon ='icon.ico')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        rm.close()
        f= open(addressTxtFileName, 'w')
        f.write(defaultAddr)
        f.close()
        break

    ## I think there is more simple method....
    if event == 'BtnIdn':
        defaultAddr = values['InpAddr']
        inst = rm.open_resource(defaultAddr)
        cmdStr = '*IDN?'
        window['TextCmd'].update(cmdStr)
        inst.write(cmdStr)
        inst_str = inst.read()
        inst_str = inst_str.replace('\n', '')
        window['TextRcv'].update(inst_str)
    if event == 'BtnBackSpace':
        if len(cmdStr) > 0:
            cmdStr = cmdStr[:-1]
            window['TextCmd'].update(cmdStr)
    if event == 'BtnCenter':
        cmdStr = cmdCenterStr
        window['TextCmd'].update(cmdStr)
    if event == 'BtnSpan':
        cmdStr = cmdSpanStr
        window['TextCmd'].update(cmdStr)
    if event == 'BtnAmplitude':
        cmdStr = cmdRlevStr
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum0':
        cmdStr += '0'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum.':
        cmdStr += '.'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum-':
        cmdStr += '-'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum1':
        cmdStr += '1'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum2':
        cmdStr += '2'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum3':
        cmdStr += '3'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum4':
        cmdStr += '4'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum5':
        cmdStr += '5'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum6':
        cmdStr += '6'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum7':
        cmdStr += '7'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum8':
        cmdStr += '8'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnNum9':
        cmdStr += '9'
        window['TextCmd'].update(cmdStr)
    if event == 'BtnGHzdBm':
        if ('FREQ' in cmdStr):
            cmdStr += 'GHZ'
        if ('LEV' in cmdStr):
            cmdStr += 'DBM'
        window['TextCmd'].update(cmdStr)
        if inst != 0:
            inst.write(cmdStr)
        else:
            sg.popup('Please open instrument with IDN Button')
    if event == 'BtnMHz':
        if ('FREQ' in cmdStr):
            cmdStr += 'MHZ'
        if ('LEV' in cmdStr):
            cmdStr += 'DBM'
        window['TextCmd'].update(cmdStr)
        if inst != 0:
            inst.write(cmdStr)
        else:
            sg.popup('Please open instrument with IDN Button')
    if event == 'BtnKHz':
        if ('FREQ' in cmdStr):
            cmdStr += 'KHZ'
        if ('LEV' in cmdStr):
            cmdStr += 'DBM'
        window['TextCmd'].update(cmdStr)
        if inst != 0:
            inst.write(cmdStr)
        else:
            sg.popup('Please open instrument with IDN Button')
    if event == 'BtnHz':
        if ('FREQ' in cmdStr):
            cmdStr += 'HZ'
        if ('LEV' in cmdStr):
            cmdStr += 'DBM'
        window['TextCmd'].update(cmdStr)
        if inst != 0:
            inst.write(cmdStr)
        else:
            sg.popup('Please open instrument with IDN Button')
window.close()