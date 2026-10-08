# Research-Quality Writing Benchmark

## Purpose

The Research-Quality Writing Benchmark (RQWB) evaluates AI-assisted research-writing workflows by the quality of the resulting technical communication. It asks whether a workflow helps a reader understand the problem, evidence, mechanism, limitation, and conclusion.

RQWB is not an AI-authorship detector and should not be used to accuse an author of AI use. It does not reward prose merely for avoiding popular AI-associated words. A clear sentence with a necessary technical term is better than a superficially human-sounding sentence that hides the physics.

## Core Question

Given the same source-grounded task, does a writing workflow improve reader understanding and technical defensibility relative to an unassisted AI draft?

## Evaluation Units

Use short, source-grounded cases instead of whole manuscripts. A case contains:

- A task brief with audience, genre, and claim boundary.
- Approved source material, data, equations, figures, or citations.
- A protected reference answer or reviewer notes.
- A prompt and workflow configuration.
- Output text and a blinded score sheet.

Recommended case types are an abstract, introduction paragraph, literature synthesis, equation explanation, methods paragraph, figure discussion, reviewer response, proposal significance paragraph, and technical title.

## Workflow Configurations

Compare workflow configurations, not individual skills as though they perform the same job.

| ID | Configuration | Intended role |
| --- | --- | --- |
| B0 | Baseline AI draft | Establishes the unassisted reference condition. |
| B1 | Pattern and redundancy audit | Identifies generic phrasing, repetition, and avoidable structural habits. |
| B2 | Reader-focused clarity pass | Improves central topic, logical flow, and reader comprehension without changing evidence. |
| B3 | Academic workflow scaffold | Structures research, drafting, review, revision, and verification. |
| B4 | Domain judgment layer | Checks physics, method completeness, evidence, citations, and validity limits. |
| B5 | Integrated workflow | Combines the relevant B1-B4 stages with human author review. |

The exact skill or tool used at each stage must be recorded. A configuration may contain different tools as long as its role is defined before evaluation.

## Corpus Governance

Create three corpus tiers:

| Tier | Permitted material | Release status |
| --- | --- | --- |
| Public | Published papers, public proposals, public talks, open datasets, and synthetic cases. | May be released with attribution and rights checks. |
| Private calibration | Author-approved manuscripts, proposals, reviewer comments, and internal examples. | Local or access-controlled only. Do not publish excerpts, filenames, prompt logs, or identifying metadata. |
| Excluded | Student drafts without explicit permission, sponsor-restricted material, patent-sensitive disclosures, identifiable reviews, and material with unclear rights. | Do not use. |

Private cases can improve an internal workflow, but public benchmark claims must be supported by public or explicitly consented material. Do not allow the model to access a gold reference answer while generating the evaluated draft.

## Blinded Rubric

Use at least two qualified raters when possible. Blind raters to author, model, skill, and configuration. Score each dimension from 1 to 5 and record evidence for scores of 1, 2, 4, or 5.

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Reader focus and logic | No clear point or sequence. | Main point is present but unevenly developed. | Clear central point; each sentence advances the argument. |
| Technical and physical meaning | Lists variables or terms without explaining their role. | Partly explains the governing mechanism. | Explains the relevant mechanism, assumptions, and causal chain. |
| Evidence and claim support | Claims outrun sources, data, or method. | Most claims are bounded, with some ambiguity. | Claims are traceable, properly bounded, and matched to evidence. |
| Specificity and terminology | Generic labels, vague verbs, or unexplained coined phrases obscure meaning. | Usually specific, with a few weak terms. | Uses familiar, precise terms that carry the intended technical meaning. |
| Economy and non-redundancy | Repeats setup, result, or implication. | Some duplication remains. | Each sentence has a distinct job; no avoidable restatement. |
| Genre fitness | Does not serve the abstract, methods, results, or proposal purpose. | Mostly appropriate for the genre. | Meets the genre's decision and reader needs. |
| Revision actionability | Does not help an author decide what to change. | Gives some usable changes. | Identifies the issue, why it matters, a concrete revision, and needed evidence. |

For mentoring workflows, score constructive tone and boundary discipline separately. For citation-heavy tasks, add citation placement and source-intent accuracy. For equations or figures, add mechanism fidelity and caption or narrative completeness.

## Required Checks

Before scoring, confirm that:

1. All configurations received the same approved source packet and task constraints.
2. The output did not introduce unsupported numerical values, citations, results, or mechanisms.
3. The final text preserves units, equations, sample sizes, uncertainty statements, and claim strength unless a source-grounded correction is documented.
4. Raters do not know which workflow generated an output.
5. A human author can reject or revise every proposed change.

## Analyses

For each configuration, report median and distribution for each rubric dimension, rater agreement, unsupported-claim count, citation or source errors, and human editing time. Do not collapse the benchmark into a single score unless the weighting is preregistered and sensitivity-tested.

Compare B5 with B0 first. Then use ablations, such as B5 without domain review or without clarity review, to identify what each stage contributes. Interpret small score differences cautiously when rater agreement is low or case count is limited.

## Figures And Tables

Use visuals that explain the workflow rather than implying false precision:

1. **Annotated before-and-after case**: show a short source-grounded excerpt, the baseline draft, revised draft, and comments tied to the rubric.
2. **Dimension profile**: grouped bars or dot-and-interval plots for rubric dimensions. Show individual cases or confidence intervals where sample size permits.
3. **Workflow ablation matrix**: rows are case types, columns are configurations, and cells show median score and evidence-error count.
4. **Issue taxonomy**: stacked bars showing the fraction of cases with unsupported claims, variable-listing equation descriptions, redundant restatement, vague terminology, or misplaced citations.
5. **Cost-quality plot**: human editing time versus reader-focus or evidence score. Report model, version, prompting, and run conditions.

Avoid radar charts when values are ordinal or sample sizes are small. Avoid a generic "AI score" because it obscures the actual writing problem.

## Reporting Language

Use terms such as "research-quality writing," "reader-centered technical writing," and "evidence-and-mechanism writing." Avoid describing a workflow as making text "human" or "undetectable." The benchmark evaluates communication quality, not authorship.

## Minimum Viable Study

Start with 12 cases: two each for literature synthesis, equation explanation, figure discussion, abstract, proposal narrative, and reviewer response. Use B0 and B5 for the first comparison, two blinded raters, and a short author debrief after scoring.

Release only the protocol, synthetic or public cases, prompts, model metadata, de-identified score sheets, and analysis code. Keep private calibration materials local.
