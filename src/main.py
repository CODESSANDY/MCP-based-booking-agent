from src.crew import build_crew

def create_booking_crew():
    """
    Initializes and returns the full CrewAI setup
    for the Unified Booking Agent.
    """
    crew = build_crew()
    return crew

if __name__ == "__main__":
    # Example local test
    crew = create_booking_crew()
    result = crew.kickoff(
        inputs={
            "location": "Paris",
            "check_in": "2026-04-10",
            "check_out": "2026-04-15",
            "guests": 2,
            "preferences": "budget-friendly, near Eiffel Tower, free cancellation"
        }
    )
    print(result)
