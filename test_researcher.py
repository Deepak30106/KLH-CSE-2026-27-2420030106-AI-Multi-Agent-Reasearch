from app.planner import create_research_plan, generate_search_queries
from app.research_agent import research_task
from app.researcher import analyze_research


query = input("Enter your research question: ")

print("\n" + "=" * 70)
print("RESEARCHER AGENT TEST")
print("=" * 70)

print("\nUSER QUERY")
print(query)


# ============================================================
# STEP 1: CREATE RESEARCH PLAN
# ============================================================

plan = create_research_plan(query)

print("\n" + "=" * 70)
print("RESEARCH PLAN")
print("=" * 70)

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


# ============================================================
# STEP 2: SEARCH + ANALYZE
# ============================================================

for i, task in enumerate(tasks, start=1):

    print("\n" + "=" * 70)
    print(f"RESEARCH TASK {i}")
    print("=" * 70)

    print("\nTask:")
    print(task)

    queries = generate_search_queries(task)

    print("\nSearch Queries:")

    for j, search_query in enumerate(queries, start=1):
        print(f"{j}. {search_query}")

    sources = research_task(task, queries)

    print(f"\nSources collected: {len(sources)}")

    # --------------------------------------------------------
    # RESEARCHER ANALYSIS
    # --------------------------------------------------------

    analysis = analyze_research(task, sources)

    print("\n" + "-" * 70)
    print("RESEARCH ANALYSIS")
    print("-" * 70)

    print(analysis)


print("\n" + "=" * 70)
print("RESEARCHER TEST COMPLETE")
print("=" * 70)