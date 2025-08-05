from decouple import config

GITHUB_MCP_URL = config('GITHUB_MCP_URL')
DUCK_GO_MCP_URL = config('DUCK_GO_MCP_URL')
SEQUENTIAL_THINKING_MCP_URL = config('SEQUENTIAL_THINKING_MCP_URL')

MCP_SERVERS_CONFIG = {
    'github-mcp': {
        'url': GITHUB_MCP_URL,
        'transport': 'streamable_http',
    },
    'duckduckgo-mcp': {
        'url': DUCK_GO_MCP_URL,
        'transport': 'streamable_http',
    },
    #     'sequentialthinking-tools': {
    #     'url': SEQUENTIAL_THINKING_MCP_URL,
    #     'transport': 'streamable_http',
    # }
}