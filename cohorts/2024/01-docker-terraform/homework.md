## Module 1 Homework

## Docker & SQL

In this homework we'll prepare the environment 
and practice with Docker and SQL


## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command:

```docker build --help```

Do the same for "docker run".

Which tag has the following text? - *Automatically remove the container when it exits* 

- [ ] `--delete`
- [ ] `--rc`
- [ ] `--rmc`
- [x] `--rm`

```bash
docker run --help | grep "Automatically remove the container when it exits"
```

## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

- [x] 0.42.0
- [ ] 1.0.0
- [ ] 23.0.1
- [ ] 58.1.0

```bash
pip list | grep "wheel"
```

# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)


## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- [ ] 15767
- [x] 15612
- [ ] 15859
- [ ] 89009

```sql
SELECT COUNT(*) 
FROM green_taxi_data
WHERE DATE(lpep_pickup_datetime) = '2019-09-18' 
AND DATE(lpep_dropoff_datetime) = '2019-09-18';
```

## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

- [ ] 2019-09-18
- [ ] 2019-09-16
- [x] 2019-09-26
- [ ] 2019-09-21

```sql
SELECT
	lpep_pickup_datetime::DATE,
	MAX(trip_distance) AS max_trip_distance
FROM green_taxi_data
WHERE lpep_pickup_datetime::DATE BETWEEN '2019-09-16'
AND '2019-09-26'
GROUP BY lpep_pickup_datetime::DATE
ORDER BY 2 DESC;
```
## Question 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
 
- [x] "Brooklyn" "Manhattan" "Queens"
- [ ] "Bronx" "Brooklyn" "Manhattan"
- [ ] "Bronx" "Manhattan" "Queens" 
- [ ] "Brooklyn" "Queens" "Staten Island"

```sql
SELECT 
	"Borough",
	SUM(total_amount)
FROM green_taxi_data
LEFT JOIN zones
ON "PULocationID" = "LocationID"
WHERE lpep_pickup_datetime::DATE = '2019-09-18'
GROUP BY 1
HAVING SUM(total_amount) > 50000
ORDER BY 2 DESC;
```

## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- [ ] Central Park
- [ ] Jamaica
- [x] JFK Airport
- [ ] Long Island City/Queens Plaza

```sql
SELECT 
	z1."Zone" AS pickup_zone,
	z2."Zone" AS dropoff_zone,
	MAX(tip_amount) AS max_tip
FROM green_taxi_data
LEFT JOIN zones z1
ON "PULocationID" = z1."LocationID"
LEFT JOIN zones z2
ON "DOLocationID" = z2."LocationID"
WHERE z1."Zone" = 'Astoria'
GROUP BY 1, 2
ORDER BY 3 DESC;
```

## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  + create

Terraform will perform the following actions:

  # aws_redshift_cluster.my_redshift_cluster will be created
  + resource "aws_redshift_cluster" "my_redshift_cluster" {
      + allow_version_upgrade               = true
      + apply_immediately                   = false
      + aqua_configuration_status           = (known after apply)
      + arn                                 = (known after apply)
      + automated_snapshot_retention_period = 1
      + availability_zone                   = (known after apply)
      + cluster_identifier                  = "zoomcamp-redshift-cluster"
      + cluster_namespace_arn               = (known after apply)
      + cluster_nodes                       = (known after apply)
      + cluster_parameter_group_name        = (known after apply)
      + cluster_public_key                  = (known after apply)
      + cluster_revision_number             = (known after apply)
      + cluster_subnet_group_name           = (known after apply)
      + cluster_type                        = "single-node"
      + cluster_version                     = "1.0"
      + database_name                       = (known after apply)
      + default_iam_role_arn                = (known after apply)
      + dns_name                            = (known after apply)
      + encrypted                           = false
      + endpoint                            = (known after apply)
      + enhanced_vpc_routing                = (known after apply)
      + iam_roles                           = (known after apply)
      + id                                  = (known after apply)
      + kms_key_id                          = (known after apply)
      + maintenance_track_name              = "current"
      + manual_snapshot_retention_period    = -1
      + master_password                     = (sensitive value)
      + master_password_secret_arn          = (known after apply)
      + master_password_secret_kms_key_id   = (known after apply)
      + master_username                     = "masteruser"
      + node_type                           = "dc2.large"
      + number_of_nodes                     = 1
      + port                                = 5439
      + preferred_maintenance_window        = (known after apply)
      + publicly_accessible                 = true
      + skip_final_snapshot                 = false
      + tags_all                            = (known after apply)
      + vpc_security_group_ids              = (known after apply)
    }

  # aws_s3_bucket.my_bucket will be created
  + resource "aws_s3_bucket" "my_bucket" {
      + acceleration_status         = (known after apply)
      + acl                         = "private"
      + arn                         = (known after apply)
      + bucket                      = "zoomcamp-data-lake"
      + bucket_domain_name          = (known after apply)
      + bucket_prefix               = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + object_lock_enabled         = (known after apply)
      + policy                      = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + tags_all                    = (known after apply)
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + versioning {
          + enabled    = true
          + mfa_delete = false
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_s3_bucket.my_bucket: Creating...
aws_redshift_cluster.my_redshift_cluster: Creating...
aws_s3_bucket.my_bucket: Creation complete after 1s [id=zoomcamp-data-lake]
aws_redshift_cluster.my_redshift_cluster: Still creating... [10s elapsed]
aws_redshift_cluster.my_redshift_cluster: Still creating... [20s elapsed]
aws_redshift_cluster.my_redshift_cluster: Still creating... [30s elapsed]
aws_redshift_cluster.my_redshift_cluster: Still creating... [40s elapsed]
aws_redshift_cluster.my_redshift_cluster: Still creating... [50s elapsed]
aws_redshift_cluster.my_redshift_cluster: Still creating... [1m0s elapsed]
aws_redshift_cluster.my_redshift_cluster: Creation complete after 1m4s [id=zoomcamp-redshift-cluster]
```

## Submitting the solutions

* Form for submitting: https://courses.datatalks.club/de-zoomcamp-2024/homework/hw01
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 29 January, 23:00 CET
