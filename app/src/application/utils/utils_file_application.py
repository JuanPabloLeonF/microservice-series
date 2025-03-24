import os
import uuid
from fastapi import UploadFile
from app.configuration.enviroments_config import ALLOW_EXTENSIONS_FILE_IMG, ALLOW_EXTENSIONS_FILE_VIDEO, MAX_SIZE_IMG_FILE_MB, MAX_SIZE_VIDEO_FILE_MB

class UtilsFilesApplication:

    @staticmethod
    def createFolder(folderName: str) -> None:
        os.makedirs(name=folderName, exist_ok=True)

    @staticmethod
    def validateExtensionFile(file: UploadFile, listExtensions: list[str]) -> None:
        extension: str = UtilsFilesApplication.getExtensionsFile(file=file)
        if extension not in listExtensions:
            raise ValueError("Invalid file extension")

    @staticmethod
    def convertSizeToMB(file: UploadFile) -> float:
        file.file.seek(0, os.SEEK_END)
        size = file.file.tell()
        file.file.seek(0)
        return size / (1024 * 1024)

    @staticmethod
    def getExtensionsFile(file: UploadFile) -> str:
        return file.filename.split(".")[-1].lower()

    @staticmethod
    def validateMaxSizeVideoFile(file: UploadFile) -> None:
        sizeMB: float = UtilsFilesApplication.convertSizeToMB(file=file)
        if sizeMB > MAX_SIZE_VIDEO_FILE_MB:
            raise ValueError(f"Lo siento el archivo es demasiado pesado, maximo de {MAX_SIZE_VIDEO_FILE_MB}MB")

    @staticmethod
    def validateMaxSizeImgFile(file: UploadFile) -> None:
        sizeMB: float = UtilsFilesApplication.convertSizeToMB(file=file)
        if sizeMB > MAX_SIZE_IMG_FILE_MB:
            raise ValueError(f"Lo siento el archivo es demasiado pesado, maximo de {MAX_SIZE_IMG_FILE_MB}MB")

    @staticmethod
    def deletedFile(filePath: str) -> None:
        if os.path.exists(filePath):
            os.remove(filePath)

    @staticmethod
    def deleteDirectoryFull(folderName: str) -> None:
        if os.path.exists(folderName):
            os.rmdir(folderName)

    @staticmethod
    def saveFile(file: UploadFile, folderName: str) -> str:

        UtilsFilesApplication.validateExtensionFile(
            file=file,
            listExtensions=ALLOW_EXTENSIONS_FILE_IMG + ALLOW_EXTENSIONS_FILE_VIDEO
        )

        extension: str = UtilsFilesApplication.getExtensionsFile(file=file)
        fileNameFull: str = f"{uuid.uuid4()}.{extension}"
        UtilsFilesApplication.createFolder(folderName=folderName)
        filePath: str = os.path.join(folderName, fileNameFull)

        if extension in ALLOW_EXTENSIONS_FILE_IMG:
            UtilsFilesApplication.validateMaxSizeImgFile(file=file)

        if extension in ALLOW_EXTENSIONS_FILE_VIDEO:
            UtilsFilesApplication.validateMaxSizeVideoFile(file=file)

        with open(filePath, "wb") as buffer:
            buffer.write(file.file.read())
        return filePath