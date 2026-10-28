from app.planner import (
    create_research_plan,
    generate_search_queries
)

from app.research_agent import research_task
from app.researcher import analyze_research
from app.validation_agent import validate_research
from app.synthesis_agent import synthesize_answer
from app.report_agent import generate_report


# ============================================================
# USER QUERY
# ============================================================

query = input(
    "Enter your research question: "
).strip()


if not query:
    print("ERROR: Research question cannot be empty.")
    raise SystemExit(1)


print("\n" + "=" * 70)
print("FULL RESEARCH + VALIDATION + SYNTHESIS + REPORT TEST")
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
# EXTRACT RESEARCH TASKS
# ============================================================

tasks = []

for line in plan.splitlines():

    line = line.strip()

    if not line:
        continue

    # Remove markdown formatting
    line = line.replace("**", "").strip()

    if not line[0].isdigit():
        continue

    # Accept:
    # 1. Task
    # 2) Task

    if "." in line[:4]:

        task = line.split(".", 1)[1].strip()

    elif ")" in line[:4]:

        task = line.split(")", 1)[1].strip()

    else:

        continue

    if task:
        tasks.append(task)


print(
    f"\nTasks detected: {len(tasks)}"
)


if not tasks:

    print(
        "\nERROR: No research tasks detected."
    )

    raise SystemExit(1)


for i, task in enumerate(
    tasks,
    start=1
):

    print(
        f"{i}. {task}"
    )


# ============================================================
# STORE ALL VALIDATED RESULTS
# ============================================================

validated_results = []


# ============================================================
# STEP 2–5
# RESEARCH + ANALYSIS + VALIDATION
# ============================================================

for task_number, task in enumerate(
    tasks,
    start=1
):

    print("\n" + "=" * 70)
    print(
        f"RESEARCH TASK {task_number}"
    )
    print("=" * 70)

    print(task)


    # ========================================================
    # SEARCH QUERY GENERATION
    # ========================================================

    print("\nSEARCH QUERIES")

    queries = generate_search_queries(
        task
    )

    if not queries:

        print(
            "WARNING: No search queries generated."
        )

        continue


    for query_number, search_query in enumerate(
        queries,
        start=1
    ):

        print(
            f"{query_number}. {search_query}"
        )


    # ========================================================
    # RESEARCH AGENT
    # ========================================================

    print("\n" + "-" * 70)
    print("RESEARCH AGENT")
    print("-" * 70)

    sources = research_task(
        task,
        queries
    )

    print(
        f"Sources collected: {len(sources)}"
    )


    if not sources:

        print(
            "WARNING: No sources found. "
            "Skipping this task."
        )

        continue


    # ========================================================
    # RESEARCH ANALYSIS
    # ========================================================

    print("\n" + "-" * 70)
    print("RESEARCH ANALYSIS")
    print("-" * 70)

    analysis = analyze_research(
        task,
        sources
    )

    print(analysis)


    # ========================================================
    # VALIDATION AGENT
    # ========================================================

    print("\n" + "-" * 70)
    print("VALIDATION AGENT")
    print("-" * 70)

    validation = validate_research(
        task,
        analysis,
        sources
    )

    print(validation)


    # ========================================================
    # SAVE COMPLETE TASK RESULT
    # ========================================================

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
# VALIDATION SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("VALIDATED RESEARCH SUMMARY")
print("=" * 70)

print(
    f"Tasks planned: {len(tasks)}"
)

print(
    f"Tasks successfully validated: "
    f"{len(validated_results)}"
)


if not validated_results:

    print(
        "\nERROR: No validated research results available."
    )

    raise SystemExit(1)


# ============================================================
# SHOW TASK VALIDATION SUMMARY
# ============================================================

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
# STEP 6: FINAL SYNTHESIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 6: FINAL SYNTHESIS")
print("=" * 70)


final_answer = synthesize_answer(
    query,
    validated_results
)


# ============================================================
# FINAL RESEARCH ANSWER
# ============================================================

print("\n" + "=" * 70)
print("FINAL RESEARCH ANSWER")
print("=" * 70)

print(final_answer)


# ============================================================
# STEP 7: REPORT GENERATION
# ============================================================

print("\n" + "=" * 70)
print("STEP 7: REPORT GENERATION")
print("=" * 70)


try:

    report_path = generate_report(
        query,
        final_answer,
        validated_results
    )

    print(
        "\nPDF REPORT GENERATED SUCCESSFULLY"
    )

    print(
        f"Report saved at:\n{report_path}"
    )

except Exception as error:

    print(
        "\nERROR: PDF report generation failed."
    )

    print(
        f"Reason: {error}"
    )


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("FULL RESEARCH PIPELINE COMPLETE")
print("=" * 70)