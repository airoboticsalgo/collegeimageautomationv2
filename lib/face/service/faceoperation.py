from lib.face.core import Face
from . import fileoperation
import os
from lib.logservice import logger as log
from lib.util import util 
logger = log.get_singletonish_logger()
# db_path1="E:/python_workspace/face_deepface1/dataset551"
# db_path1="E:/python_workspace/face_deepface1/dataset"

def finderoneface(devicename,img_path1,refresh_database=False):
        status="failed"
        error2="Human face not available.Please confirm that the image is a face photo"
        error3="More than 1 human face available.kindly upload one human face image file"
        name=""
        face_objs=[]
        finder=[]
        try:
            util.printcurrenttime("1.010")
            face_objs = Face.extract_faces(img_path =img_path1)
            util.printcurrenttime("1.011")
        except:
            face_objs=[]
            # print("Total face=0")
        logger.info(f"Total face={len(face_objs)}")

        print("Total face=",len(face_objs))
        util.printcurrenttime("1.1")
        if len(face_objs)==0 :
            return status, "",error2
        elif len(face_objs)>=2 :
            return status, "",error3
        # try:
        # current_directory = os.getcwd()
        # parentpath=os.path.abspath(os.path.join(current_directory, os.pardir))
        # dbfullpath=os.path.join(parentpath, dataset)

        # dbfullpath=os.path.join(current_directory, dataset)
        # dbfullpath=f"{dbfullpath}/{devicename}"
        dbfullpath=fileoperation.getdevicepath(devicename)
        print("getdevicepath11====",dbfullpath)
        util.printcurrenttime("1.001")
        # print("face_objs====",face_objs)
        finder=Face.find(img_path=img_path1, db_path=dbfullpath,silent=True,refresh_database=refresh_database,distance_metric="euclidean_l2",source_objs=face_objs,threshold=1.0)
        util.printcurrenttime("1.002")
        # except:
            # finder
        print("finder1====",finder)    

        status,name,recordname=fileoperation.getfilenamebypath(finder)
        print(f"{status}{name}{recordname}")
        # status,name,parentdirname
        # DeepFace.stream(db_path = db_path1)
        return status,name,recordname

def recordcreate(devicename,recordname,filetemppathname,orgfilename):
    status="failed"
    error2="Human face not available.Please confirm that the image is a face photo"
    error3="More than 1 human face available.kindly upload one human face image file"
    name=""
    face_objs=[]
    try:
            face_objs = Face.extract_faces(img_path =filetemppathname)
    except:
            face_objs=[]
            # print("Total face=0")

    print("Total face=",len(face_objs))
    logger.info(f"Total face=={len(face_objs)}")
    if len(face_objs)==0 :
            fileoperation.removefile(filetemppathname)
            return status, error2
    elif len(face_objs)>=2 :
            fileoperation.removefile(filetemppathname)
            return status, error3
    # current_directory = os.getcwd()
    # parentpath=os.path.abspath(os.path.join(current_directory, os.pardir))
    # dbfullpath=os.path.join(parentpath, dataset)
    # dbfullpath=f"{dbfullpath}/{devicename}/{recordname}"
    # print("dbfullpath=",dbfullpath)

    # fileoperation.createdir(dbfullpath)

    dbfullpath=fileoperation.getrecordpath(devicename,recordname,True)
    targetpath=f"{dbfullpath}/{orgfilename}"
    print("targetpath=",targetpath)
    fileoperation.movefile(filetemppathname,targetpath)
    
    status, id,recoredname=finderoneface(devicename,targetpath,refresh_database=True)
    print("id=",id)
    print("status=",status)


    return status, id

    
def recorddelete(devicename,recordname):
    status="success"
    id=recordname
    recordfullpath=fileoperation.getrecordpath(devicename,recordname)
    # recordfullpath=f"{dbfullpath}/{devicename}/{recordname}"
    fileoperation.deletedir(recordfullpath)

    return status, id