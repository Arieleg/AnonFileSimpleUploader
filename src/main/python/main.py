import configparser
import os
import sys
from multiprocessing import Lock

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot, QTranslator
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QProgressBar, QApplication, QAbstractItemView, \
    QDialog
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from ui.Ui_mainwindow import Ui_MainWindow
from ui.Ui_output_format import Ui_OutputFormat
from uploader import Item, Uploader


def size_of_file(size):
    if size < 1024 * 1024:
        return str(round(size, 2)) + " KB"
    elif size < 1024 * 1024 * 1024:
        return str(round(size / (1024 * 1024), 2)) + " MB"
    else:
        return str(round(size / (1024 * 1024 * 1024), 2)) + " GB"


class AnonFileSimpleUploader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.uploader = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # output format QDialog
        self.output_format_window = QDialog()
        self.output_format_window.setWindowFlags(
            self.output_format_window.windowFlags() & ~ QtCore.Qt.WindowContextHelpButtonHint)
        self.ui_output_format_window = Ui_OutputFormat()
        self.ui_output_format_window.setupUi(self.output_format_window)
        self.ui_output_format_window.pushButtonOk.clicked.connect(self.output_format_ok)
        self.ui_output_format_window.lineEditOutputFormat.returnPressed.connect(self.output_format_ok)

        # Warning translator
        self.translator_warning_qmessage = ":/Languages/Languages/main_warning_en.qm"

        # Config
        # Portable
        #self.config_folder_path = os.path.abspath(os.path.dirname(__file__))
        #self.config_file_path = self.config_folder_path + '/config.ini'

        # Installable
        #self.config_folder_path = str(os.getenv('APPDATA')) + '/AnonFileSimpleUploader'
        #self.config_file_path = self.config_folder_path + '/config.ini'



        self.output_format = "$short_link$"
        self.apply_conf_file()

        self.name_width = 360
        self.ui.TableOfFiles.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.TableOfFiles.setColumnWidth(Item.size, 60)
        self.ui.TableOfFiles.setColumnWidth(Item.name, self.name_width)
        self.ui.TableOfFiles.setColumnWidth(Item.short_link, 190)
        self.ui.TableOfFiles.setColumnWidth(Item.full_link, 380)
        self.ui.TableOfFiles.setColumnHidden(Item.uploading, True)
        self.ui.TableOfFiles.setColumnHidden(Item.error, True)
        self.ui.TableOfFiles.setColumnHidden(Item.finished, True)

        # Buttons
        self.ui.AddButton.clicked.connect(self.add)
        self.ui.RemoveButton.clicked.connect(self.remove)
        self.ui.UploadButton.clicked.connect(self.upload)
        self.ui.pushButtonUp.clicked.connect(self.up)
        self.ui.pushButtonDown.clicked.connect(self.down)
        self.ui.pushButtonCopyLinks.clicked.connect(self.copy_links)
        self.ui.pushButtonRetryAll.clicked.connect(self.retry_all)

        # Menu
        self.ui.actionShort_Link.toggled.connect(self.view_short_link)
        self.ui.actionFull_Link.toggled.connect(self.view_full_link)
        self.ui.actionOutput_format.triggered.connect(self.exec_output_format)
        self.ui.actionEnglish.triggered.connect(self.tr_english)
        self.ui.actionSpanish.triggered.connect(self.tr_spanish)

        self.lock = Lock()

        self.uploader_list = []
        self.progress_bar_list = []
        self.aux_add_flag = False
        self.parallel = 1
        self.index = 0

    @pyqtSlot(bool)
    def copy_links(self):
        clipboard = QGuiApplication.clipboard()
        text_to_clipboard = ""
        selected_items = self.ui.TableOfFiles.selectedItems()
        if len(selected_items) > 0:
            for item in selected_items:
                row = item.row()
                text = self.output_format.replace("$path$", self.ui.TableOfFiles.item(row, Item.name).text()) \
                    .replace("$size$", self.ui.TableOfFiles.item(row, Item.size).text()) \
                    .replace("$short_link$", self.ui.TableOfFiles.item(row, Item.short_link).text()) \
                    .replace("$full_link$", self.ui.TableOfFiles.item(row, Item.full_link).text()) \
                    .replace("$error$", self.ui.TableOfFiles.item(row, Item.error).text()) \
                    .replace("$name$", self.ui.TableOfFiles.item(row, Item.name).text().split("/")[-1])
                text_to_clipboard += text + "\n"
        else:
            for row in range(self.ui.TableOfFiles.rowCount()):
                text = self.output_format.replace("path", self.ui.TableOfFiles.item(row, Item.name).text()) \
                    .replace("$size$", self.ui.TableOfFiles.item(row, Item.size).text()) \
                    .replace("$short_link$", self.ui.TableOfFiles.item(row, Item.short_link).text()) \
                    .replace("$full_link$", self.ui.TableOfFiles.item(row, Item.full_link).text()) \
                    .replace("$error$", self.ui.TableOfFiles.item(row, Item.error).text()) \
                    .replace("$name$", self.ui.TableOfFiles.item(row, Item.name).text().split("/")[-1])
                text_to_clipboard += text + "\n"
        clipboard.setText(text_to_clipboard)

    @pyqtSlot(bool)
    def up(self):
        selected_items = self.ui.TableOfFiles.selectedItems()

        for item in selected_items:
            item.setSelected(False)
            row = item.row()
            if row > 0:
                self.swap(row, row - 1)
            else:
                break
        for item in selected_items:
            item.setSelected(True)

    @pyqtSlot(bool)
    def down(self):
        selected_items = self.ui.TableOfFiles.selectedItems()
        for i in range(len(selected_items) - 1, 0 - 1, -1):
            item = selected_items[i]
            item.setSelected(False)
            row = item.row()
            if row < self.ui.TableOfFiles.rowCount() - 1:
                self.swap(row, row + 1)
            else:
                break
        for item in selected_items:
            item.setSelected(True)

    def swap(self, i_src, i_dst):
        name_src = self.ui.TableOfFiles.takeItem(i_src, Item.name)
        size_src = self.ui.TableOfFiles.takeItem(i_src, Item.size)
        progress_src = self.ui.TableOfFiles.takeItem(i_src, Item.progress)
        short_link_src = self.ui.TableOfFiles.takeItem(i_src, Item.short_link)
        full_link_src = self.ui.TableOfFiles.takeItem(i_src, Item.full_link)
        uploading_src = self.ui.TableOfFiles.takeItem(i_src, Item.uploading)
        finished_src = self.ui.TableOfFiles.takeItem(i_src, Item.finished)
        error_src = self.ui.TableOfFiles.takeItem(i_src, Item.error)

        name_dst = self.ui.TableOfFiles.takeItem(i_dst, Item.name)
        size_dst = self.ui.TableOfFiles.takeItem(i_dst, Item.size)
        progress_dst = self.ui.TableOfFiles.takeItem(i_dst, Item.progress)
        short_link_dst = self.ui.TableOfFiles.takeItem(i_dst, Item.short_link)
        full_link_dst = self.ui.TableOfFiles.takeItem(i_dst, Item.full_link)
        upload_dst = self.ui.TableOfFiles.takeItem(i_dst, Item.uploading)
        finished_dst = self.ui.TableOfFiles.takeItem(i_dst, Item.finished)
        error_dst = self.ui.TableOfFiles.takeItem(i_dst, Item.error)

        self.ui.TableOfFiles.setItem(i_dst, Item.name, name_src)
        self.ui.TableOfFiles.setItem(i_dst, Item.size, size_src)
        self.ui.TableOfFiles.setItem(i_dst, Item.progress, progress_src)
        self.ui.TableOfFiles.setItem(i_dst, Item.short_link, short_link_src)
        self.ui.TableOfFiles.setItem(i_dst, Item.full_link, full_link_src)
        self.ui.TableOfFiles.setItem(i_dst, Item.uploading, uploading_src)
        self.ui.TableOfFiles.setItem(i_dst, Item.finished, finished_src)
        self.ui.TableOfFiles.setItem(i_dst, Item.error, error_src)

        self.ui.TableOfFiles.setItem(i_src, Item.name, name_dst)
        self.ui.TableOfFiles.setItem(i_src, Item.size, size_dst)
        self.ui.TableOfFiles.setItem(i_src, Item.progress, progress_dst)
        self.ui.TableOfFiles.setItem(i_src, Item.short_link, short_link_dst)
        self.ui.TableOfFiles.setItem(i_src, Item.full_link, full_link_dst)
        self.ui.TableOfFiles.setItem(i_src, Item.uploading, upload_dst)
        self.ui.TableOfFiles.setItem(i_src, Item.finished, finished_dst)
        self.ui.TableOfFiles.setItem(i_src, Item.error, error_dst)

    @pyqtSlot(bool)
    def add(self):
        files = QFileDialog.getOpenFileNames(self)
        for file in files[0]:
            if not len(self.ui.TableOfFiles.findItems(file, QtCore.Qt.MatchFixedString)) > 0:
                # Resize name width
                len_file = len(file) * 6
                if len_file > self.name_width:
                    self.name_width = len_file
                    self.ui.TableOfFiles.setColumnWidth(Item.name, self.name_width)

                row = self.ui.TableOfFiles.rowCount()
                # Name
                item_table = QtWidgets.QTableWidgetItem(file)
                item_table.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                item_table.setTextAlignment(QtCore.Qt.AlignLeft)
                self.ui.TableOfFiles.insertRow(self.ui.TableOfFiles.rowCount())
                self.ui.TableOfFiles.setItem(row, 0, item_table)

                # Size
                item_table = QtWidgets.QTableWidgetItem(size_of_file(QtCore.QFile(file).size()))
                item_table.setFlags(QtCore.Qt.ItemIsEnabled)
                item_table.setTextAlignment(QtCore.Qt.AlignLeft)
                self.ui.TableOfFiles.setItem(row, 1, item_table)

                # Progress Bar
                p_bar = QProgressBar()
                p_bar.setAlignment(QtCore.Qt.AlignHCenter)
                p_bar.setMaximum(2147483647)
                self.progress_bar_list.append(p_bar)
                self.ui.TableOfFiles.setCellWidget(row, 2, self.progress_bar_list[-1])

                # Short Link
                item_table = QtWidgets.QTableWidgetItem()
                item_table.setText("")
                item_table.setFlags(QtCore.Qt.ItemIsEnabled)
                item_table.setTextAlignment(QtCore.Qt.AlignLeft)
                self.ui.TableOfFiles.setItem(row, 3, item_table)

                # Full Link
                item_table = QtWidgets.QTableWidgetItem()
                item_table.setText("")
                item_table.setFlags(QtCore.Qt.ItemIsEnabled)
                item_table.setTextAlignment(QtCore.Qt.AlignLeft)
                self.ui.TableOfFiles.setItem(row, 4, item_table)

                # Uploading
                item_table = QtWidgets.QTableWidgetItem()
                item_table.setText("False")
                item_table.setFlags(QtCore.Qt.ItemIsEnabled)
                item_table.setTextAlignment(QtCore.Qt.AlignLeft)
                self.ui.TableOfFiles.setItem(row, 5, item_table)

                # Finished
                item_table = QtWidgets.QTableWidgetItem()
                item_table.setText("False")
                item_table.setFlags(QtCore.Qt.ItemIsEnabled)
                item_table.setTextAlignment(QtCore.Qt.AlignLeft)
                self.ui.TableOfFiles.setItem(row, 6, item_table)

                # Error
                item_table = QtWidgets.QTableWidgetItem()
                item_table.setText("False")
                item_table.setFlags(QtCore.Qt.ItemIsEnabled)
                item_table.setTextAlignment(QtCore.Qt.AlignLeft)
                self.ui.TableOfFiles.setItem(row, 7, item_table)
            else:
                self.aux_add_flag = True
        if self.aux_add_flag:
            self.aux_add_flag = False
            _translator = QTranslator()
            _translator.load(self.translator_warning_qmessage)
            msg = QMessageBox()
            msg.setWindowTitle(_translator.translate("MainWindow_Warning", "Warning"))
            msg.setText(_translator.translate("MainWindow_Warning", "Some file is already in the list."))
            msg.exec_()

    @pyqtSlot(bool)
    def remove(self):
        selected_items = self.ui.TableOfFiles.selectedItems()
        for item_table in selected_items:
            self.ui.TableOfFiles.removeRow(item_table.row())

    @pyqtSlot(bool)
    def upload(self):
        self.index = 0
        if self.is_finished():
            QApplication.beep()
            self.enable()
        else:
            self.uploader_list = []
            self.disable()
            max_parallel = self.ui.spinBoxMaxParallel.value() - 1
            len_item_list = self.ui.TableOfFiles.rowCount() - 1
            n_parallel = max_parallel if max_parallel <= len_item_list else len_item_list
            self.parallel = n_parallel + 1
            for i in range(self.parallel):
                index = self.get_next_index()
                if index >= 0:
                    self.uploader_list.append(Uploader(index, self))

    def get_next_index(self):
        self.lock.acquire()
        try:
            while self.index <= self.ui.TableOfFiles.rowCount() - 1:
                if not self.ui.TableOfFiles.item(self.index, Item.finished).text() == "True":
                    return self.index
                else:
                    self.index += 1
            return -1
        finally:
            self.index += 1
            self.lock.release()

    def is_finished(self):
        self.lock.acquire()
        try:
            for i in range(self.ui.TableOfFiles.rowCount()):
                if not self.ui.TableOfFiles.item(i, Item.finished).text() == "True":
                    return False
            return True
        finally:
            self.lock.release()

    def enable(self):
        self.ui.UploadButton.setEnabled(True)
        self.ui.AddButton.setEnabled(True)
        self.ui.RemoveButton.setEnabled(True)
        self.ui.TableOfFiles.setEnabled(True)
        self.ui.pushButtonUp.setEnabled(True)
        self.ui.pushButtonDown.setEnabled(True)
        self.ui.pushButtonCopyLinks.setEnabled(True)
        self.ui.spinBoxMaxParallel.setEnabled(True)
        self.ui.pushButtonRetryAll.setEnabled(True)

    def disable(self):
        self.ui.UploadButton.setEnabled(False)
        self.ui.AddButton.setEnabled(False)
        self.ui.RemoveButton.setEnabled(False)
        self.ui.TableOfFiles.setEnabled(False)
        self.ui.pushButtonUp.setEnabled(False)
        self.ui.pushButtonDown.setEnabled(False)
        self.ui.pushButtonCopyLinks.setEnabled(False)
        self.ui.spinBoxMaxParallel.setEnabled(False)
        self.ui.pushButtonRetryAll.setEnabled(False)

    @pyqtSlot(bool)
    def view_short_link(self, checked):
        self.ui.TableOfFiles.setColumnHidden(Item.short_link, not checked)
        config = configparser.ConfigParser()
        if config.read(self.config_file_path):
            if checked:
                config['View']['short_link'] = 'True'
            else:
                config['View']['short_link'] = 'False'
            with open(self.config_file_path, 'w') as config_file_path:
                config.write(config_file_path)

    @pyqtSlot(bool)
    def view_full_link(self, checked):
        self.ui.TableOfFiles.setColumnHidden(Item.full_link, not checked)
        config = configparser.ConfigParser()
        if config.read(self.config_file_path):
            if checked:
                config['View']['full_link'] = 'True'
            else:
                config['View']['full_link'] = 'False'
            with open(self.config_file_path, 'w') as config_file_path:
                config.write(config_file_path)

    @pyqtSlot()
    def exec_output_format(self):
        self.output_format_window.exec_()

    @pyqtSlot()
    def output_format_ok(self):
        config = configparser.ConfigParser()
        if config.read(self.config_file_path):
            output_format = self.ui_output_format_window.lineEditOutputFormat.text()
            if output_format is not "":
                self.output_format = output_format
                config['OutputFormat']['text_format'] = self.output_format
                with open(self.config_file_path, 'w') as config_file_path:
                    config.write(config_file_path)
        self.output_format_window.close()

    def tr_mainwindow(self, translator):
        QApplication.instance().installTranslator(translator)
        self.ui.retranslateUi(self)

    def tr_output_format(self, translator):
        QApplication.instance().installTranslator(translator)
        self.ui_output_format_window.retranslateUi(self.output_format_window)

    @pyqtSlot()
    def tr_spanish(self):
        # Change language of Warning: Some file is already in the list.
        self.translator_warning_qmessage = ":/Languages/Languages/main_warning_es.qm"
        # Translate MainWindow
        translator = QTranslator()
        translator.load(":/Languages/Languages/mainwindow_es.qm")
        self.tr_mainwindow(translator)
        # Translate OutputFormat
        translator.load(":/Languages/Languages/output_format_es.qm")
        self.tr_output_format(translator)
        # Save config.ini
        config = configparser.ConfigParser()
        if config.read(self.config_file_path):
            config['Languages'] = {'lang': 'es'}
            with open(self.config_file_path, 'w') as configfile:
                config.write(configfile)

    @pyqtSlot()
    def tr_english(self):
        # Change language of Warning: Some file is already in the list.
        self.translator_warning_qmessage = ":/Languages/Languages/main_warning_en.qm"
        # Translate MainWindow
        translator = QTranslator()
        translator.load(":/Languages/Languages/mainwindow_en.qm")
        self.tr_mainwindow(translator)
        # Translate OutputFormat
        translator.load(":/Languages/Languages/output_format_en.qm")
        self.tr_output_format(translator)
        # Save config.ini
        config = configparser.ConfigParser()
        if config.read(self.config_file_path):
            config['Languages'] = {'lang': 'en'}
            with open(self.config_file_path, 'w') as configfile:
                config.write(configfile)

    def apply_conf_file(self):
        config = configparser.ConfigParser()
        try:
            config.read(self.config_file_path)
            # Language
            if config['Languages']['lang'] == 'es':
                self.tr_spanish()

            # View
            if config['View']['short_link'] == 'False':
                self.ui.TableOfFiles.setColumnHidden(Item.short_link, True)
                self.ui.actionShort_Link.setChecked(False)
            else:
                self.ui.TableOfFiles.setColumnHidden(Item.short_link, False)
                self.ui.actionShort_Link.setChecked(True)

            if config['View']['full_link'] == 'False':
                self.ui.TableOfFiles.setColumnHidden(Item.full_link, True)
                self.ui.actionFull_Link.setChecked(False)
            else:
                self.ui.TableOfFiles.setColumnHidden(Item.full_link, False)
                self.ui.actionFull_Link.setChecked(True)

            # Output Format
            self.output_format = config['OutputFormat']['text_format']

        except:
            if not os.path.isdir(self.config_folder_path):
                os.makedirs(self.config_folder_path)

            config['View'] = {'short_link': 'True', 'full_link': 'False'}
            config['OutputFormat'] = {'text_format': "$short_link$"}
            config['Languages'] = {'lang': "en"}
            with open(self.config_file_path, 'w') as config_file_path:
                config.write(config_file_path)
            self.apply_conf_file()

    def retry_all(self):
        for row in range(self.ui.TableOfFiles.rowCount()):
            if self.ui.TableOfFiles.item(row, Item.error).text() != "False":
                self.ui.TableOfFiles.item(row, Item.short_link).setText("")
                self.ui.TableOfFiles.item(row, Item.full_link).setText("")
                self.ui.TableOfFiles.item(row, Item.uploading).setText("False")
                self.ui.TableOfFiles.item(row, Item.finished).setText("False")
                self.ui.TableOfFiles.item(row, Item.error).setText("False")


if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = AnonFileSimpleUploader()
    window.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
