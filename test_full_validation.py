from app.planner import create_research_plan, generate_search_queries
from app.research_agent import research_task
from app.researcher import analyze_research
from app.validation_agent import validate_research


# ============================================================
# USER QUERY
# ============================================================

query = input("Enter your research question: ").strip()


print("\n" + "=" * 70)
print("FULL VALIDATION PIPELINE TEST")
print("=" * 70)

print("\nUSER QUERY")
print(query)


# ============================================================
# STEP 1: PLANNER
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

    if line[0].isdigit():

        if "." in line[:4]:
            task = line.split(".", 1)[1].strip()

        elif ")" in line[:4]:
            task = line.split(")", 1)[1].strip()

        else:
            continue

        task = task.replace("**", "").strip()

        if task:
            tasks.append(task)


print("\nTasks detected:", len(tasks))


if not tasks:
    print("ERROR: No research tasks detected.")
    raise SystemExit(1)


for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")


# ============================================================
# STORE ALL VALIDATED RESULTS
# ============================================================

validated_results = []


# ============================================================
# PROCESS EVERY TASK
# ============================================================

for task_number, task in enumerate(tasks, start=1):

    print("\n" + "=" * 70)
    print(f"RESEARCH TASK {task_number}")
    print("=" * 70)

    print(task)


    # --------------------------------------------------------
    # SEARCH QUERY GENERATION
    # --------------------------------------------------------

    print("\nSEARCH QUERIES")

    queries = generate_search_queries(task)

    for i, search_query in enumerate(queries, start=1):
        print(f"{i}. {search_query}")


    # --------------------------------------------------------
    # RESEARCH
    # --------------------------------------------------------

    print("\n" + "-" * 70)
    print("RESEARCH AGENT")
    print("-" * 70)

    sources = research_task(
        task,
        queries
    )

    print(f"\nSources collected: {len(sources)}")


    if not sources:
        print("WARNING: No sources found for this task.")
        continue


    # --------------------------------------------------------
    # RESEARCH ANALYSIS
    # --------------------------------------------------------

    print("\n" + "-" * 70)
    print("RESEARCH ANALYSIS")
    print("-" * 70)

    analysis = analyze_research(
        task,
        sources
    )

    print(analysis)


    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    print("\n" + "-" * 70)
    print("VALIDATION AGENT")
    print("-" * 70)

    validation = validate_research(
        task,
        analysis,
        sources
    )

    print(validation)


    # --------------------------------------------------------
    # STORE RESULT
    # --------------------------------------------------------

    validated_results.append(
        {
            "task_number": task_number,
            "task": task,
            "queries": queries,
            "sources": sources,
            "analysis": analysis,
            "validation": validation
        }
    )


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("FULL VALIDATION SUMMARY")
print("=" * 70)

print(
    f"Tasks planned: {len(tasks)}"
)

print(
    f"Tasks successfully validated: {len(validated_results)}"
)


for result in validated_results:

    print("\n" + "-" * 70)

    print(
        f"TASK {result['task_number']}"
    )

    print(
        result["task"]
    )

    print(
        f"Sources: {len(result['sources'])}"
    )

    print(
        "Validation completed: YES"
    )


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("FULL VALIDATION PIPELINE TEST COMPLETE")
print("=" * 70)