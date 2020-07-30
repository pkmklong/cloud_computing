from storage_service import StorageService
from recognition_service import RecognitionService


storage_service = StorageService()
recogntion_service =  RecognitionService()

bucket_name = "aws-bucket-fun"

for file in storage_service.get_all_files(bucket_name):
    if file.key.endswith(".jpg"):
        print("Objects detected in image " + file.key + ":")
        labels = recogntion_service.detect_objects(file.bucket_name, file.key)
        for label in labels:
            print("-- "  + label["Name"] + ": " + str(label["Confidence"]))


