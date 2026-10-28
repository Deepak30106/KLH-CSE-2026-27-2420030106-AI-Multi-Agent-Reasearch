from app.synthesis_agent import synthesize_answer


# ============================================================
# SYNTHESIS AGENT TEST
# ============================================================

print("=" * 70)
print("SYNTHESIS AGENT TEST")
print("=" * 70)


# ============================================================
# USER QUERY
# ============================================================

query = input(
    "\nEnter your research question: "
).strip()


if not query:

    print(
        "\nERROR: Research question cannot be empty."
    )

    raise SystemExit(1)


print("\nUSER QUERY")
print(query)


# ============================================================
# SAMPLE VALIDATED RESEARCH
# ============================================================
#
# This is ONLY a test for the Synthesis Agent.
#
# We are intentionally not running the complete research
# pipeline here because that was already tested successfully.
#
# In the real pipeline, this data comes from:
#
# Planner
#    ↓
# Research
#    ↓
# Analysis
#    ↓
# Validation
#    ↓
# Synthesis
#
# ============================================================

validated_results = [

    {
        "task_number": 1,

        "task": (
            "Investigate the origin and creation of "
            "Shinchan."
        ),

        "analysis": """
RESEARCH FINDINGS

The collected research discusses the origin and creation
of Shinchan and identifies the manga and its creator.

The available evidence provides information about the
beginning of the character and the series.
""",

        "validation": """
VALIDATION RESULTS

Claims Checked:

1. Shinchan's origin and creation are discussed in
   the collected sources. — SUPPORTED

Evidence Issues:

1. The available evidence does not provide every
   historical detail about the series.

Overall Confidence:
Medium
""",

        "sources": [
            {
                "title": "Shinchan Origin and Creation",
                "url": "",
                "snippet": (
                    "The source provides information about "
                    "the origin and creation of Shinchan."
                )
            }
        ]
    },


    {
        "task_number": 2,

        "task": (
            "Analyze Shinchan's personality, traits, "
            "family and relationships."
        ),

        "analysis": """
RESEARCH FINDINGS

The collected evidence discusses Shinchan's personality,
behavior, family relationships and interactions with
other characters.

The evidence describes the character's humorous,
mischievous and distinctive behavior.
""",

        "validation": """
VALIDATION RESULTS

Claims Checked:

1. Shinchan's personality and relationships are discussed
   in the collected evidence. — SUPPORTED

2. Some personality interpretations have limited evidence.
   — PARTIALLY SUPPORTED

Evidence Issues:

1. Some sources provide limited character analysis.

Overall Confidence:
Medium
""",

        "sources": [
            {
                "title": "Shinchan Character and Personality",
                "url": "",
                "snippet": (
                    "The source discusses Shinchan's personality, "
                    "behavior and relationships."
                )
            }
        ]
    },


    {
        "task_number": 3,

        "task": (
            "Examine Shinchan's role in the story and "
            "his interactions with other characters."
        ),

        "analysis": """
RESEARCH FINDINGS

The evidence discusses Shinchan's role as the central
character and his interactions with his family,
friends and other characters.
""",

        "validation": """
VALIDATION RESULTS

Claims Checked:

1. Shinchan is the central character of the story.
   — SUPPORTED

2. His interactions with family and other characters
   are important to the narrative. — SUPPORTED

Overall Confidence:
Medium
""",

        "sources": [
            {
                "title": "Shinchan Story and Characters",
                "url": "",
                "snippet": (
                    "The source discusses Shinchan's role "
                    "and interactions with other characters."
                )
            }
        ]
    },


    {
        "task_number": 4,

        "task": (
            "Research Shinchan's cultural impact, popularity "
            "and adaptations."
        ),

        "analysis": """
RESEARCH FINDINGS

The collected evidence discusses Shinchan's popularity,
cultural presence and adaptations in different media.
""",

        "validation": """
VALIDATION RESULTS

Claims Checked:

1. Shinchan has had cultural popularity and media
   adaptations. — SUPPORTED

Evidence Issues:

1. The available evidence does not provide complete
   information about worldwide cultural impact.

Overall Confidence:
Medium
""",

        "sources": [
            {
                "title": "Shinchan Cultural Impact",
                "url": "",
                "snippet": (
                    "The source discusses Shinchan's popularity "
                    "and cultural impact."
                )
            }
        ]
    }

]


# ============================================================
# SYNTHESIS
# ============================================================

print("\n" + "=" * 70)
print("SYNTHESIZING RESEARCH")
print("=" * 70)


try:

    answer = synthesize_answer(
        query=query,
        validated_results=validated_results
    )


except Exception as error:

    print("\nSYNTHESIS ERROR")
    print(error)

    raise SystemExit(1)


# ============================================================
# FINAL ANSWER
# ============================================================

print("\n" + "=" * 70)
print("FINAL SYNTHESIZED ANSWER")
print("=" * 70)

print(answer)


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("SYNTHESIS AGENT TEST COMPLETE")
print("=" * 70)