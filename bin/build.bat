rmdir /S /Q build
rmdir /S /Q dist

pyinstaller build.spec

xcopy /i /s ..\data .\dist\data

