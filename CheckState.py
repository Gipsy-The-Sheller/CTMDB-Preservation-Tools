import basicwebsolver
import wpsolver

import sys
#from PyQt5.QtWidgets import QApplication,QWidget

ls = wpsolver.ChkState()

def WriteStateCsv(ls):
    csv = open('result.csv','w')
    print('-'*len(ls),end = '\r')
    for i in range(len(ls)):
        csv.writelines(ls[i][0],',',ls[i][1],',',ls[i][2],',',ls[i][3])
        print('>',end = '')
    print ('\n')
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = QWidget()
    wnd.resize(300,150)
    wnd.move(300,300)
    wnd.setWindowTitle('TLT')
    wnd.show()
    sys.exit(app.exec_())
'''
#WriteStateCsv(ls)
