from app.planner import create_research_plan, generate_search_queries
from app.research_agent import research_task
from app.researcher import analyze_research
from app.validation_agent import validate_research


# ============================================================
# USER QUERY
# ============================================================

query = input("Enter your research question: ").strip()


print("\n" + "=" * 70)
print("VALIDATION AGENT INTEGRATION TEST")
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
# STEP 2: EXTRACT TASKS
# ============================================================

tasks = []

for line in plan.splitlines():

    line = line.strip()

    if not line:
        continue

    # Accept:
    # 1. Task
    # 2) Task
    # 3. **Task**
    if line[0].isdigit():

        if "." in line[:4]:
            task = line.split(".", 1)[1].strip()

        elif ")" in line[:4]:
            task = line.split(")", 1)[1].strip()

        else:
            continue

        # Remove Markdown formatting
        task = task.replace("**", "").strip()

        if task:
            tasks.append(task)


print("\nTasks detected:", len(tasks))

for i, task_item in enumerate(tasks, start=1):
    print(f"{i}. {task_item}")


# ============================================================
# SAFETY CHECK
# ============================================================

if not tasks:

    print("\nERROR: No research tasks detected.")

    print("\nFull planner output:")
    print(plan)

    raise SystemExit(1)


# ============================================================
# TEST FIRST TASK ONLY
# ============================================================

task = tasks[0]


print("\n" + "=" * 70)
print("STEP 2: VALIDATION TEST TASK")
print("=" * 70)

print(task)


# ============================================================
# STEP 3: GENERATE SEARCH QUERIES
# ============================================================

print("\n" + "=" * 70)
print("STEP 3: SEARCH QUERY GENERATION")
print("=" * 70)

queries = generate_search_queries(task)

for i, query_text in enumerate(queries, start=1):
    print(f"{i}. {query_text}")


# ============================================================
# STEP 4: RESEARCH
# ============================================================

print("\n" + "=" * 70)
print("STEP 4: RESEARCH AGENT")
print("=" * 70)

sources = research_task(
    task,
    queries
)

print(f"\nSources collected: {len(sources)}")


# ============================================================
# SAFETY CHECK
# ============================================================

if not sources:

    print("\nWARNING: No sources were collected.")

    print("Validation cannot be meaningfully performed.")

    raise SystemExit(1)


# ============================================================
# STEP 5: RESEARCH ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 5: RESEARCH ANALYSIS")
print("=" * 70)

analysis = analyze_research(
    task,
    sources
)

print(analysis)


# ============================================================
# STEP 6: VALIDATION AGENT
# ============================================================

print("\n" + "=" * 70)
print("STEP 6: VALIDATION AGENT")
print("=" * 70)

validation = validate_research(
    task,
    analysis,
    sources
)


print("\n" + "=" * 70)
print("VALIDATION RESULTS")
print("=" * 70)

print(validation)


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("VALIDATION INTEGRATION TEST COMPLETE")
print("=" * 70)