import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super(SimpleBrowser, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Simple Browser')
    window = SimpleBrowser()
    app.exec_()
