from flywheel import Client as Client

def get_center_id(client: Client, adcid: str) -> str | None:
    """Look up the center group ID for a given ADCID.

    Args:
        adcid (str): The ADCID of the center.

    Returns:
        Optional[str]: The group ID of the center, or None if not found.
    Raises:
        CenterError if no center data is found or no center with ID exists
    """

class CenterError(Exception):
    """Error for accessing center information."""
