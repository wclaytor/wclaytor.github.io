# Tutorial Design Patterns

Best practices for creating effective, hands-on tutorials that help users master skills.

## Core Tutorial Principles

### 1. Learning by Doing
- Always include practical exercises, not just theory
- Users should build something concrete during the tutorial
- Each concept should be immediately applied to their project

### 2. Progressive Complexity
- Start with the simplest use case
- Gradually introduce more advanced features
- Build on previously learned concepts

### 3. Real-World Context
- Connect to user's actual project goals
- Use realistic examples, not toy problems
- Show how the skill solves real problems

### 4. Immediate Feedback
- Include checkpoints to verify understanding
- Provide ways to test each step
- Show expected outputs clearly

## Tutorial Structure Template

### Phase 1: Foundation (15-20% of tutorial)
**Goal:** Understand what the skill does and when to use it

1. **Skill Overview**
   - What problem does this skill solve?
   - When should you use it vs. alternatives?
   - Key concepts and terminology

2. **Prerequisites Check**
   - Required tools or dependencies
   - Baseline knowledge needed
   - Environment setup if needed

3. **First Success**
   - Simplest possible example that works
   - Builds confidence immediately
   - "Hello World" equivalent for the skill

### Phase 2: Core Concepts (40-50% of tutorial)
**Goal:** Master the fundamental features

1. **Essential Workflows**
   - Most common use cases (80/20 rule)
   - Step-by-step walkthroughs
   - Code examples with explanations

2. **Hands-On Exercise**
   - Apply concepts to user's project
   - Guided but with some creative freedom
   - Verify results at each step

3. **Common Patterns**
   - Idioms and best practices
   - Typical configurations
   - When to use each approach

### Phase 3: Practical Application (30-40% of tutorial)
**Goal:** Build something meaningful for the user's project

1. **Project Integration**
   - Choose a specific task in their project
   - Plan the implementation
   - Execute with skill guidance

2. **Iterative Improvement**
   - Start with basic version
   - Add features incrementally
   - Refine based on results

3. **Troubleshooting & Tips**
   - Common pitfalls and solutions
   - Debugging strategies
   - Performance considerations

### Phase 4: Next Steps (5-10% of tutorial)
**Goal:** Empower continued learning

1. **Advanced Features**
   - Brief overview of what else is possible
   - Point to relevant documentation
   - Suggest natural next projects

2. **Resources & References**
   - Where to find help
   - Related skills or tools
   - Community resources

## Pedagogical Techniques

### Scaffolding
- Provide more guidance early, gradually reduce support
- Use templates/examples that users modify
- Start with complete code, then have users write from scratch

### Explanatory Examples
```markdown
**Good example pattern:**
"Let's create a PDF report from data. Here's how:

```python
# This code extracts data and generates a PDF
import pdfplumber
# [code with inline comments explaining each part]
```

Notice how we [key insight about the code]."
```

### Checkpoint Questions
- "Before moving on, verify your output looks like [expected result]"
- "Can you explain why we used [X] instead of [Y]?"
- "Try modifying [parameter] - what changes?"

### Common Mistakes Section
Proactively address typical errors:
- "If you see [error message], it means [cause]. Fix it by [solution]."
- "Don't forget to [crucial step] or you'll get [problem]."

## Tutorial Tone & Style

### Writing Style
- **Conversational but precise**: "Now we'll..." not "Now one must..."
- **Active voice**: "Create a file" not "A file should be created"
- **Direct address**: "You'll notice" not "Users will notice"
- **Encouraging**: Celebrate small wins, normalize mistakes

### Code Comments
- Explain WHY, not just WHAT
- Highlight non-obvious details
- Note common modifications users might want

### Visual Markers
Use markdown effectively:
- `**Important:**` for critical information
- `**Note:**` for helpful context
- `**Warning:**` for potential pitfalls
- `**Tip:**` for pro techniques

## Adaptation Guidelines

### For Simple Skills
- Can combine phases 1-2 into "Quick Start"
- Focus on single comprehensive example
- Emphasize variations and customization

### For Complex Skills
- May need multiple tutorials (beginner, intermediate, advanced)
- Break into smaller sub-skills if needed
- Provide decision trees for choosing approaches

### For Creative Skills (design, art)
- Emphasize exploration and experimentation
- Show multiple valid approaches
- Focus on developing taste and judgment

### For Technical Skills (APIs, tools)
- Include reference-style sections
- Emphasize debugging and troubleshooting
- Show error handling patterns

## Success Criteria

A successful tutorial achieves:
- ✅ User completes a working implementation for their project
- ✅ User understands core concepts, not just copying code
- ✅ User feels confident to explore skill independently
- ✅ User can troubleshoot common issues
- ✅ User knows where to find help for advanced features
