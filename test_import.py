import sys
print("Python paths:")
for path in sys.path:
    print(f"  {path}")

print("\nTrying to import:")
try:
    from mcp.mcp_layer import MCPBookingLayer
    print("SUCCESS: mcp.mcp_layer imported!")
except ImportError as e:
    print(f"FAILED: {e}")

try:
    from mcp_layer import MCPBookingLayer
    print("SUCCESS: mcp_layer imported!")
except ImportError as e:
    print(f"FAILED: {e}")