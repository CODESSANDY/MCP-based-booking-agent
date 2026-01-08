from src.main import create_booking_crew

def run_booking_agent(user_input):
    crew = create_booking_crew()
    result = crew.kickoff(inputs=user_input)
    return result
