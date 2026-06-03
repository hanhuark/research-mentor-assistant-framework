# Validation

Validation checks whether the assistant provides useful, accurate, and appropriately bounded feedback.

## Evaluation Questions

- Does the assistant identify the same major issues a mentor would identify?
- Does it miss important technical or logical problems?
- Does it over-comment on minor style issues?
- Does it invent unsupported claims or citations?
- Does it distinguish first-pass feedback from final approval?
- Does it protect confidential examples?
- Does it give students actionable next steps?

## Test Set

Create a small validation set with:

- Strong examples.
- Weak examples with known issues.
- Drafts with unclear gaps.
- Figures with weak interpretation.
- Overly broad literature reviews.
- Text-heavy slides.
- Data-analysis plans with parameter sweeps but no hypothesis.
- Code or notebooks with reproducibility problems.

## Review Process

1. Run the assistant on each test item.
2. Compare output with human mentor comments or an expert rubric.
3. Classify comments as correct, useful but incomplete, low-priority, wrong, or unsafe.
4. Update the guidance.
5. Re-test after major revisions.

## Success Criteria

The assistant should reliably catch high-level logic and research-quality issues, provide concrete revision paths, and clearly flag decisions that need human mentor judgment.
