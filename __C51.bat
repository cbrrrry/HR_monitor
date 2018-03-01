@echo off
::This file was created automatically by CrossIDE to compile with C51.
C:
cd "\Users\carso\Documents\1. School\0. Spring 2018\Elec 292\lab4\"
"C:\CrossIDE\Call51\Bin\c51.exe" --use-stdout  "C:\Users\carso\Documents\1. School\0. Spring 2018\Elec 292\lab4\hr_monitor.c"
if not exist hex2mif.exe goto done
if exist hr_monitor.ihx hex2mif hr_monitor.ihx
if exist hr_monitor.hex hex2mif hr_monitor.hex
:done
echo done
echo Crosside_Action Set_Hex_File C:\Users\carso\Documents\1. School\0. Spring 2018\Elec 292\lab4\hr_monitor.hex
