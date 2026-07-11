# automation_strategy.md

# Hands-On 3 – Test Automation Process, Lifecycle & Framework Types

---

# Task 1: Automation Decision and Test Case Selection

## 1. Criteria for Deciding Whether a Test Case Should Be Automated

### Criterion 1: Repetitive Execution
Tests that are executed frequently are good candidates for automation because automation saves time and effort.

**Application to Scenario**

Test:
**POST /api/courses/** returns **201 Created** with the correct course data.

This API endpoint will be executed repeatedly during development and regression testing.

**Decision:** ✅ Automate

---

### Criterion 2: Regression Testing

Regression tests ensure that new code changes do not break existing functionality.

**Application to Scenario**

Creating a course is a core feature of the application. Every new release should verify that it still works correctly.

**Decision:** ✅ Automate

---

### Criterion 3: Stable Functionality

Automation is most effective when the functionality changes infrequently.

**Application to Scenario**

The API contract for creating courses is expected to remain stable.

**Decision:** ✅ Automate

---

### Criterion 4: High Risk or Business Critical

Business-critical features should always be validated automatically.

**Application to Scenario**

If course creation fails, users cannot add new courses to the system.

**Decision:** ✅ Automate

---

### Criterion 5: Data-Driven Testing

Tests requiring multiple input combinations are ideal for automation.

**Application to Scenario**

Different course names, durations, instructors, and categories can be tested using multiple datasets.

**Decision:** ✅ Automate

---

# 2. Automate or Manual Decision

| Test Case | Decision | Justification |
|------------|----------|---------------|
| (a) Regression test for all CRUD endpoints after every code change | ✅ Automate | Executed frequently and ideal for CI/CD pipelines. |
| (b) Exploratory testing of a new search feature | ❌ Manual | Requires human observation and creativity. |
| (c) Performance test with 100 concurrent users calling GET /api/courses/ | ✅ Automate | Performance testing requires automation tools for repeatable load generation. |
| (d) UI test for the login form | ✅ Automate | Login is a stable and frequently tested feature. |
| (e) Verify the API documentation (Swagger) is accurate | ❌ Manual | Documentation changes infrequently and benefits from manual review. |
| (f) Smoke test: Verify API is reachable after deployment | ✅ Automate | Quick validation after every deployment makes automation valuable. |

---

# 3. Test Automation ROI

## Definition

Test Automation ROI (Return on Investment) measures when the time and cost spent developing automated tests become less than the cumulative cost of executing the same tests manually.

---

### Given

Automation development time = **4 hours**

Manual execution time = **30 minutes = 0.5 hours**

Maintenance overhead after the 10th run = **20% of manual execution time**

Maintenance per run after run 10

20% × 0.5 = **0.1 hours**

---

### Break-even without Maintenance

4 ÷ 0.5 = **8 runs**

Therefore,

Automation pays for itself after **8 executions**.

---

### Considering Maintenance After the 10th Run

Runs 1–10

Automation Cost = 4 hours

Manual Cost = 10 × 0.5 = 5 hours

Automation is already cheaper.

From Run 11 onward

Automation cost increases by only **0.1 hours per run**, while manual execution still costs **0.5 hours per run**.

Automation continues to save:

0.5 − 0.1 = **0.4 hours per additional run**

---

### Final Answer

Automation reaches break-even after approximately **8 runs**.

Even after the maintenance overhead begins, automation continues to provide significant long-term savings.

---

# 4. Flaky Tests

## Definition

A flaky test is a test that sometimes passes and sometimes fails without any change in the application code.

These inconsistent results reduce confidence in the automation suite.

---

## Example

A Selenium test clicks the Login button before the page has completely loaded.

Sometimes the button is available and the test passes.

Sometimes the button is still loading and the test fails.

---

## Strategies to Prevent or Fix Flaky Tests

### 1. Use Explicit Waits

Wait until elements are visible or clickable instead of using fixed delays.

---

### 2. Use Stable Locators

Prefer IDs or unique CSS selectors instead of dynamic XPath expressions.

---

### 3. Keep Tests Independent

Each test should create its own test data and should not depend on previous test execution.

---

# Task 2: Compare Automation Framework Types

## 1. Linear Framework

### Description

A Linear Framework executes test scripts sequentially without separating data or reusable components. Each test case contains all steps in one script.

### Advantage

Easy to understand for beginners.

### Disadvantage

Poor code reuse and difficult maintenance.

### Example

Automating a single login and course creation workflow for a small prototype.

---

## 2. Modular Framework

### Description

A Modular Framework divides the application into reusable modules such as Login, Dashboard, and Course Management. Test scripts call these modules whenever required.

### Advantage

High code reusability.

### Disadvantage

Test data is usually hardcoded.

### Example

Create separate modules for Login, Add Course, Edit Course, and Delete Course.

---

## 3. Data-Driven Framework

### Description

A Data-Driven Framework stores test inputs in external files such as Excel, CSV, or JSON while the same automation code executes multiple datasets.

### Advantage

Large amounts of test data can be tested without changing code.

### Disadvantage

Managing external data files increases complexity.

### Example

Testing course creation using multiple course names, durations, and instructors from an Excel sheet.

---

## 4. Keyword-Driven Framework

### Description

A Keyword-Driven Framework stores test actions as keywords such as Login, ClickButton, EnterText, and VerifyMessage. The framework interprets these keywords during execution.

### Advantage

Non-technical users can create test cases.

### Disadvantage

Framework implementation is more complex.

### Example

Business analysts prepare keyword-based test cases for Course Management workflows.

---

## 5. Hybrid Framework

### Description

A Hybrid Framework combines Modular, Data-Driven, and Keyword-Driven approaches. It provides reusable components, external test data, and keyword abstraction.

### Advantage

Highly scalable, reusable, and maintainable.

### Disadvantage

Initial setup requires more effort.

### Example

Large Selenium automation suite for the Course Management application with reusable page objects, Excel data, utilities, and keyword support.

---

# 2. Recommended Framework

## Scenario

Requirements:

- Test login with 50 username/password combinations.
- Reuse login steps across 20 test cases.
- Support both technical and non-technical team members.

---

## Recommendation

A **Hybrid Framework** combining:

- **Modular Framework** for reusable login components.
- **Data-Driven Framework** for 50 login credentials.
- **Keyword-Driven Framework** for allowing non-technical users to create test scenarios.

### Justification

- Login module is reused across multiple tests.
- External data files eliminate duplicate scripts.
- Keywords make the framework easier for business users.
- Highly maintainable for long-term projects.

---

# 3. Hybrid Framework Folder Structure

```
CourseManagementAutomation/
│
├── config/
│   ├── config.properties
│   └── browser.properties
│
├── testdata/
│   ├── LoginData.xlsx
│   ├── CourseData.xlsx
│   └── Users.csv
│
├── pages/
│   ├── LoginPage.java
│   ├── DashboardPage.java
│   ├── CoursePage.java
│   └── ProfilePage.java
│
├── tests/
│   ├── LoginTest.java
│   ├── CourseTest.java
│   └── SmokeTest.java
│
├── utilities/
│   ├── ExcelReader.java
│   ├── DriverFactory.java
│   ├── ConfigReader.java
│   ├── ScreenshotUtil.java
│   └── WaitHelper.java
│
├── keywords/
│   ├── LoginKeywords.java
│   ├── CourseKeywords.java
│   └── CommonKeywords.java
│
├── reports/
│
├── screenshots/
│
└── pom.xml
```

### Folder Description

- **config/** – Stores configuration files.
- **testdata/** – Contains Excel, CSV, or JSON test data.
- **pages/** – Implements Page Object Model classes.
- **tests/** – Contains Selenium test cases.
- **utilities/** – Includes reusable helper classes.
- **keywords/** – Stores keyword-based reusable actions.
- **reports/** – Stores test execution reports.
- **screenshots/** – Stores failure screenshots.

---

# Conclusion

A successful automation strategy begins with selecting the right test cases based on repetition, stability, business impact, regression needs, and data-driven requirements. Understanding different automation frameworks helps teams choose the most suitable architecture. For the Course Management application, a Hybrid Framework offers the best balance of maintainability, scalability, code reuse, and support for both technical and non-technical team members.