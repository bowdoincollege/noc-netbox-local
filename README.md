# netbox local

Module for site-specific netbox features

## `pipeline.py`

Pipelines for social auth.  Currently, just `new_user_handler` to give
new users read-only access.  Add function to `SOCIAL_AUTH_PIPELINE` list
in `configuration.py`.
