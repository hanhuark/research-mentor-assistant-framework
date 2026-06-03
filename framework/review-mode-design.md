# Review Mode Design

Review modes make the assistant predictable. Each mode should define the input, review priorities, output format, and boundaries.

## Recommended Modes

### Pre-Mentor Review

Use before a student sends work to the mentor. Focus on major issues first: unclear objective, weak gap, missing evidence, unsupported claims, poor figure logic, incomplete methods, or lack of physical reasoning.

### Paper Section Review

Review introductions, literature reviews, methods, modeling sections, results/discussion, abstracts, and conclusions. Require each paragraph to have a central topic and a logical connection to surrounding paragraphs.

### Literature Review Review

Check whether the review tells the author's own story, groups work by mechanism or question, cites selectively, acknowledges background references professionally, and motivates the knowledge gap.

### Figure And Results Review

Review figures using four levels: description, observation, physical explanation, and comparison with existing work.

### Data Analysis And DOE Review

Check whether the work has a strong baseline case, detailed analysis of that case, and hypothesis-driven experiment or simulation design.

### Proposal Review

Check solicitation fit, reviewer criteria, significance, innovation, preliminary results, technical approach, risks, milestones, and broader impact.

### Slide And Poster Review

Check whether the audience can anticipate the next slide, whether content blocks are visually separated, whether figures carry the story, and whether text is limited to essential messages.

### Code And Reproducibility Review

Check whether scripts, notebooks, plots, simulation setup, data paths, dependencies, and outputs are reproducible and understandable by future group members.

## Output Format

Use a consistent structure:

- **Major Comments**: Problems that affect logic, validity, contribution, or reviewer understanding.
- **Specific Suggestions**: Concrete fixes tied to sections, figures, tables, slides, or code files.
- **Minor Comments**: Style, wording, formatting, or small clarity issues.
- **Questions For The Human Mentor**: Decisions that require advisor judgment.
- **Readiness**: A concise assessment of whether the work is ready to share, revise, or submit.
