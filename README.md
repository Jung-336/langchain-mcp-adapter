# LangChain MCP 어댑터

이 프로젝트는 LangChain과 MCP(Model Context Protocol) 서버들을 연결하는 어댑터입니다. 다양한 MCP 서버와의 통합을 통해 확장 가능한 AI 에이전트를 구축할 수 있습니다.

## 주요 기능

- 여러 MCP 서버와의 통합 지원
- LangChain의 React 에이전트와 연동
- 비동기 처리 지원
- 수학 연산 및 날씨 정보 조회 기능

## 시작하기

### 사전 요구사항

- Python 3.8 이상
- pip 패키지 관리자

### 설치

1. 저장소 클론:
   ```bash
   git clone [저장소 주소]
   cd langchain-mcp-adapter
   ```

2. 가상 환경 생성 및 활성화 (권장):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```

4. 환경 변수 설정:
   `.env` 파일을 생성하고 필요한 환경 변수를 설정하세요.

### 사용 방법

```python
from langchain_xai import ChatXAI
from langgraph.prebuilt import create_react_agent

# MCP 서버 설정
mcp_servers = {
    "math": {
        "command": "python",
        "args": ["servers/math_server.py"],
    },
    "weather": {
        "url": "http://localhost:8000/sse",
        "transport": "sse",
    },
}

# 에이전트 실행
async def main():
    async with MultiServerMCPClient(mcp_servers) as client:
        agent = create_react_agent(llm, client.get_tools())
        result = await agent.ainvoke({"messages": "서울의 날씨는 어떤가요?"})
        print(result["messages"][-1].content)
```

## 지원하는 MCP 서버

- **수학 서버**: 기본적인 수학 연산 수행
- **날씨 서버**: 도시별 날씨 정보 조회

## 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 기여 방법

1. 이슈를 생성하여 변경사항을 논의하세요.
2. 포크하고 기능 브랜치를 만드세요.
3. 변경사항을 커밋하고 푸시하세요.
4. 풀 리퀘스트를 열어주세요.

## 문의

질문이나 제안사항이 있으시면 이슈를 통해 문의해 주세요.
