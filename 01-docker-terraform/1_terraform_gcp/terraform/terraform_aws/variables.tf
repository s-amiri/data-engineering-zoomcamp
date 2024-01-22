variable "region" {
  type    = string
  default = "eu-central-1"
}

variable "bucket_name" {
  type        = string
  description = "A globally unique name for the S3 bucket"
}

variable "acl" {
  type    = string
  default = "private"
}
