from tools import calculate_budget, retrieve_travel_info


def run_agent(query):
    query_lower = query.lower()

    if "budget" in query_lower or "cost" in query_lower:
        return calculate_budget(5, 100)

    if any(word in query_lower for word in ["visit", "attraction", "tokyo", "paris", "london"]):
        return retrieve_travel_info(query)

    return "The agent does not know which tool to use yet."


if __name__ == "__main__":
    print(run_agent("What should I visit in Tokyo?"))
    print(run_agent("What is my estimated budget?"))
