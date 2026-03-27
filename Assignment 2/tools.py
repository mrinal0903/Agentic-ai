from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool

def get_tools():
    search = DuckDuckGoSearchRun()
    wiki_api = WikipediaAPIWrapper()
    wiki = WikipediaQueryRun(api_wrapper=wiki_api)

    return [
        Tool(name="Web Search", func=search.run, description="Search internet"),
        Tool(name="Wikipedia", func=wiki.run, description="Get topic info")
    ]
