from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from mcp_tools.mcp_servers import MCP_SERVERS_CONFIG
from prompt.agent_system_prompt import AGENT_SYSTEM_PROMPT
from services.model_service import ModelService

class AgentService:
    """Service responsible for creating and configuring the agent"""
    
    def __init__(self):
        self.model_service = ModelService()
        self.memory = MemorySaver()
        self.mcp_client = MultiServerMCPClient(MCP_SERVERS_CONFIG)
        self._agent_executor = None
    
    async def get_agent_executor(self):
        """Initializes and returns the agent executor"""
        if self._agent_executor is None:
            model = self.model_service.get_model()
            tools = await self.mcp_client.get_tools()
            
            self._agent_executor = create_react_agent(
                model=model,
                tools=tools,
                prompt=AGENT_SYSTEM_PROMPT,
                checkpointer=self.memory,
            )
        
        return self._agent_executor