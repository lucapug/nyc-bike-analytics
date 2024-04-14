#### Steps to reproduce the analysis

Clone or fork this repository to your machine

You need to have already installed in your coding environment on your machine:

* Docker (to build and run the container that executes Mage AI, with dbt integrated)
* Terraform (to manage the cloud infrastructure (gcs bucket and bq dataset)
* google-cloud-cli (to allow terraform to interact with google cloud platform services)

You need to have a google account and to create in Google Cloud a GCP Project with an associated service account with the following permissions:

* roles/storage.Admin: This role grants full administrative access to Cloud Storage buckets, allowing Terraform to create, delete, and modify them.
* roles/bigquery.DataEditor: This role allows creating, updating, and deleting datasets and tables in BigQuery. Terraform requires this role to manage BigQuery resources like creating datasets and tables or deleting them.
* roles/BigQuery Job User: This role allows submitting BigQuery Jobs.

Then generate a JSON service account key that you will download inside the `.dbt` folder. These are the credentials with which terraform will communicate and write/read to Google cloud resources. Notice that this key must not be published; in particular do not upload it to Github (that's why there is a local .gitignore inside .dbt folder)

Now, in the same terminal session where you will execute the terraform commands, assign this environment variable (necessary for terraform to be accredited to the google services):

`export GOOGLE_APPLICATION_CREDENTIALS="$HOME/nyc-bike-analytics/.dbt/[your-key-name-here].json"`

Change all the values in `variables.tf` to your convenience.

You are now ready to create the cloud resources for the project:

`cd terraform`

`terraform init`

`terraform plan`

`terraform apply`

With the gcs bucket and the bq dataset created, it is now time to install Mage AI on your machine, in a dockerized way, the only way in which you can have DBT integrated in the Mage project, at the moment, easily adding DBT blocks to the pipeline when necessary.

`docker run -it -p 6789:6789 -p 8080:8080 -v $(pwd):/home/src mageai/mageai /app/run_app.sh mage start mage_dbt_gcp`

the two forwarded ports are respectively for accessing in the web browser to the Mage UI (http://localhost:6789) and to the static web site containing the dbt project documentation (and in particular the lineage graph) (http://localhost:8080)

from now on, the rest of the project can be run from inside the Mage UI, where there is also a terminal (that is executed inside the running container)
