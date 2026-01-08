from crewai.tools import tool
from mcp.mcp_layer import MCPBookingLayer

@tool("MCPBookingTool")
def mcp_booking_tool(location: str, check_in: str, check_out: str, guests: int) -> str:
    """
    Aggregates accommodation listings from Booking.com and Amadeus.
    """
    mcp = MCPBookingLayer()
    results = mcp.search_all(location, check_in, check_out, guests)
    return str(results)
