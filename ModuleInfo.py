import requests
import json

ALL_DATA  = {}

MODINFO = requests.get("https://api.nusmods.com/v2/2022-2023/moduleInfo.json")
MODINFO = MODINFO.json()

def search_modinfo(moduleCode):
    output = ""
    for MOD in MODINFO:
        if MOD["moduleCode"] == moduleCode:
            output = output + "<b>Module Code: </b>" + MOD["moduleCode"] + "\n"
            output = output + "<b>Title: </b>" + MOD["title"] + "\n"
            output = output + "<b>Faculty: </b>" + MOD["faculty"] + "\n"
            output = output + "<b>Department: </b>" + MOD["department"] + "\n\n"
            output = output + "<b>Module Credit: </b>" + MOD["moduleCredit"] + "\n"

            try:
                output = output + "<b>Prerequisite: </b>" + MOD["prerequisite"] + "\n"
            except KeyError:
                output = output + "<b>Prerequisite: </b>None\n"
            
            try:
                output = output + "<b>Preclusion: </b>" + MOD["preclusion"] + "\n"
            except KeyError:
                output = output + "<b>Preclusion: </b>None\n"

            try:
                output = output + "<b>Corequisite: </b>" + MOD["corequisite"] + "\n\n"
            except KeyError:
                output = output + "<b>Corequisite: </b>None\n\n"

            output = output + "<b>Workload: </b>\n - " + str(MOD["workload"][0]) + "h in lectures\n - " + str(MOD["workload"][1]) + "h in tutorials\n - " + str(MOD["workload"][2]) + "h at the lab\n - " + str(MOD["workload"][3]) + "h doing project work\n - " + str(MOD["workload"][4]) + "h preparing for classes\n\n"

            output = output + "<b>Description: </b>" + MOD["description"] + "\n\n"

            output = output + "This information is generated from <a href='https://nusmods.com'>NUSMods</a>. For more details, please go to https://nusmods.com/modules/" + moduleCode + "/"
    return output
