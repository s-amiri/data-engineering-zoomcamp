import os
import requests
import pandas as pd
import boto3
from dotenv import load_dotenv
import pyarrow as pa
import pyarrow.parquet as pq
from schema_definition import get_yellow_taxi_schema

# Load environment variables
load_dotenv()

# services = ['fhv','green','yellow']
init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download'
# switch out the bucketname
s3_bucket_name = os.getenv('S3_BUCKET_NAME')

def download_file(url, output_path):
    with requests.get(url, stream=True) as response:
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=10240):
                    f.write(chunk)
            print(f"Downloaded {url} to {output_path}")
        else:
             print(f"Failed to download {url}")
    
    
def upload_to_aws(bucket_name, key, file_path):
    s3 = boto3.client('s3')
    try:
        # Upload the file to S3
        with open(file_path, 'rb') as f:
            s3.upload_fileobj(f, bucket_name, key)
        print(f"Uploaded {file_path} to S3://{bucket_name}/{key}")
        return True
    except Exception as e:
        print(f"Error uploading {file_path} to S3://{bucket_name}/{key}: {e}")
        return False
    
    s3.put_object(Bucket=bucket_name, Key=key, Body=data)

def delete_files(*files):
    # Delete the downloaded files
    for file in files:
        os.remove(file)
        print(f"Deleted {file}")

def convert_csv_to_parquet(csv_file, parquet_file):
    # Define chunk size for reading the CSV file
    chunk_size = 200000  # Adjust as needed based on available memory and file size

    parquet_writer = None
    schema = None

    # Import the schema
    schema = get_yellow_taxi_schema()

    # Use an iterator to load the gzip CSV file in chunks
    for i, chunk in enumerate(pd.read_csv(csv_file, compression='gzip', chunksize=chunk_size)):
        print(f"Processing chunk {i}")
        # Convert the chunk to a PyArrow Table
        table = pa.Table.from_pandas(chunk, schema=schema, preserve_index=False)
        
        # If the schema hasn't been defined yet, define it from the first chunk
        if parquet_writer is None:
            # schema = table.schema
            parquet_writer = pq.ParquetWriter(parquet_file, schema=schema)

        # Write the table (chunk) to the Parquet file
        parquet_writer.write_table(table)

    # Close the Parquet writer
    if parquet_writer:
        parquet_writer.close()
        print(f"Converted {csv_file} to {parquet_file}")

def web_to_aws(year, service):
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        file_name_initial = f"{service}_tripdata_{year}-{month}.csv.gz"
        
        # download it using requests via a pandas df
        request_url = f"{init_url}/{service}/{file_name_initial}"
        print(f"Request: {request_url}")
        download_file(request_url, file_name_initial)
        # open(file_name, 'wb').write(response_content)
        # print(f"Local: {file_name}")

        # read it back into a parquet file
        file_name = file_name_initial.replace('.csv.gz', '.parquet')
        convert_csv_to_parquet(file_name_initial, file_name)
        # df = pd.read_csv(file_name_initial, compression='gzip')
        # df.to_parquet(file_name_initial, engine='pyarrow')
        print(f"Parquet: {file_name}")

        # upload it to gcs 
        upload_to_aws(s3_bucket_name, f"{service}/{file_name}", file_name)
        print(f"aws: {service}/{file_name}")

        # delete the files
        delete_files(file_name_initial, file_name)


if __name__ == "__main__":
    
    # web_to_aws(2019, 'green')
    # web_to_aws(2020, 'green')

    web_to_aws(2019, 'yellow')
    web_to_aws(2020, 'yellow')

    # web_to_aws(2019, 'fhv')
