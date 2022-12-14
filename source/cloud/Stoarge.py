import os
from pprint import pprint
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'source/cloud/INFO.json'
storage_client = storage.Client()

class cloud:
   
    def __init__(self) -> None:
        self.bucket_name = 'game1data1'

    # # create a new bucket
    # bucket = storage_client.bucket(bucket_name)
    # bucket.storage_class = 'COLDLINE' # Archive | Nearline | Standard
    # bucket.location = 'US' # Taiwan
    # bucket = storage_client.create_bucket(bucket) # returns Bucket object

    # pprint(vars(bucket))

    # bucket.name
    # bucket._properties['selfLink']
    # bucket._properties['id']
    # bucket._properties['location']
    # bucket._properties['timeCreated']
    # bucket._properties['storageClass']
    # bucket._properties['timeCreated']
    # bucket._properties['updated']

    """
    Get Bucket
    """
    # my_bucket = storage_client.get_bucket(self.bucket_name)
    # pprint(vars(my_bucket))

    """
    Upload File
    """
    def upload_to_bucket(self, blob_name, file_path):
        '''
        Upload file to a bucket
        : blob_name  (str) - object name
        : file_path (str)
        : bucket_name (str)
        '''
        bucket = storage_client.get_bucket(self.bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return blob


    # response = upload_to_bucket('DATA.json', "sample.json" , self.bucket_name)


    """
    Download File By Blob Name
    """
    def download_file_from_bucket(self, blog_name, file_path):
        bucket = storage_client.get_bucket(self.bucket_name)
        blob = bucket.blob(blog_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        print('Saved')

    # download_file_from_bucket('NEW.json', 'sample.json', self.bucket_name)


    """
    Download File By Passing URI Path
    """
    # def download_file_uri(uri, file_path):
    #     with open(file_path, 'wb') as f:
    #         storage_client.download_blob_to_file(uri, f)
    #     print('Saved')

    # uri = 'gs://<uri>'
    # # download_file_uri(uri, r'H:\PythonVenv\GoogleAI\Cloud Storage\Voice List2.csv')



    """
    List Buckets
    list_buckets(max_results=None, page_token=None, prefix=None, projection='noAcl', fields=None, project=None, timeout=60, retry=<google.api_core.retry.Retry object>)
    """
    # for bucket in storage_client.list_buckets(max_results=100):
    #     print(bucket)