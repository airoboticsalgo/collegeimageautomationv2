from flask import Flask,flash, request
from werkzeug.utils import secure_filename
import os
import numpy as np
from pathlib import Path
import re
import pandas as pd
import random
import shutil
from lib.logservice import logger as log

logger = log.get_singletonish_logger()
ALLOWED_EXTENSIONS = {'jpg'}
temp="temp"
dataset="collegefacedatabase"

def getdevicepath(devicename,makedir=False):
    current_directory = os.getcwd()
    parentpath=os.path.abspath(os.path.join(current_directory, os.pardir))
    dbfullpath=os.path.join(parentpath, dataset)
    dbdevicefullpath=os.path.join(dbfullpath, devicename)
    if makedir:
        createdir(dbdevicefullpath)
    return dbdevicefullpath
def getrecordpath(devicename,recordname,makedir=False):
    current_directory = os.getcwd()
    parentpath=os.path.abspath(os.path.join(current_directory, os.pardir))
    dbfullpath=os.path.join(parentpath, dataset)
    dbdevicefullpath=os.path.join(dbfullpath, devicename)
    dbrecoredfullpath=os.path.join(dbdevicefullpath, recordname)
    if makedir:
        createdir(dbrecoredfullpath)
    return dbrecoredfullpath


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def removefile(filename):
    if os.path.exists(filename): os.remove(filename)

def deletedir(dir):
    try:
        
        shutil.rmtree(dir)
    except OSError as e:
        logger.info(f"deleted file missing====Error: {e.filename}- {e.strerror}.")
    

    
def movefile(path1,path2):
    shutil.move(path1, path2)
    return
def dosavetemp(request):
     status="success"
     filename=""
     if 'file' not in request.files:
         
         print("request.files",request.files)
         status="failed:please upload the file"
         return status,filename,""
     file = request.files['file']
     if file.filename == '':
            status="failed:please upload the file"
            return status,filename,""
     
     if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        basefilename = Path(filename).stem
        # print("basefilename==",basefilename)
        rad=str(random.randint(10000,99999))
        basefilename=f"{basefilename}_{rad}.jpg"
        fullpath=os.path.join(temp, basefilename)
        file.save(fullpath)
        current_directory = os.getcwd()
        final_path = os.path.join(current_directory, fullpath)
        return status,final_path,filename
     return "failed","",""

def dosave(request):
     status="success"
     filename=""
     if 'file' not in request.files:
         
         print("request.files",request.files)
         status="failed:please upload the file"
         return status,filename
     file = request.files['file']
     if file.filename == '':
            status="failed:please upload the file"
            return status,filename
     
     if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        basefilename = Path(filename).stem
        # print("basefilename==",basefilename)
        rad=str(random.randint(10000,99999))
        basefilename=f"{basefilename}_{rad}.jpg"
        fullpath=os.path.join(temp, basefilename)
        file.save(fullpath)
        current_directory = os.getcwd()
        final_path = os.path.join(current_directory, fullpath)
        return status,final_path
     return "failed",""




def createdir(path):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, path)
    if not os.path.exists(final_directory):
     os.makedirs(final_directory)
    return


def getfilenamebypath(finder):
    status ="failed"
    error1="unknown person"
    print("finder len=",len(finder))

    data =pd.DataFrame(finder[0])
    print("finder data=",data)
    logger.info(f"finder data={data}")
    # emptydata=data.to_numpy()
    print("emptydata=",data.empty)
    if data.empty:
        return status,error1
    # print("to_json=",data.to_json())
    # print("data.columns[1]",data.columns[1][1][0])
    # print("data.columns[0]",data.columns[0][0][0])
    # j=data.index(0)
    # fullpath=j[0]
    fullpath=""
    k=0
    for i, j in data.iterrows():
    #  d=f"{i}=={k}=={j[0]}"
     fullpath=str(j[0])
     break
    #  print(d)
    #  k+=1
    status="success"
    print("fullpath=",fullpath)
    logger.info(f"fullpath={fullpath}")
    basefilename = Path(fullpath).stem

    print("recordname=",basefilename)
    logger.info(f"recordname={basefilename}")

    # print("finder value11 =",str(finder[0]).strip())
    # finalname=str(finder[0])
    # print("finder value =",finalname)
    # (
    # print("finder value2 =", (finalname.find("Empty DataFrame")))
    # if finalname.find("DataFrame") > -1 :
    #     return error1
    # afinder=np.array(finalname)
    # print("afinder12=",str(afinder[0]))
    # out_arr = numpy.char.split(str(afinder[0])," ") 
    # print("out_arr=",out_arr)
    # final=str(out_arr.item(0)).split(", """)
    # print("out_arr1=",final[0])
    # print("afinder=",afinder)
    # array1=str(afinder).strip()
    # array2=array1.split("  ")
    # print("ss=",array2)
    # out_arr = np.char.split(str(array1)," ") 
    # print("out_arr=",out_arr)
    # fname=""
    # for item in array2:
    #      print("item=",str(item))
    #      if str(item).endswith(".jpg"):
    #          fname=str(item)
       
    #          break

    # # res = np.any([s.find(".jpg") for s in array2])
    # print("fname=",fname)
   
    # basefilename = Path(array2[0]).stem
    # print("basefilename=",basefilename)
    return status,basefilename
createdir(temp)