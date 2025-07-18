from flywheel import FileOutput as FileOutput, Project as Project
from typing import Any, Callable, Literal

ERROR_HEADER_NAMES: list[str]
STATUS_HEADER_NAMES: list[str]

def qc_data(file_object: FileOutput) -> dict[str, Any]:
    """Returns the QC object in the metadata for the file.

    Args:
      file_object: the file metadata
    Returns:
      the dictionary for info.qc if non-empty. Otherwise, the empty dictionary.
    """
def validation_data(qc_object: dict[str, Any], gear_name: str) -> dict[str, Any]:
    """Returns the validation object in the QC metadata for the named gear.

    Args:
      qc_object: the QC metadata (file.info.qc)
      gear_name: the name of the gear
    """
def error_data(qc_object: dict[str, Any], gear_name: str) -> dict[str, Any]:
    """Returns the error object in the QC metadata.

    Args:
      qc_object: the QC metadata (file.info.qc)
      gear_name: the name of the gear
    Returns:
      the dictionary for gear_name.validation.data if exists.
      Otherwise, the empty dictionary.
    """
def status_data(qc_object: dict[str, Any], gear_name: str) -> Literal['pass', 'fail'] | None:
    """Returns the QC status in the QC metadata.

    Args:
      qc_object: the QC metadata (file.info.qc)
      gear_name: the name of the gear
    Returns:
      the QC status for the gear if set. None, otherwise.
    """
def build_qc_info_list(file_object: FileOutput, insert_info: Callable[[dict[str, Any], str, list[dict[str, Any]]], None]) -> list[dict[str, Any]]:
    """Build dictionaries for output of QC data for the file using the insert
    function.

    Args:
      file_object: the FW file
      insert_info: the QC data insert function
    Returns:
      A list of dictionaries for each object in the QC data for the file
    """
def get_qc_data(project: Project, info_builder: Callable[[FileOutput], list[dict[str, Any]]]) -> list[dict[str, Any]]:
    """Helper function to create list of dictionaries created by the info
    builder function applied to files in the project.

    Args:
      project: the project
      info_builder: function to create list of QC information
    Returns:
      List of QC information dictionaries for files in the project
    """
def get_error_data(project: Project) -> list[dict[str, Any]]:
    """Creates a list of dictionaries, each corresponding to an error in a file
    in the project.

    Args:
      project: the flywheel project object
    """
def get_status_data(project: Project) -> list[dict[str, Any]]:
    """Returns a list of dictionaries containing QC status data for files in
    the project.

    Args:
      project: the project
    Returns:
      a list of containing status info objects for files in the project
    """
