import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from prompts import INCIDENT_ANALYSIS_PROMPT
from parser import get_parser


# Load environment variables
load_dotenv()


# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)


# Get JSON parser
parser = get_parser()


# Create Prompt Template
prompt = PromptTemplate(
    template=INCIDENT_ANALYSIS_PROMPT,
    input_variables=["incident_text"]
)


# Create AI Chain
incident_chain = (
    prompt
    | llm
    | parser
)


def analyze_incident(incident_text: str):
    """
    Analyze incident and return structured response.
    """

    response = incident_chain.invoke(
        {
            "incident_text": incident_text
        }
    )

    return response