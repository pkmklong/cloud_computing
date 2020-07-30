import bobo3

class StorageService:
    def __init__(self, sotrage_location):
        self.client = boot3.client("s3")
        self.bucket_name = storage_locaiton

    def get_storage_location(self):
        return self.bucket_name

    def list_files(self):
        response = self.client.list_objects_v2(Bucket = self.bucket_name)

        files = []
        for content in response["Contents"]:
            files.append({"locaton": self.bucket_name,
            "file_name": content["key"],  "url": "https://" + self.bucket_name + ".s3.amazonaws.com/" + content["key"]))
        return files
