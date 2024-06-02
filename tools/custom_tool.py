from crewai_tools import BaseTool


class MyCustomTool(BaseTool):
    name: str = "Tool name"
    description: str = "Tool description"

    def _run(self) -> str:
        # Add your code here
        return
