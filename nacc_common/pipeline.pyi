from flywheel import Client as Client, Project as Project
from typing import Literal

def get_project(client: Client, group_id: str, datatype: Literal['form', 'enrollment', 'dicom'] = 'form', pipeline_type: Literal['ingest', 'sandbox'] = 'sandbox', study_id: str = 'adrc') -> Project:
    """Look up the project for a given center, study, and datatype.

    Args:
        group_id (str): The group ID of the center.
        datatype (str): The datatype to look up.
        pipeline_type (str): The type of the pipeline.
        study_id (str): The study ID for the project.
    Returns:
        Project: The project for the given center, study, and datatype.
    """

class PipelineProjectError(Exception):
    """Error for missing pipeline project."""

def get_published_view(client: Client, label: str) -> str:
    """Return the view ID for the published dataview.

    Args:
      client: the Flywheel SDK client
      label: the label for the dataview to return
    Returns:
      the ID for the dataview
    """
