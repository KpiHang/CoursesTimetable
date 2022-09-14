import json

def analyseCinfo():
    with open("coursesInfo.json", "r", encoding="utf-8") as f:
        info_json = json.load(f)
    courses_infos = info_json["data"]["courseList"]

    # print(courses_infos)

    coursesInfos = {}
    for courseInfo in courses_infos:
        for key, value in courseInfo.items():
            value = value[0]
            if key == "weeknull":
                # 网课不在课表上体现
                continue
            if value['jskj']-value['kskj'] == 1:
                flag_key = "Week"+value['skz']+"_"+str(value['kskj'])+str(value['jskj'])
                coursesInfos[flag_key] = value
            else:
                mid_kj = value['kskj'] + 1
                flag_key1 = "Week"+value['skz']+"_"+str(value['kskj'])+str(mid_kj)
                flag_key2 = "Week"+value['skz']+"_"+str(mid_kj+1)+str(value['jskj'])
                coursesInfos[flag_key1] = value
                coursesInfos[flag_key2] = value
    return coursesInfos