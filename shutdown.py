import os,time
shutdown = True 
while shutdown:
    shutdown = input("Bạn muốn tắt máy không? (Yes / No): ")
    if shutdown == 'Yes':
        os.system("shutdown /s /t 10") 
        shutdown = False
    else:
        print("Wait..")
        time.sleep(30)
        shutdown = True