provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = var.bucket_name
  acl    = var.acl

  versioning {
    enabled = true
  }

  # You can add more configuration options as needed, e.g., tags, logging, etc.
}

resource "aws_redshift_cluster" "my_redshift_cluster" {
  cluster_identifier         = var.redshift_cluster_identifier
  node_type                  = var.redshift_node_type
  cluster_type               = "single-node"
  master_username            = var.redshift_master_username
  master_password            = var.redshift_master_password
  skip_final_snapshot        = true
}