---
epic:
  title: "Epic: [Your Epic Title Here]"
  labels: ["epic"]  # Add relevant labels: "feature", "enhancement", "infrastructure", etc.
  milestone: ""  # Optional: "Sprint 1", "Q1 2025", "Version 1.0", etc.
  description: |
    [Provide a clear, concise description of the epic. Explain the business value,
    user needs, or technical goals this epic addresses.]
    
    ## Context
    [Why is this epic important? What problem does it solve?]
    
    ## Success Criteria
    - [ ] [Measurable criterion 1]
    - [ ] [Measurable criterion 2]
    - [ ] [Measurable criterion 3]
    
    ## Scope
    [What's included and what's not included in this epic]
    
    **In Scope**:
    - [Item 1]
    - [Item 2]
    
    **Out of Scope**:
    - [Item 1]
    - [Item 2]
---

# [Epic Name] - Development Tickets

## Sprint [Number] / Phase [Name]

---
ticket:
  id: [PREFIX]-001  # Use consistent prefix: FEAT-001, BUG-001, INFRA-001, etc.
  title: [Brief, Action-Oriented Title]
  type: task  # Options: task, story, bug, spike, technical-debt
  priority: P2  # Options: P0 (critical), P1 (high), P2 (medium), P3 (low)
  points: 3  # Story points: 1, 2, 3, 5, 8, 13, 21
  sprint: 1  # Sprint number or phase
  labels: ["feature"]  # Relevant labels for this ticket
  assignee: ""  # GitHub username or leave empty
  dependencies: []  # Other ticket IDs this depends on: ["PREFIX-000"]
---

### [PREFIX]-001: [Brief Title]

**Description:**
[Clear explanation of what needs to be accomplished. Include enough detail that
any team member can understand the work.]

**Acceptance Criteria:**
- [ ] [Specific, testable criterion 1]
- [ ] [Specific, testable criterion 2]
- [ ] [Specific, testable criterion 3]

**Technical Notes:**
[Optional: Architecture considerations, patterns to use, implementation approach,
constraints, or technical requirements]

**Resources:**
[Optional: Links to designs, documentation, related tickets, or external resources]
- [Link Title](URL)
- `/docs/path/to/file.md`

**Testing Requirements:**
[Optional: Specific testing considerations]
- [ ] Unit tests
- [ ] Integration tests
- [ ] Accessibility validation
- [ ] Performance benchmarks
- [ ] Cross-browser testing

---
ticket:
  id: [PREFIX]-002
  title: [Another Task Title]
  type: task
  priority: P2
  points: 5
  sprint: 1
  labels: ["feature"]
  assignee: ""
  dependencies: ["[PREFIX]-001"]  # This task depends on PREFIX-001
---

### [PREFIX]-002: [Another Task Title]

**Description:**
[Task description]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Technical Notes:**
[Optional implementation details]

---
ticket:
  id: [PREFIX]-003
  title: [Third Task Title]
  type: task
  priority: P1
  points: 2
  sprint: 1
  labels: ["feature", "testing"]
  assignee: ""
  dependencies: ["[PREFIX]-001", "[PREFIX]-002"]  # Multiple dependencies
---

### [PREFIX]-003: [Third Task Title]

**Description:**
[Task description]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Technical Notes:**
[Optional implementation details]

---

## Additional Tickets (Optional Second Sprint/Phase)

---
ticket:
  id: [PREFIX]-004
  title: [Future Task Title]
  type: task
  priority: P3
  points: 8
  sprint: 2
  labels: ["enhancement"]
  assignee: ""
  dependencies: ["[PREFIX]-003"]
---

### [PREFIX]-004: [Future Task Title]

**Description:**
[Task description for future sprint]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

---

<!-- 
================================================================================
USAGE INSTRUCTIONS
================================================================================

1. COPY THIS TEMPLATE
   - Don't edit this file directly
   - Copy to a new file: cp epic-template.md my-feature-epic.md

2. FILL IN THE EPIC SECTION
   - Replace placeholders in the epic frontmatter
   - Write clear description with context and success criteria
   - Add appropriate labels
   - Optional: Set milestone

