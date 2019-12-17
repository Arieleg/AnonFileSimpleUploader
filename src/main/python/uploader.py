import json

from PyQt5 import QtCore, QtNetwork
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QHttpMultiPart, QHttpPart, QNetworkRequest
from PyQt5.QtWidgets import QApplication


class Item:
    name = 0
    size = 1
    progress = 2
    short_link = 3
    full_link = 4
    uploading = 5
    finished = 6
    error = 7


class Uploader:
    max_parallel = 1

    def __init__(self, index, anon_file_uploader):
        self.anon_file_uploader = anon_file_uploader
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.finished)
        if self.anon_file_uploader.is_finished():
            QApplication.beep()
            self.anon_file_uploader.enable()
        else:
            self.index = index
            self.name = anon_file_uploader.ui.TableOfFiles.item(self.index, Item.name)
            self.size = anon_file_uploader.ui.TableOfFiles.item(self.index, Item.size)
            self.progress_bar = anon_file_uploader.progress_bar_list[self.index]
            self.short_link = anon_file_uploader.ui.TableOfFiles.item(self.index, Item.short_link)
            self.full_link = anon_file_uploader.ui.TableOfFiles.item(self.index, Item.full_link)
            self.uploading = anon_file_uploader.ui.TableOfFiles.item(self.index, Item.uploading)
            self.uploading.setText("True")
            self.item_finished = anon_file_uploader.ui.TableOfFiles.item(self.index, Item.finished)
            self.error = anon_file_uploader.ui.TableOfFiles.item(self.index, Item.error)
            self.upload()

    def upload(self):
        multi_part = QHttpMultiPart(QHttpMultiPart.FormDataType)
        file = QtCore.QFile(self.name.text())
        if not file.open(QtCore.QIODevice.ReadOnly):
            self.uploading.setText("False")
            error = "Error opening file"
            self.error.setText(error)
            self.short_link.setText(error)
            self.full_link.setText(error)
            next_index = self.anon_file_uploader.get_next_index()
            if next_index >= 0:
                self.__init__(next_index, self.anon_file_uploader)
        else:
            part = QHttpPart()
            part.setHeader(QNetworkRequest.ContentDispositionHeader,
                           "form-data; name=\"{}\"; filename=\"{}\"".format("file", file.fileName()))
            part.setBodyDevice(file)
            file.setParent(multi_part)
            multi_part.append(part)
            url = QUrl("https://api.anonfile.com/upload")
            request = QNetworkRequest(url)
            reply = self.manager.post(request, multi_part)
            reply.uploadProgress.connect(self.progress_bar_progress)

            multi_part.setParent(reply)

    def progress_bar_progress(self, bytes_sent, bytes_total):
        if bytes_total > 0:
            self.progress_bar.setValue(2147483647 * (bytes_sent / bytes_total))

    def finished(self, reply):
        self.item_finished.setText("True")
        try:
            if reply.error() == QtNetwork.QNetworkReply.NoError:
                json_reply = json.loads(reply.readAll().data())
                if json_reply["status"]:
                    link = json_reply["data"]["file"]["url"]
                    self.short_link.setText(link["short"])
                    self.full_link.setText((link["full"]))
                else:
                    error = json_reply["error"]
                    self.error.setText(error)
                    self.short_link.setText(error)
                    self.full_link.setText(error)
            else:
                json_reply = json.loads(reply.readAll().data())
                error = json_reply["error"]["message"]
                self.error.setText(error)
                self.short_link.setText(error)
                self.full_link.setText(error)
        except:
            error = "Error, invalid reply. Verify your Internet connection"
            self.error.setText(error)
            self.short_link.setText(error)
            self.full_link.setText(error)
        finally:
            reply.deleteLater()
            self.uploading.setText("False")
            if self.anon_file_uploader.is_finished():
                QApplication.beep()
                self.anon_file_uploader.enable()
            else:
                next_index = self.anon_file_uploader.get_next_index()
                if next_index >= 0:
                    self.__init__(next_index, self.anon_file_uploader)
