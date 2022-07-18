import requests
import json

ALL_DATA  = {}

MODINFO = requests.get("https://api.nusmods.com/v2/2022-2023/moduleInfo.json")
MODINFO = MODINFO.json()

def search_modinfo(moduleCode):
    output = ""
    for MOD in MODINFO:
        if MOD["moduleCode"] == moduleCode:
            output = output + "Module Code: " + MOD["moduleCode"] + "\n"
            output = output + "Title: " + MOD["title"] + "\n"
            output = output + "Faculty: " + MOD["faculty"] + "\n"
            output = output + "Department: " + MOD["department"] + "\n\n"
            output = output + "Module Credit: " + MOD["moduleCredit"] + "\n"
            #output = output + "Prerequisite: " + MOD["prerequisite"] + "\n"

            try:
                output = output + "Prerequisite: " + MOD["prerequisite"] + "\n"
            except KeyError:
                output = output + "Prerequisite: None\n"
            
            try:
                output = output + "Preclusion: " + MOD["preclusion"] + "\n"
            except KeyError:
                output = output + "Preclusion: None\n"

            try:
                output = output + "Corequisite: " + MOD["corequisite"] + "\n\n"
            except KeyError:
                output = output + "Corequisite: None\n\n"


            output = output + "Description: " + MOD["description"]
    return output

#print(search_modinfo("MA2001"))
