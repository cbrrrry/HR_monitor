@echo off
::This file was created automatically by CrossIDE to compile with C51.
C:
cd "\Users\carso\Documents\1. School\0. Spring 2018\Elec 292\lab4\"
"C:\CrossIDE\Call51\Bin\c51.exe" --use-stdout  "C:\Users\carso\Documents\1. School\0. Spring 2018\Elec 292\lab4\frequency.c"
if not exist hex2mif.exe goto done
if exist frequency.ihx hex2mif frequency.ihx
if exist frequency.hex hex2mif frequency.hex
:done
echo done
echo Crosside_Action Set_Hex_File C:\Users\carso\Documents\1. School\0. Spring 2018\Elec 292\lab4\frequency.hex
