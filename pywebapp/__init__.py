from io import BytesIO
from requests import get
from glob import glob
from os import getcwd,remove
from zipfile import ZipFile
import sys,os
from os import system




def errors(args):
    with open("error.log","a") as er:
        er.write("\n"+str(args))



def LoadFrontEnd():
    print("Front End components Loading...")
    components_url = "https://github.com/twbs/bootstrap/archive/v4.3.1.zip"
    parse_zip = get(components_url)
    file_name = parse_zip.headers['content-disposition'].split("filename=")[1]
    with open(file_name,"wb") as writer:
        writer.write(parse_zip.content)
        ZipFile(file_name,"r").extractall(getcwd())

    remove(str(getcwd())+'\\'+file_name)
    print("done")

####### Template creator functions ######
def Template():
    fileargs = sys.argv
    txt = ""
    for i in fileargs[1:]:
        if ".html" in i:
            try:
                os.makedirs("Templates")
            except Exception as e:
                errors(e)
            with open("Templates/"+i,"w+") as writer:
                writer.write("HTML code here")
        elif ".css" in i:
            try:
                os.makedirs("static/css")
            except Exception as e:
                errors(e)
            with open("static/css/"+i,"w+") as r:
                r.write('body {font-family: "Lato", sans-serif}')
        elif ".js" in i:
            try:
                os.makedirs("static/js")
            except Exception as e:
                errors(e)
            with open("static/js/"+i,"w+") as r:
                pass
        else:
            print("you have enter wrong keywords :(")
        





