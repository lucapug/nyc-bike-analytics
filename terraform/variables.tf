variable "credentials" {
  description = "My credentials"
  default     = "../.dbt/dtc-de-zoomcamp-2024-4a477d7bc858.json"
}

variable "project" {
  description = "Project"
  default     = "dtc-de-zoomcamp-2024"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "zone" {
  description = "Zone"
  default     = "us-central1-c"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default     = "nyc_bikes"
}

variable "gcs_bucket_name" {
  description = "MY GCS bucket name"
  default     = "nyc_bike_lucapug"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "uniform_bucket_level_access" {
  description = "Uniform bucket level access"
  default     = true
}
