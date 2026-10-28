from crewai import Agent, Task, Crew
city = input("Which city would you like to visit? ")

planner = Agent(
    role="Travel Planner",
    goal="Recommend exactly three interesting places to visit in the city provided by the user.",
    backstory="You are an experienced travel planner who helps first-time visitors discover memorable attractions. You provide concise, practical recommendations with a brief explanation of why each place is worth visiting.",
    verbose=True
)
task = Task(
    description="Recommend exactly 3 places to visit in {city}. "
                "For each place, provide its name, a brief description, "
                "and one practical travel tip.",
    expected_output="Exactly 3 numbered recommendations. "
                    "Each recommendation must include the place name, "
                    "a brief description, and one practical travel tip.",
    agent=planner
)
crew = Crew(
    agents=[planner],
    tasks=[task],
    verbose=True
)
result = crew.kickoff(inputs={"city": city})

print("\nTravel Planner Recommendations:")
print(result)
