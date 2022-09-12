import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CourseTimetable(QMainWindow):
    def __init__(self):
        super(CourseTimetable, self).__init__()
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

        week = QPushButton('第一周')
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
        Monday_12 = QTextEdit('')
        Monday_12.setStyleSheet('font-size:16px;')
        grid.addWidget(Monday_12, 2, 1, 4, 1)

        Monday_34 = QTextEdit('')
        Monday_34.setStyleSheet('font-size:16px;')
        grid.addWidget(Monday_34,6,1,4,1)

        Monday_56 = QTextEdit('')
        Monday_56.setStyleSheet('font-size:16px;')
        grid.addWidget(Monday_56, 10, 1, 4, 1)

        Monday_78 = QTextEdit('')
        Monday_78.setStyleSheet('font-size:16px;')
        grid.addWidget(Monday_78, 14, 1, 4, 1)

        Monday_9 = QTextEdit('')
        Monday_9.setStyleSheet('font-size:16px;')
        grid.addWidget(Monday_9, 18, 1, 5, 1)


        '''星期二'''
        Tuesday_12 = QTextEdit('')
        Tuesday_12.setStyleSheet('font-size:16px;')
        grid.addWidget(Tuesday_12, 2, 2, 4, 1)

        Tuesday_34 = QTextEdit('')
        Tuesday_34.setStyleSheet('font-size:16px;')
        grid.addWidget(Tuesday_34, 6, 2, 4, 1)

        Tuesday_56 = QTextEdit('')
        Tuesday_56.setStyleSheet('font-size:16px;')
        grid.addWidget(Tuesday_56, 10, 2, 4, 1)

        Tuesday_78 = QTextEdit('')
        Tuesday_78.setStyleSheet('font-size:16px;')
        grid.addWidget(Tuesday_78, 14, 2, 4, 1)

        Tuesday_9 = QTextEdit('')
        Tuesday_9.setStyleSheet('font-size:16px;')
        grid.addWidget(Tuesday_9, 18, 2, 5, 1)


        '''星期三'''
        Wednesday_12 = QTextEdit('')
        Wednesday_12.setStyleSheet('font-size:16px;')
        grid.addWidget(Wednesday_12, 2, 3, 4, 1)

        Wednesday_34 = QTextEdit('')
        Wednesday_34.setStyleSheet('font-size:16px;')
        grid.addWidget(Wednesday_34, 6, 3, 4, 1)

        Wednesday_56 = QTextEdit('')
        Wednesday_56.setStyleSheet('font-size:16px;')
        grid.addWidget(Wednesday_56, 10, 3, 4, 1)

        Wednesday_78 = QTextEdit('')
        Wednesday_78.setStyleSheet('font-size:16px;')
        grid.addWidget(Wednesday_78, 14, 3, 4, 1)

        Wednesday_9 = QTextEdit('')
        Wednesday_9.setStyleSheet('font-size:16px;')
        grid.addWidget(Wednesday_9, 18, 3, 5, 1)


        '''星期四'''
        Thursday_12 = QTextEdit('')
        Thursday_12.setStyleSheet('font-size:16px;')
        grid.addWidget(Thursday_12, 2, 4, 4, 1)

        Thursday_34 = QTextEdit('')
        Thursday_34.setStyleSheet('font-size:16px;')
        grid.addWidget(Thursday_34, 6, 4, 4, 1)

        Thursday_56 = QTextEdit('')
        Thursday_56.setStyleSheet('font-size:16px;')
        grid.addWidget(Thursday_56, 10, 4, 4, 1)

        Thursday_78 = QTextEdit('')
        Thursday_78.setStyleSheet('font-size:16px;')
        grid.addWidget(Thursday_78, 14, 4, 4, 1)

        Thursday_9 = QTextEdit('')
        Thursday_9.setStyleSheet('font-size:16px;')
        grid.addWidget(Thursday_9, 18, 4, 5, 1)


        '''星期五'''
        Friday_12 = QTextEdit('')
        Friday_12.setStyleSheet('font-size:16px;')
        grid.addWidget(Friday_12, 2, 5, 4, 1)

        Friday_34 = QTextEdit('')
        Friday_34.setStyleSheet('font-size:16px;')
        grid.addWidget(Friday_34, 6, 5, 4, 1)

        Friday_56 = QTextEdit('')
        Friday_56.setStyleSheet('font-size:16px;')
        grid.addWidget(Friday_56, 10, 5, 4, 1)

        Friday_78 = QTextEdit('')
        Friday_78.setStyleSheet('font-size:16px;')
        grid.addWidget(Friday_78, 14, 5, 4, 1)

        Friday_9 = QTextEdit('')
        Friday_9.setStyleSheet('font-size:16px;')
        grid.addWidget(Friday_9, 18, 5, 5, 1)


        '''星期六'''
        Saturday_12 = QTextEdit('')
        Saturday_12.setStyleSheet('font-size:16px;')
        grid.addWidget(Saturday_12, 2, 6, 4, 1)

        Saturday_34 = QTextEdit('')
        Saturday_34.setStyleSheet('font-size:16px;')
        grid.addWidget(Saturday_34, 6, 6, 4, 1)

        Saturday_56 = QTextEdit('')
        Saturday_56.setStyleSheet('font-size:16px;')
        grid.addWidget(Saturday_56, 10, 6, 4, 1)

        Saturday_78 = QTextEdit('')
        Saturday_78.setStyleSheet('font-size:16px;')
        grid.addWidget(Saturday_78, 14, 6, 4, 1)

        Saturday_9 = QTextEdit('')
        Saturday_9.setStyleSheet('font-size:16px;')
        grid.addWidget(Saturday_9, 18, 6, 5, 1)


        '''星期日'''
        Sunday_12 = QTextEdit('')
        Sunday_12.setStyleSheet('font-size:16px;')
        grid.addWidget(Sunday_12, 2, 7, 4, 1)

        Sunday_34 = QTextEdit('')
        Sunday_34.setStyleSheet('font-size:16px;')
        grid.addWidget(Sunday_34, 6, 7, 4, 1)

        Sunday_56 = QTextEdit('')
        Sunday_56.setStyleSheet('font-size:16px;')
        grid.addWidget(Sunday_56, 10, 7, 4, 1)

        Sunday_78 = QTextEdit('')
        Sunday_78.setStyleSheet('font-size:16px;')
        grid.addWidget(Sunday_78, 14, 7, 4, 1)

        Sunday_9 = QTextEdit('')
        Sunday_9.setStyleSheet('font-size:16px;')
        grid.addWidget(Sunday_9, 18, 7, 5, 1)


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
    main_wnd.show()
    app.exec()