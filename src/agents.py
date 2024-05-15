from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun

# Initialize and configure the Wikipedia API wrapper
# This wrapper fetches up to 2 results per query and limits the content to 1000 characters
api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=1000)
# Create a WikipediaQueryRun tool using the API wrapper
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

# Initialize and configure the DuckDuckGo Search API wrapper
# This wrapper is set to fetch news results from the German region ("de-de")
# and limits the results to the past day ("d") with a maximum of 4 results
wrapper = DuckDuckGoSearchAPIWrapper(region="de-de", time="d", max_results=4)
# Create a DuckDuckGoSearchResults tool using the API wrapper, specifying the source as "news"
ddg_search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")

# Initialize and configure the Arxiv API wrapper
# This wrapper fetches up to 1 result per query and limits the content to 1000 characters
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
# Create an ArxivQueryRun tool using the API wrapper
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

# Combine all tools into a single list for easy management and use
tools = [ddg_search, arxiv]

# The 'tools' list now contains the configured search and query tools for:
# 1. DuckDuckGo news search results
# 2. Arxiv academic paper search results
# 3. Wikipedia search results
