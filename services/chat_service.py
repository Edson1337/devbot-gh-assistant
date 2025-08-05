from services.agent_service import AgentService

class ChatService:
    """Service responsible for the conversation loop"""
    
    def __init__(self):
        self.agent_service = AgentService()
        self.config = {'configurable': {'thread_id': '1'}}
    
    async def start_chat_loop(self):
        """Starts the main conversation loop"""
        agent_executor = await self.agent_service.get_agent_executor()
        
        print("Chat started! Type 'quit' to exit.")
        
        while True:
            user_input = input('Type: ')
            
            if user_input.lower() in ['quit', 'exit', 'sair']:
                print("Ending chat...")
                break
            
            await self._process_message(agent_executor, user_input)
    
    async def _process_message(self, agent_executor, user_input: str):
        """Processes a user message"""
        input_message = {
            'role': 'user',
            'content': user_input,
        }
        
        async for step in agent_executor.astream(
            {'messages': [input_message]}, 
            self.config, 
            stream_mode='values'
        ):
            step['messages'][-1].pretty_print()