@echo off
setlocal enabledelayedexpansion

echo IPv4 cim lekerese...
echo.

for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do (
    set ipv4=%%a
    set ipv4=!ipv4:~1!
    echo Talalt IPv4 cim: !ipv4!
    echo !ipv4! > address.txt
    echo.
    echo Az IPv4 cim elmentve az address.txt fajlba!
    goto :found
)

:found
echo.
pause
