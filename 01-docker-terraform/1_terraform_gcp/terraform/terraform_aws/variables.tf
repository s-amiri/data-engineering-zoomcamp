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

variable "redshift_cluster_identifier" {
  description = "The identifier for the Amazon Redshift cluster."
  default     = "my-redshift-cluster"
}

variable "redshift_node_type" {
  description = "The node type for the Amazon Redshift cluster."
  default     = "dc2.large"
}

variable "redshift_master_username" {
  description = "The master username for the Amazon Redshift cluster."
  default     = "masteruser"
}

variable "redshift_master_password" {
  description = "The master password for the Amazon Redshift cluster."
  default     = "MySuperSecretPassword"
}
