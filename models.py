from pydantic import BaseModel, Field


class IncidentAnalysis(BaseModel):
    """
    Schema for AI generated incident analysis.
    """

    summary: str = Field(
        description="A concise summary of the incident"
    )

    priority: str = Field(
        description="Priority level of the incident: Critical, High, Medium, Low"
    )

    agencies: list[str] = Field(
        description="List of agencies required to handle the incident"
    )