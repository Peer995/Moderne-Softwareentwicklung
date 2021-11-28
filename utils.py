import logging
import os
import boto3
from botocore.exceptions import ClientError

"""
Funktion zur Vorzertifizierung von URLs. Dieser Prozess ist für einige URLs notwendig, da Alexa nur Daten von durch Amazon anerkannte zertifizierte
Seiten entgegennimmt. So lässt sich beispielsweise - in dieser Methode - auf den S3-Storage zugreifen, der zu AWS gehört.
"""
def create_presigned_url(object_name):
    s3_client = boto3.client('s3',
                             region_name=os.environ.get('S3_PERSISTENCE_REGION'),
                             config=boto3.session.Config(signature_version='s3v4',s3={'addressing_style': 'path'}))
    try:
        bucket_name = os.environ.get('S3_PERSISTENCE_BUCKET')
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=60*1)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response