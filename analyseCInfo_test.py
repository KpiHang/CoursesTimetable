import json

def analyseCinfo():
    with open("coursesInfo.json", "r", encoding="utf-8") as f:
        info_json = json.load(f)
    courses_infos = info_json["data"]["courseList"]

    # print(courses_infos)

    coursesInfos = {}
    # 从这往下有大问题，但却能正常工作，暂时不动；
    for courseInfo in courses_infos:
        for key, values in courseInfo.items():
            # 网课不在课表上体现
            if key == "weeknull": continue
            # 两门课在一起，不同周上但在同一个位置；value中可能有两个；
            if len(values) < 2:
                # print(values)
                value = values[0]
                final = []
                if value['jskj']-value['kskj'] == 1:
                    flag_key = "Week"+value['skz']+"_"+str(value['kskj'])+str(value['jskj'])
                    final.append(value)
                    coursesInfos[flag_key] = final
                else:
                    mid_kj = value['kskj'] + 1
                    flag_key1 = "Week"+value['skz']+"_"+str(value['kskj'])+str(mid_kj)
                    flag_key2 = "Week"+value['skz']+"_"+str(mid_kj+1)+str(value['jskj'])
                    final.append(value)
                    coursesInfos[flag_key1] = final
                    coursesInfos[flag_key2] = final

            else:
                final = []
                for value in values:
                    # print(value)
                    if value['jskj'] - value['kskj'] == 1:
                        flag_key = "Week" + value['skz'] + "_" + str(value['kskj']) + str(value['jskj'])
                        final.append(value)
                        coursesInfos[flag_key] = final
                    else:
                        mid_kj = value['kskj'] + 1
                        flag_key1 = "Week" + value['skz'] + "_" + str(value['kskj']) + str(mid_kj)
                        flag_key2 = "Week" + value['skz'] + "_" + str(mid_kj + 1) + str(value['jskj'])
                        final.append(value)
                        coursesInfos[flag_key1] = final
                        coursesInfos[flag_key2] = final
    # print(coursesInfos["Week7_78"])
    return coursesInfos