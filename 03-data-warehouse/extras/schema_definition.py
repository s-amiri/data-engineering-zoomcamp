# schema_definition.py

import pyarrow as pa

def get_yellow_taxi_schema():
    schema = pa.schema([
        ('VendorID', pa.int64()),
        ('tpep_pickup_datetime', pa.string()),
        ('tpep_dropoff_datetime', pa.string()),
        ('passenger_count', pa.int64()),
        ('trip_distance', pa.float64()),
        ('RatecodeID', pa.int64()),
        ('store_and_fwd_flag', pa.string()),
        ('PULocationID', pa.int64()),
        ('DOLocationID', pa.int64()),
        ('payment_type', pa.int64()),
        ('fare_amount', pa.float64()),
        ('extra', pa.float64()),
        ('mta_tax', pa.float64()),
        ('tip_amount', pa.float64()),
        ('tolls_amount', pa.float64()),
        ('improvement_surcharge', pa.float64()),
        ('total_amount', pa.float64()),
        ('congestion_surcharge', pa.float64())
    ])
    return schema

def get_fhv_trips_schema():
    schema = pa.schema([
        ('dispatching_base_num', pa.string()), 
        ('pickup_datetime', pa.string()),      
        ('dropOff_datetime', pa.string()),     
        ('PUlocationID', pa.int64()),         
        ('DOlocationID', pa.int64()),         
        ('SR_Flag', pa.float64()),              
        ('Affiliated_base_number', pa.string())
    ])
    return schema

def get_green_taxi_schema():
    schema = pa.schema([
        ('VendorID', pa.int64()),
        ('lpep_pickup_datetime', pa.string()),
        ('lpep_dropoff_datetime', pa.string()),
        ('store_and_fwd_flag', pa.string()),
        ('RatecodeID', pa.int64()),
        ('PULocationID', pa.int64()),
        ('DOLocationID', pa.int64()),
        ('passenger_count', pa.int64()),
        ('trip_distance', pa.float64()),
        ('fare_amount', pa.float64()),
        ('extra', pa.float64()),
        ('mta_tax', pa.float64()),
        ('tip_amount', pa.float64()),
        ('tolls_amount', pa.float64()),
        ('ehail_fee', pa.float64()),
        ('improvement_surcharge', pa.float64()),
        ('total_amount', pa.float64()),
        ('payment_type', pa.int64()),
        ('trip_type', pa.int64()),
        ('congestion_surcharge', pa.float64())
    ])
    return schema