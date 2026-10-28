from app.planner import create_research_plan, generate_search_queries
from app.research_agent import research_task
from app.source_filter import filter_sources


print("=" * 70)
print("REAL SOURCE FILTER TEST")
print("=" * 70)


# ============================================================
# USER QUERY
# ============================================================

query = input("\nEnter your research question: ")

print("\nUSER QUERY")
print(query)


# ============================================================
# CREATE RESEARCH PLAN
# ============================================================

plan = create_research_plan(query)

print("\n" + "=" * 70)
print("RESEARCH PLAN")
print("=" * 70)

print(plan)


# ============================================================
# EXTRACT FIRST TASK
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


if not tasks:
    raise RuntimeError("No research tasks were generated.")


task = tasks[0]

print("\n" + "=" * 70)
print("RESEARCH TASK")
print("=" * 70)

print(task)


# ============================================================
# GENERATE SEARCH QUERIES
# ============================================================

queries = generate_search_queries(task)

print("\n" + "=" * 70)
print("SEARCH QUERIES")
print("=" * 70)

for i, search_query in enumerate(queries, start=1):

    print(f"{i}. {search_query}")


# ============================================================
# REAL WEB RESEARCH
# ============================================================

sources = research_task(
    task,
    queries
)

print("\n" + "=" * 70)
print("ORIGINAL SOURCES")
print("=" * 70)

print(f"Sources collected: {len(sources)}")


# ============================================================
# SOURCE FILTER
# ============================================================

filtered_sources = filter_sources(
    sources
)

print("\n" + "=" * 70)
print("FILTERED SOURCES")
print("=" * 70)

print(f"Sources after filtering: {len(filtered_sources)}")


# ============================================================
# DISPLAY RESULTS
# ============================================================

for i, source in enumerate(
    filtered_sources,
    start=1
):

    print(f"\n{i}. {source.get('title', 'No title')}")

    print(
        f"Quality score: "
        f"{source.get('quality_score', 0)}"
    )

    print(
        f"URL: "
        f"{source.get('url', '')}"
    )


print("\n" + "=" * 70)
print("REAL SOURCE FILTER TEST COMPLETE")
print("=" * 70)