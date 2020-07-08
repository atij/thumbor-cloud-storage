from tornado.concurrent import return_future
from gcloud import storage

buckets = {}


@return_future
def load(context, path, callback):
    project_id = context.config.get("CLOUD_STORAGE_PROJECT_ID")

    # get the app key from path
    b = path.split('/').get(0, None)

    # load buckets
    if len(buckets) == 0:
        # bucket config, dictionary with app_name => bucket_id
        bucket_settings = context.config.get("CLOUD_STORAGE_BUCKETS")
        # Update bucket list with configured buckets
        for k, v in bucket_settings.items():
            client = storage.Client(project_id)
            bucket = client.get_bucket(v)
            buckets[k] = bucket

    bucket = buckets.get(b)
    p = path.split('/')
    blob = bucket.get_blob('/'.join((p[1:])))

    if blob:
        callback(blob.download_as_string())
    else:
        callback(blob)
