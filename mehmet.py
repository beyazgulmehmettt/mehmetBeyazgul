# Fill in this file with the code from parsing JSON exercise
import json
dosya=open("myfile.json","r")
json_dosya=json.load(dosya)
print("Ad    : ",json_dosya["kimlik"]["ad"])
print("Soyad : ",json_dosya["kimlik"]["soyad"])
print("Kimlik: ",json_dosya["kimlik"])
