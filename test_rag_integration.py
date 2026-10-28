from app.planner import (
    create_research_plan,
    generate_search_queries
)

from app.research_agent import research_task

from app.source_filter import filter_sources

from app.rag_agent import hybrid_search


print("=" * 70)
print("REAL SOURCE RAG INTEGRATION TEST")
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
# EXTRACT FIRST RESEARCH TASK
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

    raise RuntimeError(
        "No research tasks were generated."
    )


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


for i, search_query in enumerate(
    queries,
    start=1
):

    print(
        f"{i}. {search_query}"
    )


# ============================================================
# REAL WEB RESEARCH
# ============================================================

sources = research_task(
    task,
    queries
)


print("\n" + "=" * 70)
print("ORIGINAL WEB SOURCES")
print("=" * 70)

print(
    f"Sources collected: {len(sources)}"
)


# ============================================================
# SOURCE QUALITY FILTER
# ============================================================

filtered_sources = filter_sources(
    sources
)


print("\n" + "=" * 70)
print("SOURCE QUALITY FILTER")
print("=" * 70)

print(
    f"Original sources: {len(sources)}"
)

print(
    f"Filtered sources: {len(filtered_sources)}"
)


# ============================================================
# DISPLAY FILTERED SOURCES
# ============================================================

print("\n" + "=" * 70)
print("QUALITY SOURCES")
print("=" * 70)


for i, source in enumerate(
    filtered_sources,
    start=1
):

    print(
        f"\n{i}. "
        f"{source.get('title', 'No title')}"
    )

    print(
        f"Quality score: "
        f"{source.get('quality_score', 0)}"
    )

    print(
        f"URL: "
        f"{source.get('url', '')}"
    )


# ============================================================
# HYBRID RAG
# ============================================================

results = hybrid_search(
    task,
    filtered_sources,
    top_k=5
)


print("\n" + "=" * 70)
print("HYBRID RAG RESULTS")
print("=" * 70)


for i, result in enumerate(
    results,
    start=1
):

    print(
        f"\n{i}. "
        f"{result.get('title', 'No title')}"
    )

    print(
        f"Vector score: "
        f"{result.get('vector_score', 0)}"
    )

    print(
        f"Keyword score: "
        f"{result.get('keyword_score', 0)}"
    )

    print(
        f"Hybrid score: "
        f"{result.get('hybrid_score', 0)}"
    )

    print(
        f"Quality score: "
        f"{result.get('quality_score', 0)}"
    )

    print(
        f"URL: "
        f"{result.get('url', '')}"
    )


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("RAG INTEGRATION TEST COMPLETE")
print("=" * 70)