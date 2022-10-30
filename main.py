import os

EXTENSIONS = {"MICROSOFT_OFFICE": {"doc", "docx", "ppt", "pptx", "xls", "xlsx"},
              "IMAGES": {"png", "jpg", "jpeg", "gif"},
              "VIDEO_AND_AUDIO": {"mp3", "mp4", "wav"},
              "PDF": {"pdf"},
              "SCRIPTS_AND_EXECUTABLES": {"py", "java", "c", "cs", "cpp", "exe", "js", "json", "html", "css", "jar"}}

DOWNLOADS_DIRECTORY = "C:\\Users\\Reilly\\Downloads"
UNKNOWN = "UNKNOWN_EXTENSIONS.txt"


def main():
    files = os.listdir(DOWNLOADS_DIRECTORY)
    folders = list(filter(lambda x: "." not in x, files))
    files = list(filter(lambda x: "." in x, files))
    for folder_name in EXTENSIONS:
        if folder_name not in folders:
            os.mkdir(os.path.join(DOWNLOADS_DIRECTORY, folder_name))
    if UNKNOWN not in files:
        open(os.path.join(DOWNLOADS_DIRECTORY, UNKNOWN), 'x')
    for file_name in files:
        if file_name != UNKNOWN:
            extension = file_name.split(".")[-1]
            for folder_name in EXTENSIONS:
                if extension in EXTENSIONS[folder_name]:
                    os.rename(os.path.join(DOWNLOADS_DIRECTORY, file_name), os.path.join(os.path.join(DOWNLOADS_DIRECTORY, folder_name), file_name))
                else:
                    os.rename(os.path.join(DOWNLOADS_DIRECTORY, file_name), os.path.join(os.path.join(DOWNLOADS_DIRECTORY, "OTHER"), file_name))
                    with open(os.path.join(DOWNLOADS_DIRECTORY, UNKNOWN), "a") as f:
                        f.write(extension + "\n")


if __name__ == "__main__":
    main()
