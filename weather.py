from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_wheather(location:str)->str:
    """Give the wheather report"""
    return f"Today wheather is rainy {location}"

if __name__=="__main__":
    mcp.run(transport="streamable-http")