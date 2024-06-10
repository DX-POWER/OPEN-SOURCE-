#_-_-_ADVANCE_METHOD_PROTECT_-_-_#
#_-_-_GIFT_BY_DX_-_-_#
#_-_-_CODING_BY_-_-_PRINCE RONI_-_-_#


#ADVANCE PYTHON PROGRAMMING  PAID COURSE 
#ALL TELETEST ADVANCE CODING VIDEO 68
#COURSE  PRICE  : 1000 TK

        #OFFER
#70% DISCOUNT  COURSE  PRICE  300TK 
#OFFER END DATE : 15/06/2024

#CONTACT  :    TELEGRAM ID    :    @dxPrince150


#__________#
import psutil
#______________________________________#
def capture_module_killar(module_name):
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if module_name in proc.info['name']:
                print(f"Module {module_name} found with PID {proc.info['pid']}")
                print(f"Username: {proc.info['username']}")
                print("Killing the module...")
                proc.terminate()
                print("Module killed successfully")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        else:
            exit('IF YOU BAD I AM DX YOUR DAD MIND IT NOOB')


                              #Set packages module name
module_name = "killar"  # Replace with the module name you want to capture

capture_module_killar(module_name)
