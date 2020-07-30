from storage_service import StorageService
from recognition_service import RecognitionService
import sys

def main(bucket_name):

    for file in storage_service.get_all_files(bucket_name):
        if file.key.endswith(".jpg"):
            print(f"Objects detected in image {file.key} :")
            labels = recogntion_service.detect_objects(file.bucket_name, file.key)
            for label in labels:
                print(f"-- {label['Name']}: {str(label['Confidence'])}")

if __name__=="__main__":

    storage_service = StorageService()
    recogntion_service =  RecognitionService()
    bucket_name = sys.argv[1]
    main(bucket_name)
