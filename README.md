# Research Mentor Assistant Framework

A framework for converting documented research mentoring practices into transparent, updateable AI assistants that provide first-pass feedback on academic writing, literature review, figures, data analysis, coding, presentations, and proposals.

The goal is not to clone an advisor or replace human mentoring. The goal is to help students and researchers receive structured preliminary feedback before meetings, revisions, submissions, or reviews.

## Why This Exists

Research mentoring often relies on tacit knowledge: how an advisor comments on introductions, how a lab discusses figures, how proposals are structured, how data analysis is expected to justify a claim, and how slides should guide an audience. These expectations are usually learned slowly through repeated feedback.

This framework turns those expectations into reusable, inspectable guidance. A mentor assistant should make hidden standards easier to learn while keeping final scientific judgment with the human mentor, research group, and review process.

## What The Framework Produces

A research mentor assistant can support:

- First-pass manuscript and section reviews.
- Critical literature review feedback.
- Figure and results-discussion review.
- Hypothesis-driven data-analysis and DOE feedback.
- Proposal narrative and review-criteria feedback.
- Presentation and poster feedback.
- Research code and reproducibility review.
- Pre-meeting preparation for students.

## Core Principle

Use a mentor assistant as a calibrated review layer, not as an authority.

It should say: "I provide first-pass feedback based on documented mentoring guidance and examples. Final research direction, approval, authorship, submission, and scientific judgment remain with the human mentor and research team."

## Framework Workflow

1. **Collect Mentor Signals**
   Gather approved examples of papers, proposals, slides, comments, rubrics, coding expectations, and advising notes.

2. **Extract Reusable Principles**
   Convert examples into explicit guidance for logic flow, evidence use, figure discussion, methodology detail, proposal structure, slide design, and review tone.

3. **Separate General Practice From Local Preference**
   Distinguish universal research quality standards from mentor-specific habits, lab-specific workflows, and domain-specific judgment.

4. **Design Review Modes**
   Create task-specific modes such as paper review, proposal review, slide review, data-analysis review, code review, and pre-advisor review.

5. **Add Guardrails**
   Prevent impersonation, protect confidential material, require uncertainty labeling, and keep the assistant's role as first-pass feedback.

6. **Validate Against Human Feedback**
   Compare assistant comments with real mentor comments, identify missed issues and false positives, and revise the guidance.

7. **Package And Iterate**
   Publish the framework, templates, and seed implementation in a version-controlled repository so the assistant can evolve.

## Repository Structure

```text
framework/
  mentor-signal-collection.md
  principle-extraction.md
  review-mode-design.md
  guardrails.md
  validation.md
templates/
  mentor-profile-template.md
  student-facing-disclaimer.md
  review-rubric-template.md
  skill-template/
  agent-profile-template/
examples/
  thermal-fluid-research-mentor/
docs/
  privacy-and-consent.md
  adapting-to-a-new-lab.md
  evaluation-plan.md
```

## Seed Implementation

The first seed implementation is the [Thermal-Fluid Research Workflow](https://github.com/hanhuark/mechanical-engineering-research-skill), a mechanical engineering research assistant built from documented guidance on technical writing, literature review, thermal-fluid data analysis, presentations, proposals, coding, and research workflows.

This seed is an example of the framework, not the framework itself. Other mentors, labs, and disciplines should replace the seed materials with their own approved examples and standards.

## License

This project is released under the MIT License.
