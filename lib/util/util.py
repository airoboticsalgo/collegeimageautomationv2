from datetime import datetime
def printcurrenttime(msg=""):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S:%f")
    print(f"{msg}-date and time =", dt_string)
    