3. CREATE TICKETS
   - Use consistent ID prefix (FEAT-, BUG-, INFRA-, AUTH-, UI-, etc.)
   - Number sequentially: 001, 002, 003...
   - Set realistic story points
   - Add specific, testable acceptance criteria
   - Mark dependencies between tickets

4. VALIDATE
   - Run dry-run to check for errors:
     python3 scripts/github/issues-create-epic/create-epic.py my-feature-epic.md --dry-run
   
5. CREATE ISSUES
   - Create actual issues:
     python3 scripts/github/issues-create-epic/create-epic.py my-feature-epic.md
   
   - Or specify a different repo:
     python3 scripts/github/issues-create-epic/create-epic.py my-feature-epic.md --repo owner/repo

================================================================================
FIELD GUIDELINES
================================================================================

EPIC FIELDS:
- title: Start with "Epic:" for clarity
- labels: Always include "epic", add others as needed
- milestone: Optional, use for sprint or version planning
- description: Include context, success criteria, and scope

TICKET FIELDS:
- id: Unique identifier (PREFIX-NNN format recommended)
- title: Brief, action-oriented (e.g., "Implement user login")
- type: task, story, bug, spike, technical-debt
- priority: P0 (critical) to P3 (low)
- points: Use Fibonacci: 1, 2, 3, 5, 8, 13, 21
- sprint: Number or name
- labels: Categorize work (frontend, backend, testing, docs, etc.)
- assignee: GitHub username or empty string
- dependencies: Array of ticket IDs (use exact IDs)

TICKET CONTENT:
- Description: What needs to be done and why
- Acceptance Criteria: Specific, testable, checkbox format
- Technical Notes: Implementation guidance (optional)
- Resources: Links to related materials (optional)
- Testing Requirements: QA considerations (optional)

================================================================================
BEST PRACTICES
================================================================================

✅ DO:
- Use descriptive, action-oriented titles
- Write specific, testable acceptance criteria
- Set realistic story points
- Mark true blocking dependencies
- Group related tickets
- Include context and rationale
- Use consistent ID prefixes
- Organize by sprint/phase
- Run dry-run before creating

❌ DON'T:
- Use vague titles like "Update code"
- Skip acceptance criteria
- Over-estimate or under-estimate points
- Create circular dependencies
- Mix unrelated work in one ticket
- Leave fields empty without reason
- Use inconsistent naming
- Forget to validate first

================================================================================
COMMON TICKET PATTERNS
================================================================================

FEATURE DEVELOPMENT:
PREFIX-001: Design and architecture
PREFIX-002: Backend implementation
PREFIX-003: Frontend implementation  
PREFIX-004: Testing and validation
PREFIX-005: Documentation

BUG FIX EPIC:
BUG-001: Reproduce and investigate
BUG-002: Implement fix
BUG-003: Add regression tests
BUG-004: Update documentation

INFRASTRUCTURE:
INFRA-001: Design solution
INFRA-002: Setup infrastructure
INFRA-003: Migration scripts
INFRA-004: Testing and validation
INFRA-005: Rollout and monitoring

================================================================================
EXAMPLE PREFIXES
================================================================================

FEAT-    Feature development
BUG-     Bug fixes
INFRA-   Infrastructure work
AUTH-    Authentication/Authorization
UI-      User interface work
API-     API development
DB-      Database work
TEST-    Testing improvements
DOCS-    Documentation
PERF-    Performance optimization
SEC-     Security improvements
A11Y-    Accessibility improvements

================================================================================
LABEL SUGGESTIONS
================================================================================

TYPE LABELS:
- epic
- feature
- enhancement
- bug
- technical-debt
- spike
- documentation

AREA LABELS:
- frontend
- backend
- database
- api
- infrastructure
- security
- performance
- accessibility

PRIORITY LABELS:
- critical
- high-priority
- low-priority

STATUS LABELS:
- in-progress
- blocked
- needs-review
- ready-for-qa

TEAM LABELS:
- design
- development
- qa
- devops

================================================================================
MORE INFORMATION
================================================================================

See README.md in this directory for:
- Complete documentation
- Command-line options
- Troubleshooting guide
- Advanced usage examples
- Best practices

See test-epic.md for a working example.

================================================================================
-->
