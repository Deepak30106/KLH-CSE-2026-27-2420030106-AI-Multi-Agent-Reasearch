from app.planner import (
    create_research_plan,
    generate_search_queries,
)

from app.research_agent import ResearchAgent


def run_research_pipeline(query: str):

    print("\n" + "=" * 80)
    print("AI MULTI-AGENT RESEARCH ASSISTANT")
    print("=" * 80)

    print("\nUSER QUERY")
    print(query)

    # -------------------------------------------------
    # STEP 1: PLANNER AGENT
    # -------------------------------------------------

    print("\n" + "=" * 80)
    print("STEP 1: PLANNER AGENT")
    print("=" * 80)

    plan = create_research_plan(query)

    print(plan)

    # -------------------------------------------------
    # STEP 2: EXTRACT RESEARCH TASKS
    # -------------------------------------------------

    tasks = []

    for line in plan.splitlines():

        line = line.strip()

        if not line:
            continue

        if line[0].isdigit() and "." in line:

            task = line.split(".", 1)[1].strip()

            if task:
                tasks.append(task)

    print("\nTasks detected:", len(tasks))

    # -------------------------------------------------
    # STEP 3: RESEARCH EACH TASK
    # -------------------------------------------------

    research_agent = ResearchAgent()

    all_results = []

    for task_number, task in enumerate(tasks, start=1):

        print("\n" + "=" * 80)
        print(f"STEP 2: RESEARCH TASK {task_number}")
        print("=" * 80)

        print("\nTask:")
        print(task)

        # Generate search queries
        search_queries = generate_search_queries(task)

        print("\nSearch Queries:")

        for i, query_text in enumerate(search_queries, start=1):
            print(f"{i}. {query_text}")

        # Search web
        result = research_agent.research(
            task=task,
            search_queries=search_queries,
        )

        all_results.append(result)

    # -------------------------------------------------
    # FINAL OUTPUT
    # -------------------------------------------------

    print("\n" + "=" * 80)
    print("PIPELINE COMPLETE")
    print("=" * 80)

    total_sources = sum(
        result["source_count"]
        for result in all_results
    )

    print("\nResearch tasks:", len(all_results))
    print("Total sources collected:", total_sources)


if __name__ == "__main__":

    user_query = input(
        "\nEnter your research question: "
    ).strip()

    if not user_query:
        print("Please enter a research question.")
    else:
        run_research_pipeline(user_query)