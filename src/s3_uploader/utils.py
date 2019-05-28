import os
import boto3

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

s3 = boto3.client(
   "s3",
   aws_access_key_id=os.environ.get("S3_ACCESS_KEY"), # PUT YOUR ACCESS KEY 
   aws_secret_access_key=os.environ.get("S3_SECRET_ACCESS_KEY") # PUT YOUR SECRET ACCESS KEY 
)

def uploadImage(file, bucket_name="group-c", acl="public-read"): 
    
    # Uploads file
    s3.upload_fileobj(
        file, 
        bucket_name,
        'images/{}'.format(file.filename),
        ExtraArgs={
            "ACL": acl, # makes sure that everyone has access to the image 
            "ContentType": file.content_type, 
        }
    )    

def allowed_file(filename):
    try:
        name, ext = filename.rsplit('.', 1)
    except ValueError:
        return False
    return ext.lower() in ALLOWED_EXTENSIONS