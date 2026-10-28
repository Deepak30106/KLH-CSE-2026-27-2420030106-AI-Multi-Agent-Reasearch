from app.planner import create_research_plan, generate_search_queries


query = input("Enter your research question: ")

print("\n===== RESEARCH PLAN =====\n")

tasks = create_research_plan(query)

print(tasks)


print("\n===== SEARCH QUERIES =====\n")

for i, task in enumerate(tasks.splitlines(), start=1):

    task = task.split(".", 1)[-1].strip()

    print(f"\n--- TASK {i} ---")
    print(task)

    queries = generate_search_queries(task)

    for j, query in enumerate(queries, start=1):
        print(f"{j}. {query}")