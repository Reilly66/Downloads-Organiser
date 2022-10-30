import os

EXTENSIONS = {"MICROSOFT_OFFICE": {"doc", "docx", "ppt", "pptx", "xls", "xlsx"},
              "IMAGES": {"png", "jpg", "jpeg", "gif"},
              "VIDEO_AND_AUDIO": {"mp3", "mp4", "wav"},
              "PDF": {"pdf"},
              "SCRIPTS_AND_EXECUTABLES": {"py", "java", "c", "cs", "cpp", "exe", "js", "json", "html", "css", "jar"},
              "OTHER": {None}}

DOWNLOADS_DIRECTORY = "C:\\Users\\Reilly\\Downloads"


def main():
    files = os.listdir(DOWNLOADS_DIRECTORY)
    folders = list(filter(lambda x: "." not in x, files))
    files = list(filter(lambda x: "." in x, files))
    for folder_name in EXTENSIONS:
        if folder_name not in folders:
            os.mkdir(os.path.join(DOWNLOADS_DIRECTORY, folder_name))
    for file_name in files:
        extension = file_name.split(".")[-1]
        for folder_name in EXTENSIONS:
            if extension in EXTENSIONS[folder_name]:
                os.rename(os.path.join(DOWNLOADS_DIRECTORY, file_name), os.path.join(os.path.join(DOWNLOADS_DIRECTORY, folder_name), file_name))


if __name__ == "__main__":
    main()
