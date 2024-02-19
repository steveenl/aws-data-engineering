terraform {
  required_providers {
    databricks = {
      source = "databricks/databricks"
    }
  }
}

provider "databricks" {}

data "databricks_spark_version" "latest" {}
data "databricks_node_type" "smallest" {
  local_disk = true
}
