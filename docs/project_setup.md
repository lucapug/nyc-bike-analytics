#### Steps to reproduce the analysis

Clone or fork this repository to your machine

You need to have already installed in your coding environment:

* Docker (to build and run the container that executes Mage AI, with dbt integrated)
* Terraform (to manage the cloud infrastructure (gcs bucket and bq dataset)

* google-cloud-cli (to allow terraform to interact with google cloud platform services)

You need to have a google account and to create in Google Cloud a GCP Project with an associated service account with the following permissions:

* roles/storage.Admin: This role grants full administrative access to Cloud Storage buckets, allowing Terraform to create, delete, and modify them.
* roles/bigquery.DataEditor: This role allows creating, updating, and deleting datasets and tables in BigQuery. Terraform requires this role to manage BigQuery resources like creating datasets and tables or deleting them.
* roles/BigQuery Job User: This role allows submitting BigQuery Jobs.

Then generate a JSON service account key that you will download inside the .dbt folder. These are the credentials with which terraform (but also Mage AI) will communicate and write/read to Google cloud resources. Notice that this key must not be published; in particular do not upload it to Github (that's why there is a local .gitignore inside .dbt folder)

Now, in the same terminal session where you will execute the terraform commands, assign this environment variable (necessary for terraform to be accredited to the google services):

`export GOOGLE_APPLICATION_CREDENTIALS="$HOME/nyc-bike-analytics/.dbt/[your-key-name-here].json"`
