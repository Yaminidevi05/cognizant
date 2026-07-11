# Hands-On 2 – SDLC vs TDLC: V-Model & Agile QA Integration

## Name:
## Register Number:
## Date:

---

# Task 1: V-Model Mapping

## 1. V-Model Diagram

```
                    SDLC (Development)

          Requirements Specification
                    |
                    |
              System Design
                    |
                    |
          Architecture Design
                    |
                    |
              Module Design
                    |
                    |
                  Coding
                    ▲
                    |
            Unit Testing
                    |
                    |
        Integration Testing
                    |
                    |
          System Testing
                    |
                    |
       Acceptance Testing

                 TDLC (Testing)
```

### SDLC to TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase |
|------------|--------------------------|
| Requirements | Acceptance Testing |
| System Design | System Testing |
| Architecture Design | Integration Testing |
| Module Design | Unit Testing |
| Coding | Implementation |

---

# 2. Test Artifacts Produced During Development

| SDLC Phase | Corresponding Test Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements | Acceptance Testing | Acceptance Test Plan, Acceptance Test Cases |
| System Design | System Testing | System Test Plan, System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan, Integration Test Cases |
| Module Design | Unit Testing | Unit Test Cases, Unit Test Plan |
| Coding | Execution | Source Code, Unit Test Execution Results |

---

# 3. Entry and Exit Criteria

## Unit Testing

### Entry Criteria
- Module coding completed.
- Code successfully compiled.
- Unit test cases prepared.

### Exit Criteria
- All unit tests executed.
- No Critical or High severity defects.
- Code coverage meets project standards.

---

## Integration Testing

### Entry Criteria
- Individual modules passed unit testing.
- Modules integrated successfully.
- Integration test cases available.

### Exit Criteria
- All integration test cases executed.
- Interfaces between modules work correctly.
- No unresolved Critical defects.

---

## System Testing

### Entry Criteria
- Entire application integrated.
- System test environment ready.
- Test data prepared.

### Exit Criteria
- All planned system test cases executed.
- Functional requirements verified.
- No Critical or High severity defects remain.

---

## Acceptance Testing

### Entry Criteria
- System testing completed successfully.
- Business requirements documented.
- UAT environment available.

### Exit Criteria
- Customer approves the application.
- Business requirements satisfied.
- Product ready for production deployment.

---

# 4. Early QA Engagement in the Course Management API

### 1. Requirements Review

QA reviews the project requirements before development starts to identify:
- Missing requirements
- Ambiguous statements
- Validation rules
- Error scenarios

This prevents defects before coding begins.

---

### 2. Design Review

QA participates during API and database design by reviewing:
- API endpoints
- Request and response formats
- Database schema
- Error handling
- Validation rules

This ensures the design is testable and reduces future defects.

---

# Task 2: Agile QA and Shift-Left Testing

## 5. Problems with Waterfall Testing

In the Waterfall model, testing starts only after development is complete.

### Problem 1

Defects are discovered very late, making them expensive to fix.

---

### Problem 2

Requirement misunderstandings remain unnoticed until testing begins.

---

### Problem 3

Development delays directly delay testing, reducing the time available for proper QA.

---

# 6. QA Role in Agile Ceremonies

## Sprint Planning

QA:
- Reviews user stories.
- Defines acceptance criteria.
- Estimates testing effort.
- Identifies testing risks.

---

## Daily Standup

QA:
- Reports testing progress.
- Discusses blocked defects.
- Coordinates with developers.
- Highlights testing issues.

---

## Sprint Review

QA:
- Demonstrates completed features.
- Verifies acceptance criteria.
- Confirms all stories are tested.
- Shares defect status.

---

## Sprint Retrospective

QA:
- Discusses testing improvements.
- Suggests automation opportunities.
- Identifies process improvements.
- Shares lessons learned.

---

# 7. Shift-Left Testing Practices

## a. Review Requirements for Testability

Before development starts, QA reviews the Course Management API requirements to ensure:
- Every requirement is measurable.
- Validation rules are defined.
- Error responses are specified.

---

## b. Write Test Cases Before Coding (TDD/BDD)

QA prepares test scenarios before development begins.

Example:
Write tests for creating a course before developers implement the POST endpoint.

---

## c. Static Code Analysis

Developers run static analysis tools to detect:
- Code quality issues
- Security vulnerabilities
- Coding standard violations

before executing the application.

---

## d. API Contract Testing Before Integration

QA verifies API contracts using the API specification.

Checks include:
- Endpoint URLs
- HTTP methods
- Request body format
- Response format
- Status codes

This ensures frontend and backend integration is smooth.

---

# 8. Acceptance Criteria (Given-When-Then)

## Scenario 1: Happy Path

**Given**
the college admin is logged in

**When**
the admin submits valid course details

**Then**
the course is created successfully

**And**
HTTP Status Code 201 is returned

---

## Scenario 2: Duplicate Course Code

**Given**
a course with the same course code already exists

**When**
the admin submits another course using that course code

**Then**
the system rejects the request

**And**
an appropriate duplicate course error message is displayed

---

## Scenario 3: Missing Required Fields

**Given**
the admin opens the Create Course page

**When**
required fields such as Course Name or Course Code are left empty

**Then**
validation errors are displayed

**And**
the course is not created

---

# Conclusion

This document includes:

- Complete V-Model mapping
- SDLC ↔ TDLC relationship
- Test artifacts for every phase
- Entry and Exit Criteria for all testing levels
- Two early QA engagement points
- Three Waterfall testing problems
- QA responsibilities in Agile ceremonies
- Four Shift-Left testing practices
- Three Gherkin Acceptance Criteria scenarios

