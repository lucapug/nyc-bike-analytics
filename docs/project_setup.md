### Steps to reproduce the analysis

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

Change all the values in `variables.tf` with the ones corresponding to your google clud resources.

Remember also to change in the io_config.yml your key name:

```
# GOOGLE
GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/.dbt/dtc-de-zoomcamp-2024-4a477d7bc858.json"
GOOGLE_LOCATION: US # Optional
```

Also, for dbt to connect to google cloud when making the transformations, you must edit `profiles.yml` in the `dbt_ops` folder (modify project, dataset, key_file and location entries)

You are now ready to create the cloud resources for the project:

`cd terraform`

`terraform init`

`terraform plan`

`terraform apply`

With the gcs bucket and the bq dataset created, it is now time to install Mage AI on your machine and launch the application to reproduce the blocks of the data pipeline; we make the installation in a dockerized way, the only way in which you can have DBT integrated in the Mage project at the moment, by easily adding DBT blocks to the pipeline when necessary.

`docker run -it -p 6789:6789 -p 8080:8080 -v $(pwd):/home/src mageai/mageai /app/run_app.sh mage start mage_dbt_gcp`

the two forwarded ports are respectively for accessing in the web browser to the Mage UI (http://localhost:6789) and to the static web site containing the dbt project documentation (and in particular the lineage graph) (http://localhost:8080). While the Mage UI is up and running after the docker command, we will see in the following how to serve the dbt documentation in a static web site.

from now on, the rest of the project can be run from inside the Mage UI, where there is also a terminal (that is executed inside the running container)

Open the bike_analytics pipeline. The first 3 blocks of the pipeline must be executed for each year from 2019 to 2023. The year environment variable must be set manually at each execution of the three blocks. Once this operation is finished, you have 5 external tables in the BigQuery dataset, on which you can make the subsequent transformations by means of DBT blocks.

Each one of the DBT blocks must be execude only one time. The first block materializes to a staging table (partitioned and clustered for optimal performance of the successive operations) the 5 external tables built before. The second DBT block select the columns of interest for the analysis and add on the fly a calculated column (trip_duration). Its output is the facts_JC_citibike_trips.

Finally you can connect Looker studio to this facts table and create tiles like the ones proposed in my report, to exctract insights from the dataset.

In order to see the dbt project documentation, including the lineage graph, open a terminal **inside Mage AI** and launch the following commands in the dbt_ops folder:

`dbt docs generate`

`dbt docs serve`

By doing so (and having forwarded the port 8080 in the containerization operation) you can see the stati website at localhost:8080. Notice that this is a static website. If you make successive modifications to the sources, models or any other component of the dbt project, you have to generate the documentation site again to reflect the changes in the documentation.

When you are done with the experimentation of the project, you can stop the docker container (this time the terminal is the one outside the container, that you have used previously):

`docker stop [container name] `

you can find the container name with: `docker ps -a`

finally you can delete the google cloud resources with the command:

`terraform destroy`

hope you enjoy!
