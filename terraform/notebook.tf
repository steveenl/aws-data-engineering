resource "databricks_notebook" "device_health" {
    source = file("${path.cwd}/../device_health.py")
    path = "/aws-data-engineering"
    language = "PYTHON"
}