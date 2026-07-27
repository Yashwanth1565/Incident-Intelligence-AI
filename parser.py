from langchain_core.output_parsers import JsonOutputParser

from models import IncidentAnalysis


# Create parser using our Pydantic schema
incident_parser = JsonOutputParser(
    pydantic_object=IncidentAnalysis
)


def get_parser():
    """
    Returns the incident analysis output parser.
    """

    return incident_parser