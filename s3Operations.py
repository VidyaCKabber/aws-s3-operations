import boto3


class S3Operaions:
    def __init__(self):
        self.client = boto3.client('s3')
        self.bucket_name = 'mybucket'
        self.bucket = None
    
    def create_bucket(self):
        '''create bucket'''
        self.bucket = self.client.create_bucket(Bucket = self.bucket_name)
        assert self.bucket['ResponseMetadata']['HTTPStatusCode'] == 200


    def list_buckets(self):
        '''list existing buckets'''
        list_buckets = self.client.list_buckets()
        assert list_buckets['Buckets'] is not None

    def upload_objects(self, file_name, bucket, object_name=None, args=None):
        """upload objects to destination bucket
        file_name : file name in local system
        bucket : destination bucket
        object_name : file name on s3 bucket
        args : custom args
        """
        
        self.client.upload_file(file_name, bucket, object_name, ExtraArgs = args)
        res = self.client.list_objects(Bucket=bucket)
        isObjFound = False
        for obj in res['Contents']:
            if object_name in obj['Key']:
                isObjFound = True
                break
        if isObjFound:
            assert True
        else:
            assert False    

if __name__ == '__main__':
    s = S3Operaions()
    s.create_bucket()
    s.list_buckets()
    s.upload_objects('/files/birthday.gif', 'mybucket', 'birthday.gif')