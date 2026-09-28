TRAVEL_INFO = {
    "tokyo": "Tokyo: Shibuya, Asakusa, Senso-ji Temple, and extensive rail transport.",
    "paris": "Paris: Eiffel Tower, Louvre Museum, and Seine River cruises.",
    "london": "London: British Museum, Tower Bridge, and Buckingham Palace.",
}


def retrieve_travel_info(query):
    query_lower = query.lower()
    for city, information in TRAVEL_INFO.items():
        if city in query_lower:
            return information
    return "No matching travel information found."


def calculate_budget(days, daily_budget):
    return f"Estimated basic budget: {days * daily_budget} units for {days} days."
