---
epic:
  title: "Epic: Test Epic for Script Validation"
  labels: ["epic", "test"]
  milestone: ""
  description: |
    This is a test epic created to validate the create-epic.py script functionality.
    
    Success Criteria:
    - Script successfully parses the markdown file
    - Epic issue is created in GitHub
    - Child issues are created and linked to the epic
---

# Test Epic - Development Tickets

## Test Sprint

---
ticket:
  id: TEST-001
  title: First Test Child Issue
  type: task
  priority: P1
  points: 2
  sprint: 1
  labels: ["test", "child-issue"]
  assignee: ""
  dependencies: []
---

### TEST-001: First Test Child Issue

**Description:**
This is the first test child issue to validate the create-epic.py script.

**Acceptance Criteria:**
- [ ] Issue is created successfully
- [ ] Issue is linked to parent epic
- [ ] Issue has proper labels and metadata

**Technical Notes:**
- This is a test issue
- No actual implementation required

---
ticket:
  id: TEST-002
  title: Second Test Child Issue
  type: task
  priority: P2
  points: 3
  sprint: 1
  labels: ["test", "child-issue"]
  assignee: ""
  dependencies: ["TEST-001"]
---

### TEST-002: Second Test Child Issue

**Description:**
This is the second test child issue to validate the create-epic.py script.
This issue depends on TEST-001 to test dependency linking.

**Acceptance Criteria:**
- [ ] Issue is created successfully
- [ ] Issue is linked to parent epic
- [ ] Dependency on TEST-001 is properly referenced
- [ ] Issue has proper labels and metadata

**Technical Notes:**
- This is a test issue with a dependency
- No actual implementation required
