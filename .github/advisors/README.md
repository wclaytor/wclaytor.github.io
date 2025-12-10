# Advisors

This directory contains fictional advisor personas used for structured reviews and analysis. Each advisor provides a unique analytical lens informed by established methodologies and thought leaders in their respective domains.

---

## ⚠️ Important Disclaimer

**These advisors are fictional personas.** They are AI-assisted analytical tools that channel specific perspectives and methodologies. They do not represent the actual opinions, endorsements, or reviews of the individuals who inspired them.

When we invoke "The Clarity Advocate," we are not claiming that Steve Krug reviewed our work. We are applying an analytical framework *informed by* the usability principles he has publicly shared.

---

## The Advisory Panel

| Advisor | Alias | Inspired By | Focus Area |
|---------|-------|-------------|------------|
| [The Clarity Advocate](./clarity-advocate.md) | Clara | Steve Krug | First impressions, usability, cognitive load |
| [The Usability Heuristic](./usability-heuristic.md) | Henrik | Jakob Nielsen | Heuristic evaluation, accessibility, UX |
| [The Test-Driven Thinker](./test-driven-thinker.md) | Trent | Kent Beck | Testing, QA, iterative development |
| [The Refactoring Advocate](./refactoring-advocate.md) | Marty | Martin Fowler | Code quality, architecture, maintainability |
| [The Paranoid Sysadmin](./paranoid-sysadmin.md) | Simon | BOFH | Security, infrastructure, risk assessment |

---

## How to Use Advisors

### In Prompts

Reference an advisor to invoke their analytical perspective:

```markdown
Please have The Clarity Advocate (Clara) review this homepage design 
and identify any first-impression issues.
```

```markdown
Ask The Paranoid Sysadmin (Simon) to assess the security posture 
of this PR before we merge.
```

### Multi-Advisor Reviews

For comprehensive reviews, invoke multiple advisors:

```markdown
Please convene the advisory panel to review this PR:
- The Paranoid Sysadmin: Security assessment
- The Refactoring Advocate: Code quality review
- The Clarity Advocate: First impression check
```

### Panel Assessments

For go/no-go decisions, use the structured assessment prompt:
- [Go-Live Assessment Prompt](../.github/prompts/gh-persona-go-live-assessment.prompt.md)

---

## Why Fictional Advisors?

We use advisor personas because:

1. **Structured Thinking** — Each advisor brings a specific analytical framework
2. **Comprehensive Coverage** — Different perspectives catch different issues
3. **Consistent Voice** — The advisor's "personality" creates memorable, actionable feedback
4. **Ethical Clarity** — We're not claiming real people reviewed our work

### What We're Actually Doing

When we ask "The Clarity Advocate" to review something, we are:
- ✅ Applying usability principles from Steve Krug's publicly available work
- ✅ Using a structured framework for first-impression analysis
- ✅ Getting AI-assisted analysis through a specific lens
- ❌ NOT claiming Steve Krug personally reviewed our work
- ❌ NOT representing his actual opinions or endorsements

---

## Advisor Profiles

Each advisor file contains:

- **Identity** — Name, alias, and inspiration source
- **Core Philosophy** — The advisor's fundamental beliefs
- **Review Focus Areas** — What they look for during reviews
- **Typical Advice** — Example feedback in their voice
- **When to Consult** — Situations where this advisor is most valuable
- **Attribution** — Clear acknowledgment of the inspiration source

---

## Persona Source Files

The underlying persona profiles that inform these advisors are located in:

```
.github/personas/
├── bofh/
│   └── bofh.md
├── jakob-nielson/
│   └── jakob-nielsen.md
├── kent-beck/
│   └── kent-beck.md
├── martin-fowler/
│   └── martin-fowler.md
└── steve-krug/
    └── steve-krug.md
```

These contain biographical information and methodology summaries derived from public sources (Wikipedia, published books, articles).

---

## Creating New Advisors

To add a new advisor:

1. Create a persona profile in `.github/personas/[name]/[name].md`
2. Create an advisor file in `.github/advisors/[advisor-name].md`
3. Follow the established template structure
4. Include clear attribution and disclaimers
5. Update this README with the new advisor

### Template Structure

```markdown
# [Advisor Name]

**Alias:** [Short name]
**Inspired by:** [Link to persona profile]
**Focus:** [Primary areas of expertise]

---

## About This Advisor
[Description + disclaimer]

## Core Philosophy
[Key beliefs and principles]

## Review Focus Areas
[What they evaluate]

## Typical Advice
[Example feedback quotes]

## When to Consult This Advisor
[Use cases]

## Attribution
[Clear acknowledgment + disclaimer]
```

---

## Ethical Guidelines

When using advisors:

1. **Never claim real endorsements** — These are analytical tools, not testimonials
2. **Maintain disclaimers** — Always be clear these are fictional personas
3. **Respect the inspiration** — Use their methodologies constructively
4. **Stay current** — Update advisor profiles as methodologies evolve
5. **Be honest** — If asked, explain exactly what these advisors are

---

*The advisory system helps us apply structured thinking to complex problems while being transparent about our methods.*
