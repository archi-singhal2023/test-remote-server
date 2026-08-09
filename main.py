from fastmcp import FastMCP
import random, json

mcp = FastMCP("Simple Calculator server")

@mcp.tool
def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b

    """
    return a+b

@mcp.tool
def random_number(min_val: float=1, max_val:float = 100) -> float:
    """Generate a random number within a range.

    Args:
        min_val: Minimum value(default: 1)
        max_val: Maximum value(default: 100)

    Returns:
        float: A random number between min_val and max_val
    """
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server"""
        
    info = {
        "name": "Simple Calculator server",
        "description": "A simple MCP server with math tools",
        "version": "1.0.0",
        "author": "Archi",
        "tools": ["add", "random_number"]
    }

    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)