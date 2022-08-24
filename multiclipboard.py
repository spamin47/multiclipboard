import clipboard
import sys
import json
import os
#testing git clone
#test
SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:  
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}    
    
lenArg = len(sys.argv)
if lenArg >= 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save" and lenArg == 3: #Save value into a key from clipboard
        data[sys.argv[2]] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data saved! Saved data:\n" + data[sys.argv[2]])
    elif command == "load" and lenArg == 3: #Copy value of key onto clipboard
        if sys.argv[2] in data:
            clipboard.copy(data[sys.argv[2]])
            print("Data loaded onto clipboard. Loaded data:\n" + data[sys.argv[2]])
        else:
            print("Key does not exist.")
    elif command == "list": #List data from saved file
        print(data)
    elif command == "delete": #delete file 
        if os.path.isfile(SAVED_DATA):
            os.remove(SAVED_DATA)
            print("File has been deleted.")
        else:
            print("File does not exist.")
    else:
        print("unkown command")
else:
    print("please pass exact command")