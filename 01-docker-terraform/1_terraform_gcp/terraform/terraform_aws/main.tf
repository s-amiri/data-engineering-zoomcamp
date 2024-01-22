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
