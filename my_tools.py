## Importing libraries and files

#import crewai_tools as tools
import os
from dotenv import load_dotenv
load_dotenv()

#from crewai-tools.tools import SerperDevTool
# from crewai_tools.tools.serper_dev_tool.serper_dev_tool import SerperDevTool






from langchain_community.document_loaders import PDFLoader  # Ensure this is installed



## Creating search tool
# search_tool = SerperDevTool()  # Use the class itself, or instantiate if needed: SerperDevTool()

## Creating custom PDF reader tool
class BloodTestReportTool:
    @staticmethod
    async def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a PDF file at a given path.

        Args:
            path (str): Path of the PDF file.

        Returns:
            str: Cleaned and formatted blood test report content.
        """
        try:
            docs = PDFLoader(file_path=path).load()
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

        full_report = ""
        for data in docs:
            content = data.page_content.strip()
            content = content.replace("\n\n", "\n")  # Normalize spacing
            full_report += content + "\n"

        return full_report

## Creating Nutrition Analysis Tool
class NutritionTool:
    @staticmethod
    async def analyze_nutrition_tool(blood_report_data: str):
        """Analyze blood data and generate nutrition advice (placeholder).

        Args:
            blood_report_data (str): The blood test report as text.

        Returns:
            str: Nutrition recommendations (to be implemented).
        """
        cleaned_data = blood_report_data.replace("  ", " ")
        # TODO: Implement real analysis logic
        return "Nutrition analysis functionality to be implemented"

## Creating Exercise Planning Tool
class ExerciseTool:
    @staticmethod
    async def create_exercise_plan_tool(blood_report_data: str):
        """Generate an exercise plan based on blood data (placeholder).

        Args:
            blood_report_data (str): The blood test report as text.

        Returns:
            str: Exercise plan or suggestions.
        """
        # TODO: Implement real exercise plan logic
        return "Exercise planning functionality to be implemented"
