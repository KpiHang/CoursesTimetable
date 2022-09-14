import datetime
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import analyseCInfo_test
import utilities


class CourseTimetable(QMainWindow):
    def __init__(self):
        super(CourseTimetable, self).__init__()
        # test
        self.couresTableFlag = {}
        # test
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Course")
        # self.resize(560,950)
        self.resize(900,700)

        '''布局'''
        widget = QWidget()
        grid = QGridLayout()

        '''头部'''
        name = QLabel('课程表')
        name.setStyleSheet('font-size:25px;')
        grid.addWidget(name,0,0,1,2)


        week = QPushButton(f"{ datetime.date.today() }  第{ utilities.getWeekN() }周")
        week.setIcon(QIcon('icons/week.ico'))
        grid.addWidget(week,0,5,1,2)

        more = QPushButton()
        more.setIcon(QIcon('icons/more.ico'))
        grid.addWidget(more,0,7,1,1)


        '''课表框架'''
        label1 = QLabel('节次/时间')
        label1.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet('background-color:Gainsboro;')
        grid.addWidget(label1, 1, 0, 1, 1)

        label2 = QLabel('星期一')
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet('background-color:Gainsboro;')
        grid.addWidget(label2, 1, 1, 1, 1)

        label3 = QLabel('星期二')
        label3.setAlignment(Qt.AlignCenter)
        label3.setStyleSheet('background-color:Gainsboro;')
        grid.addWidget(label3, 1, 2, 1, 1)

        label4 = QLabel('星期三')
        label4.setAlignment(Qt.AlignCenter)
        label4.setStyleSheet('background-color:Gainsboro;')
        grid.addWidget(label4, 1, 3, 1, 1)

        label5 = QLabel('星期四')
        label5.setAlignment(Qt.AlignCenter)
        label5.setStyleSheet('background-color:Gainsboro;')
        grid.addWidget(label5, 1, 4, 1, 1)

        label6 = QLabel('星期五')
        label6.setAlignment(Qt.AlignCenter)
        label6.setStyleSheet('background-color:Gainsboro;')
        grid.addWidget(label6, 1, 5, 1, 1)

        label7 = QLabel('星期六')
        label7.setAlignment(Qt.AlignCenter)
        label7.setStyleSheet('background-color:Gainsboro;')
        grid.addWidget(label7, 1, 6, 1, 1)

        label8 = QLabel('星期日')
        label8.setAlignment(Qt.AlignCenter)
        label8.setStyleSheet('background-color:Gainsboro;')
        grid.addWidget(label8, 1, 7, 1, 1)

        label_12 = QLabel()
        label_12.setText(
            "<font style = 'font-size:15px;font-weight: bold;text-align:center;'>第一节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>08:00 ~ 08:45</font>"
            "<br/>""<br/>"
            "<font style = 'font-size:15px;font-weight: bold;'>第二节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>08:55 ~ 09:40</font>"
        )
        label_12.setAlignment(Qt.AlignCenter)
        label_12.setStyleSheet('background-color:	LightGreen;')
        grid.addWidget(label_12,2,0,4,1)

        label_34 = QLabel()
        label_34.setText(
            "<font style = 'font-size:15px;font-weight: bold;'>第三节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>10:10 ~ 10:55</font>"
            "<br/>""<br/>"
            "<font style = 'font-size:15px;font-weight: bold;'>第四节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>11:05 ~ 11:50</font>"
        )
        label_34.setAlignment(Qt.AlignCenter)
        label_34.setStyleSheet('background-color:	MediumOrchid;')
        grid.addWidget(label_34, 6,0,4,1)

        label_56 = QLabel()
        label_56.setText(
            "<font style = 'font-size:15px;font-weight: bold;'>第五节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>14:00 ~ 14:45</font>"
            "<br/>""<br/>"
            "<font style = 'font-size:15px;font-weight: bold;'>第六节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>14:55 ~ 15:40</font>"
        )
        label_56.setAlignment(Qt.AlignCenter)
        label_56.setStyleSheet('background-color:	LightGreen;')
        grid.addWidget(label_56, 10, 0, 4, 1)

        label_78 = QLabel('')
        label_78.setText(
            "<font style = 'font-size:15px;font-weight: bold;'>第七节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>16:00 ~ 16:45</font>"
            "<br/>""<br/>"
            "<font style = 'font-size:15px;font-weight: bold;'>第八节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>16:55 ~ 17:40</font>"
        )
        label_78.setAlignment(Qt.AlignCenter)
        label_78.setStyleSheet('background-color:	MediumOrchid;')
        grid.addWidget(label_78, 14, 0, 4, 1)

        label_9 = QLabel('')
        label_9.setText(
            "<font style = 'font-size:15px;font-weight: bold;'>第九节</font>"
            "<br/>""<br/>"
            "<font style = 'font-size:13px;'>19:00 ~ 19:45</font>"
            "<br/>""<br/>"
            "<font style = 'font-size:15px;font-weight: bold;'>第十节</font>"
            "<br/>" "<br/>"
            "<font style = 'font-size:13px;'>19:55 ~ 20:40</font>"
            "<br/>""<br/>"
        )
        label_9.setAlignment(Qt.AlignCenter)
        label_9.setStyleSheet('background-color:LightSteelBlue;')
        grid.addWidget(label_9, 18, 0, 5, 1)


        '''课表内容'''

        '''星期一'''
        # Monday_12 = QTextEdit('')
        # Monday_12.setStyleSheet('font-size:16px;')
        # grid.addWidget(Monday_12, 2, 1, 4, 1)
        Week1_12 = QTextEdit('')
        self.couresTableFlag["Week1_12"] = Week1_12
        grid.addWidget(Week1_12, 2, 1, 4, 1)

        Week1_34 = QTextEdit('')
        self.couresTableFlag["Week1_34"] = Week1_34
        grid.addWidget(Week1_34,6,1,4,1)

        Week1_56 = QTextEdit('')
        self.couresTableFlag["Week1_56"] = Week1_56
        grid.addWidget(Week1_56, 10, 1, 4, 1)

        Week1_78 = QTextEdit('')
        self.couresTableFlag["Week1_78"] = Week1_78
        grid.addWidget(Week1_78, 14, 1, 4, 1)

        Week1_910 = QTextEdit('')
        self.couresTableFlag["Week1_910"] = Week1_910
        grid.addWidget(Week1_910, 18, 1, 5, 1)


        '''星期二'''
        Week2_12 = QTextEdit('')
        self.couresTableFlag["Week2_12"] = Week2_12
        grid.addWidget(Week2_12, 2, 2, 4, 1)

        Week2_34 = QTextEdit('')
        self.couresTableFlag["Week2_34"] = Week2_34
        grid.addWidget(Week2_34, 6, 2, 4, 1)

        Week2_56 = QTextEdit('')
        self.couresTableFlag["Week2_56"] = Week2_56
        grid.addWidget(Week2_56, 10, 2, 4, 1)

        Week2_78 = QTextEdit('')
        self.couresTableFlag["Week2_78"] = Week2_78
        grid.addWidget(Week2_78, 14, 2, 4, 1)

        Week2_910 = QTextEdit('')
        self.couresTableFlag["Week2_910"] = Week2_910
        grid.addWidget(Week2_910, 18, 2, 5, 1)


        '''星期三'''
        Week3_12 = QTextEdit('')
        self.couresTableFlag["Week3_12"] = Week3_12
        grid.addWidget(Week3_12, 2, 3, 4, 1)

        Week3_34 = QTextEdit('')
        self.couresTableFlag["Week3_34"] = Week3_34
        grid.addWidget(Week3_34, 6, 3, 4, 1)

        Week3_56 = QTextEdit('')
        self.couresTableFlag["Week3_56"] = Week3_56
        grid.addWidget(Week3_56, 10, 3, 4, 1)

        Week3_78 = QTextEdit('')
        self.couresTableFlag["Week3_78"] = Week3_78
        grid.addWidget(Week3_78, 14, 3, 4, 1)

        Week3_910 = QTextEdit('')
        self.couresTableFlag["Week3_910"] = Week3_910
        grid.addWidget(Week3_910, 18, 3, 5, 1)



        '''星期四'''
        Week4_12 = QTextEdit('')
        self.couresTableFlag["Week4_12"] = Week4_12
        grid.addWidget(Week4_12, 2, 4, 4, 1)

        Week4_34 = QTextEdit('')
        self.couresTableFlag["Week4_34"] = Week4_34
        grid.addWidget(Week4_34, 6, 4, 4, 1)

        Week4_56 = QTextEdit('')
        self.couresTableFlag["Week4_56"] = Week4_56
        grid.addWidget(Week4_56, 10, 4, 4, 1)

        Week4_78 = QTextEdit('')
        self.couresTableFlag["Week4_78"] = Week4_78
        grid.addWidget(Week4_78, 14, 4, 4, 1)

        Week4_910 = QTextEdit('')
        self.couresTableFlag["Week4_910"] = Week4_910
        grid.addWidget(Week4_910, 18, 4, 5, 1)

        '''星期五'''
        Week5_12 = QTextEdit('')
        self.couresTableFlag["Week5_12"] = Week5_12
        grid.addWidget(Week5_12, 2, 5, 4, 1)

        Week5_34 = QTextEdit('')
        self.couresTableFlag["Week5_34"] = Week5_34
        grid.addWidget(Week5_34, 6, 5, 4, 1)

        Week5_56 = QTextEdit('')
        self.couresTableFlag["Week5_56"] = Week5_56
        grid.addWidget(Week5_56, 10, 5, 4, 1)

        Week5_78 = QTextEdit('')
        self.couresTableFlag["Week5_78"] = Week5_78
        grid.addWidget(Week5_78, 14, 5, 4, 1)

        Week5_910 = QTextEdit('')
        self.couresTableFlag["Week5_910"] = Week5_910
        grid.addWidget(Week5_910, 18, 5, 5, 1)


        '''星期六'''
        Week6_12 = QTextEdit('')
        self.couresTableFlag["Week6_12"] = Week6_12
        grid.addWidget(Week6_12, 2, 6, 4, 1)

        Week6_34 = QTextEdit('')
        self.couresTableFlag["Week6_34"] = Week6_34
        grid.addWidget(Week6_34, 6, 6, 4, 1)

        Week6_56 = QTextEdit('')
        self.couresTableFlag["Week6_56"] = Week6_56
        grid.addWidget(Week6_56, 10, 6, 4, 1)

        Week6_78 = QTextEdit('')
        self.couresTableFlag["Week6_78"] = Week6_78
        grid.addWidget(Week6_78, 14, 6, 4, 1)

        Week6_910 = QTextEdit('')
        self.couresTableFlag["Week6_910"] = Week6_910
        grid.addWidget(Week6_910, 18, 6, 5, 1)


        '''星期日'''
        Week7_12 = QTextEdit('')
        self.couresTableFlag["Week7_12"] = Week7_12
        grid.addWidget(Week7_12, 2, 7, 4, 1)

        Week7_34 = QTextEdit('')
        self.couresTableFlag["Week7_34"] = Week7_34
        grid.addWidget(Week7_34, 6, 7, 4, 1)

        Week7_56 = QTextEdit('')
        self.couresTableFlag["Week7_56"] = Week7_56
        grid.addWidget(Week7_56, 10, 7, 4, 1)

        Week7_78 = QTextEdit('')
        self.couresTableFlag["Week7_78"] = Week7_78
        grid.addWidget(Week7_78, 14, 7, 4, 1)

        Week7_910 = QTextEdit('')
        self.couresTableFlag["Week7_910"] = Week7_910
        grid.addWidget(Week7_910, 18, 7, 5, 1)


        widget.setLayout(grid)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
                            QPushButton{background-color: #f0f0f0;}
                            QPushButton:hover{background-color: #f0f0f0;}
                            QPushButton:pressed{background-color: #f0f0f0;}
                        ''')
    main_wnd = CourseTimetable()

    # # test
    # main_wnd.couresTableFlag["Week1_12"].setText(
    #     "<font style = 'font-size:15px;font-weight: bold;'>分布式计算</font>"
    #     "<br/>"
    #     "<font style = 'font-size:13px;'>(老师姓名 北区302教师)</font>"
    #     "<br/>""<br/>"
    #     "<font style = 'font-size:10px;'>单双周；第1-2节</font>"
    #     "<br/>"
    #     "<font style = 'font-size:10px;'>100000000</font>"
    #     "<br/>"
    # )
    # main_wnd.couresTableFlag["Week1_12"].setAlignment(Qt.AlignCenter)
    # # test

    coursesInfos = analyseCInfo_test.analyseCinfo()
    for flag in coursesInfos:
        if len(coursesInfos[flag]) == 1:
            course_info_dict = coursesInfos[flag][0]

            text = f'''
                <font style = 'font-size:15px;font-weight: bold;'>{ "《"+ course_info_dict['kcmc'] + "》" }</font>
                <br/>
                <font style = 'font-size:13px;'>{(course_info_dict['rkjsmc'] + course_info_dict['classroomNo'])}</font>
                <br/>
                <font style = 'font-size:10px;'>{course_info_dict['skzlxmc'] + "，" + str(course_info_dict['ksz']) + "~" +str(course_info_dict['jsz']) + "周" }</font>
                <br/>
                <font style = 'font-size:10px;'>{course_info_dict['kcbm']}</font>
                <br/>
            '''
            main_wnd.couresTableFlag[flag].setText(text)
        else:
            course_info_dict1 = coursesInfos[flag][0]
            course_info_dict2 = coursesInfos[flag][1]
            text = f'''
                <font style = 'font-size:10px;font-weight: bold;'>{ "1."+ course_info_dict1['kcmc']  }</font>
                <br/>
                <font style = 'font-size:10px;'>{(course_info_dict1['rkjsmc'] + course_info_dict1['classroomNo'])}</font>
                <br/> 
                <font style = 'font-size:10px;'>{course_info_dict1['skzlxmc'] + "，" + str(course_info_dict1['ksz']) + "~" +str(course_info_dict1['jsz']) + "周" }</font>
                <br/>
                <font style = 'font-size:10px;font-weight: bold;'>{ "2."+ course_info_dict2['kcmc'] }</font>
                <br/>
                <font style = 'font-size:10px;'>{(course_info_dict2['rkjsmc'] + course_info_dict2['classroomNo'])}</font>
                <br/>
                <font style = 'font-size:10px;'>{course_info_dict1['skzlxmc'] + "，" + str(course_info_dict1['ksz']) + "~" +str(course_info_dict1['jsz']) + "周" }</font>
            '''
            main_wnd.couresTableFlag[flag].setText(text)
        main_wnd.couresTableFlag[flag].setStyleSheet('background-color:LavenderBlush;')
        # 隐藏竖直滚动条；
        main_wnd.couresTableFlag[flag].setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_wnd.couresTableFlag[flag].setAlignment(Qt.AlignCenter)
    main_wnd.show()
    app.exec()