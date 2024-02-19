resource "databricks_job" "device_health_job" {
  name = "Job to generate and aggregate device health"

  job_cluster {
    job_cluster_key = "job_a"
    new_cluster {
      num_workers   = 2
      spark_version = data.databricks_spark_version.latest.id
      node_type_id  = data.databricks_node_type.smallest.id
    }
  }

  task {
    task_key        = "a"
    job_cluster_key = "job_a"
    notebook_task {
      notebook_path = databricks_notebook.device_health.path
    }
  }
}
