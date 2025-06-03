import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI  # OpenAI용 LLM 임포트 (필요시 설치)
from langchain_anthropic import ChatAnthropic  # Anthropic용 LLM 임포트 (최신)
from langchain_groq import ChatGroq 
from langchain_xai import ChatXAI 
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatXAI(model="grok-3-fast-latest")





async def main():
    async with MultiServerMCPClient({
                    "math": {
                        "command": "python",
                        "args": [
                            "D:\\vibe-coding\\mcp-crash-course-udemy\\langchain-mcp-adapter\\servers\\math_server.py"
                        ],
                    },
                    "weather": {
                        "url": "http://localhost:8000/sse",
                        "transport": "sse",
                    },
                }   ) as client:
        agent = create_react_agent(llm, client.get_tools())
        result = await agent.ainvoke({"messages":"What is the weather in New York?"})
        print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())


    