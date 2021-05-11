import os
class TransferData():
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
        
def main()
    access_token = ''
    transferData = TransferData(access_token)
    file_from = input("write the file name")
    file_to = input("write the file path")

    