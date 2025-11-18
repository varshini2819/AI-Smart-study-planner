# AI-Smart-study-planner
A Multi-Agent Smart Study Planner: ingests syllabus &amp; deadlines, auto-plans an adaptive study schedule, generates quizzes, tracks performance to discover weak topics, and continuously optimizes the plan using long-term memory and observability.

# What it is
StudyMate creates adaptive study schedules, generates quizzes, grades answers, stores learner history, and rebalances plans to focus on weak areas.

# Features
- Planner Agent: creates topic-based schedules from syllabus + deadlines.
- Quiz Generator Agent: generates MCQs & short-answer questions per topic.
- Grader Agent: auto-grades and computes mastery.
- Memory Bank: stores performance across sessions.
- Observability: logs and metrics for progress & time.

**Problem:** Students waste time planning and studying inefficiently; curricula are large and one-size-fits-all schedules don’t adapt to how students actually perform.

**Solution:** StudyMate is a multi-agent system that creates personalized study plans, generates targeted quizzes, monitors performance, and rebalances study time automatically based on memory of past weaknesses. It accepts syllabus files/URLs, deadlines, and the user’s available hours.

**Value**: Reduces planning time, improves learning efficiency by focusing on weak areas, and provides traceable metrics (progress, mastery). Judges will see clear use of agents, memory, tools, observability, and deployment (Agent Engine) — covering the feature requirements and bonus points.

**Key differentiators:**

Multi-agent pipeline (planner, quiz generator, evaluator, insights, memory) with loop/iteration until mastery.

Long-term memory allowing cross-course learning and persistent learner model.

Execution tool integration (code execution for auto-grading multiple choice / short answer via tests).

Easy demo: upload syllabus → watch plan + quiz + automated plan adjustments.

