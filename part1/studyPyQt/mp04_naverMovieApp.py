import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverAPI import *
from urllib.request import urlopen
import webbrowser # 웹브라우저 모듈

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverApimovei.ui', self)
        self.setWindowIcon(QIcon('./studyPyQt/movie.png'))

        # 검색 버튼 클릭시그널 / 슬롯함수
        self.btnsearch.clicked.connect(self.btnSearchClicked)
        # 검색어 입력후 엔터를 치면 처리
        self.txtsearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    def tblResultDoubleClicked(self):
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text() # url 링크변경
        webbrowser.open(url) # 네이버 영화 웹사이트

    def txtSearchReturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.txtsearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '영화명을 입력하세요!')
            return
        else:
            api = NaverAPI() # NaverApi 클래스 객체 생성
            node = 'movie' # movie로 변경하면 영화검색
            outputs = [] # 결과 담을 리스트변수
            display = 100
            
            result = api.get_naver_search(node, search, 1, display)
            # 리스트뷰에 출력 기능
            items = result['items'] # json결과 중 items 아래 배열만 추출
            # print(result)
            self.makeTable(items) # 테이블 위젯에 데이터들을 할당함수

    # 테이블 위젯에 데이터 표시 -- 네이버 영화 결과 변경
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection) # 단일선택
        self.tblResult.setColumnCount(7)
        self.tblResult.setRowCount(len(items)) # 현재 100개의 행 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '개봉년도', '감독', '배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 100)
        self.tblResult.setColumnWidth(1, 70) # 개봉년도
        self.tblResult.setColumnWidth(4, 50) # 평점
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 데이터를 수정금지

        for i, post in enumerate(items): # 0, 영화 ...
            title = self.replaceHtmlTag(post['title']) 
            subtitle = post['subtitle']
            title = f'{title} ({subtitle})'
            pubDate = post['pubDate']
            director = post['director'].replace('|', ',')[:-1] # 마지막 변환된 쉼표 없애기
            actor = post['actor'].replace('|', ',')[:-1] # [:-1] 파이썬에서만 가능함

            userRating = post['userRating']
            link = post['link']
            img_url = post['image']

            #230308. 포스터 이미지 추가
            if img_url != '': # 빈값이면 포스터가 없음
                data = urlopen(img_url).read() # 2진데이터 - 네이버영화에 있는 이미지 다운, 텍스트형태데이터
                image = QImage() # 이미지 객체
                image.loadFromData(data)
                # QTableWidget 이미지를 그냥 넣을 수 없음. QLabel() 집어넣은뒤 QLabel -> QTableWidget
                imgLabel = QLabel()
                imgLabel.setPixmap(QPixmap(image))

                # data를 이미지로 저장가능
                # f = open(f'./studyPyQt/temp/image_{i+1}.png', mode='wb') # 파일쓰기
                # f.write(data)
                # f.close

            # setItem(행, 열, 넣을데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))
            # self.tblResult.setItem(i, 6, QTableWidgetItem(img_url))
            if img_url != '':
                self.tblResult.setCellWidget(i, 6, imgLabel)
                self.tblResult.setRowHeight(i, 110) # 포스터가 있으면 쉘 높이를 올림

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<') # lesser than 작다
        result = result.replace('&gt;', '>') # greater than 크다
        result = result.replace('<b>', '') # bold
        result = result.replace('</b>', '') # bold
        result = result.replace('&apos;', "'") # apostopy 홑따옴표
        result = result.replace('&quot;', '"') # quotation mark 쌍따옴표
        # 변환 안된 특수문자가 나타나면 여기 추가

        return result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())