from app.planner import create_research_plan, generate_search_queries
from app.research_agent import research_task


query = input("Enter your research question: ")

print("\n" + "=" * 70)
print("AI MULTI-AGENT RESEARCH ASSISTANT")
print("=" * 70)

print("\nUSER QUERY")
print(query)


# ============================================================
# STEP 1: PLANNER AGENT
# ============================================================

print("\n" + "=" * 70)
print("STEP 1: PLANNER AGENT")
print("=" * 70)

plan = create_research_plan(query)

print(plan)


# ============================================================
# EXTRACT TASKS
# ============================================================

tasks = []

for line in plan.splitlines():

    line = line.strip()

    if not line:
        continue

    if line[0].isdigit() and "." in line:

        task = line.split(".", 1)[1].strip()

        if task:
            tasks.append(task)


print(f"\nTasks detected: {len(tasks)}")


# ============================================================
# STEP 2: SEARCH QUERY GENERATION + RESEARCH
# ============================================================

all_sources = []

for i, task in enumerate(tasks, start=1):

    print("\n" + "=" * 70)
    print(f"STEP 2: RESEARCH TASK {i}")
    print("=" * 70)

    print("\nTask:")
    print(task)

    queries = generate_search_queries(task)

    print("\nSearch Queries:")

    for j, query_text in enumerate(queries, start=1):
        print(f"{j}. {query_text}")

    sources = research_task(task, queries)

    all_sources.extend(sources)


# ============================================================
# PIPELINE COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("PIPELINE COMPLETE")
print("=" * 70)

print(f"\nResearch tasks: {len(tasks)}")
print(f"Total sources collected: {len(all_sources)}")