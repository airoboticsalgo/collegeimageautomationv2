from flask import Flask,flash, request, redirect, url_for
from flask import request
from lib.face.service import fileoperation
from lib.face.service import faceoperation
import os
app = Flask(__name__)
from lib.logservice import logger as log

logger = log.get_singletonish_logger()
# db="E:/python_workspace/face_deepface1/dataset551"   
dataset="collegefacedatabase"
@app.route("/faceapi/record/validation", methods=['PUT'])
def record_validation():
     logger.info("/faceapi/record/validation================================================================ start") 
     devicename = request.args.get('devicename')
     
     logger.info(f"api={request.url}") 
     devicedb=fileoperation.getdevicepath(devicename)
     print("devicenamepathname=",devicedb)
     
#      devicedb=os.getcwd()
#      devicedb=f"{devicedb}/{dataset}/{devicename}/"
    #    if not os.path.exists(final_directory):
#      print("devicedb=",devicedb)
     
#      print("devicename1=",os.path.exists(devicedb))
     id=""
     status="failed"
     
     if devicename=="" or devicename==" " or devicename==None:
          status="failed:kindly provide the devicename in param"
     elif os.path.exists(devicedb)==False:
           status="failed:device not available"
     else:
        status,filename=fileoperation.dosave(request)
    
        print(f"{filename}==temp file save status:",status)

        status, id=faceoperation.finderoneface(devicename,filename)
        print("id=",id)
        print("status=",status)
        fileoperation.removefile(filename)
      #   if os.path.exists(filename): os.remove(filename)
     reponse = {
            "id": id,
             "status": status
                }
     logger.info(f"response==={reponse}") 
     logger.info("/faceapi/record/validation================================================================ end") 

     return reponse
@app.route("/faceapi/record/create", methods=['POST'])
def record_create():
    logger.info("/faceapi/record/create================================================================ start") 
    logger.info(f"api={request.url}")
    devicename = request.args.get('devicename')
    recordname = request.args.get('recordname')
    # devicename = request.args.get('devicename')
    print("devicenamepathname=",fileoperation.getdevicepath(devicename))
    id=""
    status="failed"
    filename=""
    orgfilename=""

     
    if devicename=="" or devicename==" " or devicename==None:
          status="failed:kindly provide the devicename in param"
    elif recordname=="" or recordname==" " or recordname==None:
          status="failed:kindly provide the recordname in param"
    else:         
        status,filetemppath,orgfilename=fileoperation.dosavetemp(request)

        logger.info(f"filesaved status={status}")
        logger.info(f"filesaved filetemppath={filetemppath}")
        logger.info(f"filesaved orgfilename={orgfilename}")
        print("status=",status)
        print("filename=",filetemppath)
        print("orgfilename=",orgfilename)
        status, id= faceoperation.recordcreate(devicename,recordname,filetemppath,orgfilename)
    reponse = {
            "id": id,
             "status": status
                }
    logger.info(f"reponse==={reponse}") 
    logger.info("/faceapi/record/create================================================================ end") 
    return reponse
@app.route("/faceapi/record/delete", methods=['DELETE'])
def record_delete():
    logger.info("/faceapi/record/delete================================================================ start")
    logger.info(f"api={request.url}") 
    devicename = request.args.get('devicename')
    recordname = request.args.get('recordname')
    # devicename = request.args.get('devicename')
    print("devicename1=",os.path.exists(devicename))
    id=""
    status="failed"
    filename=""
    orgfilename=""

     
    if devicename=="" or devicename==" " or devicename==None:
          status="failed:kindly provide the devicename in param"
    elif recordname=="" or recordname==" " or recordname==None:
          status="failed:kindly provide the recordname in param"
    else:         
          status, id= faceoperation.recorddelete(devicename,recordname)

     
    reponse = {
            "id": id,
             "status": status
                }
    logger.info(f"reponse==={reponse}") 
    logger.info("/faceapi/record/delete================================================================ end") 
    return reponse


if __name__ == '__main__':
    devicename="common"
    # run() method of Flask class runs the application 
    # on the local development server.
    # app.run()
    imgpath="E:/python_workspace/college_face_automation1/college_face_automation/temp/1.jpg"
    # db="E:/python_workspace/face_deepface1/dataset551"

    status, name=faceoperation.finderoneface(devicename,imgpath)
    print("name=",name)
    print("status=",status)
    # # finder = service.find(img1_path=imgpath, db=db, model_name="VGG-Face",
    #                       detector_backend="opencv",distance_metric="cosine",
    #                       align=True,enforce_detection=True,anti_spoofing=False)


 
    # print("finder len=",len(finder))
    
    # print("finder =",finder[0])
    # afinder=numpy.asarray(finder[0])
    # print("afinder12=",str(afinder[0]))
    # out_arr = numpy.char.split(str(afinder[0])," ") 
    # print("out_arr=",out_arr)
    # final=str(out_arr.item(0)).split(", """)
    # print("out_arr1=",final[0])
    # print("out_arr1=",final)
    # array1=str(afinder[0])
    # array2=array1.split(" ")
    # print("ss=",array2[0])
    # basefilename = Path(array2[0]).stem
    # print("basefilename=",basefilename)

# createdir(temp)