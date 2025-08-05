import asyncio
from config.settings import settings
from services.chat_service import ChatService

async def main():
    """Main function of the application"""
    try:
        # Validate settings
        settings.validate()

        # Start chat service
        chat_service = ChatService()
        await chat_service.start_chat_loop()
        
    except ValueError as e:
        print(f"Configuration error: {e}")
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(main())