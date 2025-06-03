import asyncio
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI  # OpenAI용 LLM 임포트 (필요시 설치)
from langchain_anthropic import ChatAnthropic  # Anthropic용 LLM 임포트 (최신)
from langchain_groq import ChatGroq 
from langchain_xai import ChatXAI 
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

# llm = ChatOpenAI(model="gpt-4o")
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro-preview-03-25")

llm = ChatXAI(model="grok-3-fast-latest")


stdio_server_params = StdioServerParameters(
    command = "python",
    args = ["D:\\vibe-coding\\mcp-crash-course-udemy\\langchain-mcp-adapter\\servers\\math_server.py"]
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            # print("session initialized")
            tools = await load_mcp_tools(session)
            # print(tools)
            agent = create_react_agent(llm, tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="(1+2)*(3+1) = ?")]})
            
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
