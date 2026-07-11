# Hands-On 1 – QA Concepts, Functional Testing & Defect Lifecycle

## Name:
## Register Number:
## Date:

---

# Task 1: Map Testing Types to a Real System

## 1. Testing Types for the Course Management API

### Unit Testing
**Description:**
Tests a single function independently without involving the database or API.

**Example Test Case:**
Test the `validate_course_name()` function to ensure it accepts valid course names and rejects empty strings.

**Testing Type:**
Functional Testing

---

### Integration Testing
**Description:**
Tests whether multiple components work together correctly.

**Example Test Case:**
Send a POST request to `/api/courses/` and verify that the course is successfully stored in the database.

**Testing Type:**
Functional Testing

---

### System Testing
**Description:**
Tests the complete application from beginning to end.

**Example Test Case:**
Create a course using the API, retrieve it using GET `/api/courses/`, update it, and finally delete it. Verify that all operations complete successfully.

**Testing Type:**
Functional Testing

---

### User Acceptance Testing (UAT)
**Description:**
Tests whether the application satisfies the actual user's business requirements.

**Example Test Case:**
A college administrator logs in, creates a new course, edits course details, views the course list, and confirms that the workflow meets the college's requirements.

**Testing Type:**
Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Testing
Checks whether the application performs the required functionality correctly.

**Example**
Verify that POST `/api/courses/` successfully creates a new course.

### Non-Functional Testing
Checks how well the application performs.

**Example**
Performance Testing:
Verify that the Course Management API responds within **2 seconds** while handling **100 simultaneous users**.

---

## 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|-------------------|-------------------|
| Tests application without knowledge of internal code. | Tests application with knowledge of source code. |
| Focuses on inputs and outputs. | Focuses on code structure, logic and execution paths. |
| Performed mainly by QA Testers. | Performed mainly by Developers. |
| Validates functionality. | Validates code quality and internal implementation. |

**QA Tester:** Usually performs **Black-Box Testing**

**Developer:** Usually performs **White-Box Testing**

---

## 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create a course with valid details | API server running | 1. Open Postman 2. Send POST request with valid JSON | Course created successfully with HTTP 201 | | |
| TC002 | Create a course without course name | API server running | Send POST request with empty course_name | Validation error (HTTP 400/422) | | |
| TC003 | Create duplicate course | Course already exists | Send POST request using existing course details | Duplicate record error returned | | |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Additional Paths

**Rejected**
- The reported issue is not considered a valid defect.
- Example: Expected system behavior.

**Deferred**
- The defect is acknowledged but postponed to a future release due to lower priority or time constraints.

---

## 6. Severity and Priority Classification

### a. POST /api/courses/ returns 500 Internal Server Error for all requests

**Severity:** Critical

**Priority:** P1

**Justification:**
The API cannot create courses, making a core feature unusable.

---

### b. Course names longer than 150 characters are silently truncated

**Severity:** Medium

**Priority:** P3

**Justification:**
Data integrity is affected but the application remains usable.

---

### c. Swagger /docs page contains a typo

**Severity:** Low

**Priority:** P4

**Justification:**
Only documentation is affected.

---

### d. Login occasionally returns 401 despite correct credentials

**Severity:** High

**Priority:** P2

**Justification:**
Intermittent authentication failures affect users and indicate instability.

---

## 7. Defect Report

**Defect ID:** BUG-001

**Title:**
POST /api/courses/ returns 500 Internal Server Error for all requests

**Environment:**
- Windows 11
- Python 3.14
- FastAPI
- MySQL
- Postman

**Build Version:**
v1.0.0

**Severity:**
Critical

**Priority:**
P1

**Steps to Reproduce**

1. Start the Course Management API.
2. Open Postman.
3. Send POST request to `/api/courses/`.
4. Provide valid JSON data.
5. Click Send.

**Expected Result**

The course should be created successfully and HTTP 201 Created should be returned.

**Actual Result**

HTTP 500 Internal Server Error is returned for every request.

**Attachments**

Screenshot of 500 Internal Server Error.

---

## 8. Difference Between Severity and Priority

### Severity
Severity measures how much the defect impacts the system.

### Priority
Priority measures how quickly the defect should be fixed.

### Example

A spelling mistake on the CEO's dashboard:

- **Severity:** Low (does not affect functionality)
- **Priority:** High (needs immediate correction before a presentation)

Another example:

A rarely used report export feature crashes.

- **Severity:** High (feature completely broken)
- **Priority:** Low (few users access it, so it can be fixed later)

This demonstrates that High Severity does not always mean High Priority.

---

# Conclusion

This document demonstrates:

- Unit Testing
- Integration Testing
- System Testing
- User Acceptance Testing
- Functional Testing
- Non-Functional Testing
- Black-Box Testing
- White-Box Testing
- Formal Test Case Documentation
- Complete Defect Lifecycle
- Severity and Priority Classification
- Professional Defect Report