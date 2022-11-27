from fastapi import FastAPI 
from pydantic import BaseModel 
from typing import Optional
import easyocr
import sys
import re
import os
from fastapi import FastAPI, File, UploadFile, Form
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory


app = FastAPI()
@app.get("/")
def read_root():
    return {"Name": "ANISH",
            "What You Can do here": "TEST OCR"
    }
    
@app.post("/predict")

def predict(my_file: UploadFile = File(...)):
    print(os.getcwd() + "\\Tenjin_captcha\\" + my_file.filename) 
    filePath = os.getcwd() + "\\Tenjin_captcha\\" + my_file.filename
    result = reader.readtext(filePath)
    new_ls=[]
    new_ls=re.split("\'",str(result))
    s1=str(new_ls[2])
    s2=(s1[slice(2,7)])
    if float(s2) > 0.9:
        return {
            "RESULT": new_ls[1],
            "CONFIDENCE": s2,
            "SURITY": "HIGH"
            }
    else:
        return {
            "RESULT": new_ls[1],
            "CONFIDENCE": s2,
            "SURITY": "LOW"
            }

