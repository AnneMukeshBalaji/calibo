-- ============================================================
-- STAGE 1: Create the Employees Table
-- ============================================================

CREATE DATABASE IF NOT EXISTS employee_db;
USE employee_db;

CREATE TABLE employees (
    emp_id      INT             PRIMARY KEY AUTO_INCREMENT,
    emp_name    VARCHAR(100)    NOT NULL,
    email       VARCHAR(150)    NOT NULL UNIQUE,
    department  VARCHAR(50)     NOT NULL,
    job_role    VARCHAR(100)    NOT NULL,
    salary      DECIMAL(10, 2)  NOT NULL CHECK (salary > 0),
    age         INT             NOT NULL CHECK (age >= 18 AND age <= 65),
    city        VARCHAR(100)    DEFAULT NULL
);


-- ============================================================
-- STAGE 2: Insert Employee Data (20 Records)
-- ============================================================
-- Covers: 4+ departments, 4+ cities, varied roles/salaries/ages,
--         repeated salaries, repeated cities, one NULL city.

INSERT INTO employees (emp_name, email, department, job_role, salary, age, city) VALUES
('Aarav Sharma',    'aarav.sharma@company.com',    'Engineering',  'Software Engineer',        75000.00, 28, 'Mumbai'),
('Priya Mehta',     'priya.mehta@company.com',     'Engineering',  'Senior Developer',         95000.00, 34, 'Bengaluru'),
('Rohan Verma',     'rohan.verma@company.com',     'Engineering',  'DevOps Engineer',          82000.00, 31, 'Bengaluru'),
('Sneha Iyer',      'sneha.iyer@company.com',      'Engineering',  'QA Engineer',              68000.00, 27, 'Hyderabad'),
('Karan Joshi',     'karan.joshi@company.com',     'Engineering',  'Software Engineer',        75000.00, 29, 'Mumbai'),
('Ananya Nair',     'ananya.nair@company.com',     'Marketing',    'Marketing Manager',        88000.00, 36, 'Delhi'),
('Vikram Rao',      'vikram.rao@company.com',      'Marketing',    'Content Strategist',       62000.00, 25, 'Mumbai'),
('Divya Pillai',    'divya.pillai@company.com',    'Marketing',    'SEO Specialist',           58000.00, 24, 'Bengaluru'),
('Mohit Gupta',     'mohit.gupta@company.com',     'Marketing',    'Brand Analyst',            65000.00, 30, 'Delhi'),
('Lakshmi Reddy',   'lakshmi.reddy@company.com',   'HR',           'HR Manager',               80000.00, 38, 'Hyderabad'),
('Suresh Babu',     'suresh.babu@company.com',     'HR',           'Recruiter',                55000.00, 26, 'Chennai'),
('Nisha Kulkarni',  'nisha.kulkarni@company.com',  'HR',           'HR Executive',             52000.00, 23, 'Pune'),
('Arjun Desai',     'arjun.desai@company.com',     'HR',           'Payroll Specialist',       60000.00, 32, 'Pune'),
('Pooja Singh',     'pooja.singh@company.com',     'Finance',      'Financial Analyst',        90000.00, 35, 'Mumbai'),
('Rahul Kapoor',    'rahul.kapoor@company.com',    'Finance',      'Accountant',               70000.00, 29, 'Delhi'),
('Meera Patel',     'meera.patel@company.com',     'Finance',      'Tax Consultant',           78000.00, 33, 'Bengaluru'),
('Aditya Kumar',    'aditya.kumar@company.com',    'Finance',      'CFO',                     150000.00, 45, 'Mumbai'),
('Ritika Saxena',   'ritika.saxena@company.com',   'Engineering',  'Data Scientist',          105000.00, 37, 'Hyderabad'),
('Sameer Khan',     'sameer.khan@company.com',     'Marketing',    'Digital Marketing Lead',   72000.00, 28, NULL),
('Tanvi Bhatt',     'tanvi.bhatt@company.com',     'HR',           'Training Coordinator',     58000.00, 27, 'Chennai');


-- ============================================================
-- STAGE 3: SELECT Queries
-- ============================================================

-- 3.1 Display all employee records
SELECT * FROM employees;

-- 3.2 Display specific columns: name, department, salary, city
SELECT emp_name, department, salary, city
FROM employees;

-- 3.3 Retrieve employees from the Engineering department
SELECT * FROM employees
WHERE department = 'Engineering';


-- ============================================================
-- STAGE 4: WHERE and Comparison Operators
-- ============================================================

-- 4.1 (=) Employees with salary exactly 75000
SELECT * FROM employees WHERE salary = 75000;

-- 4.2 (>) Employees earning more than 80000
SELECT * FROM employees WHERE salary > 80000;

-- 4.3 (<) Employees below age 30
SELECT * FROM employees WHERE age < 30;

-- 4.4 (>=) Employees earning 80000 or more
SELECT * FROM employees WHERE salary >= 80000;

-- 4.5 (<=) Employees aged 30 or younger
SELECT * FROM employees WHERE age <= 30;

-- 4.6 (<>) Employees not in the Marketing department
SELECT * FROM employees WHERE department <> 'Marketing';

-- 4.7 (!=) Employees not in the HR department
SELECT * FROM employees WHERE department != 'HR';


-- ============================================================
-- STAGE 5: Logical Operators
-- ============================================================

-- 5.1 (AND) Engineering employees earning above 80000
SELECT * FROM employees
WHERE department = 'Engineering' AND salary > 80000;

-- 5.2 (OR) Employees from Engineering or Finance
SELECT * FROM employees
WHERE department = 'Engineering' OR department = 'Finance';

-- 5.3 (NOT) Employees NOT from Marketing
SELECT * FROM employees
WHERE NOT department = 'Marketing';


-- ============================================================
-- STAGE 6: Special Operators
-- ============================================================

-- 6.1 BETWEEN – Employees with salary between 60000 and 90000
SELECT * FROM employees WHERE salary BETWEEN 60000 AND 90000;

-- 6.2 BETWEEN – Employees aged between 25 and 35
SELECT * FROM employees WHERE age BETWEEN 25 AND 35;

-- 6.3 IN – Employees in Engineering, Finance, or HR departments
SELECT * FROM employees WHERE department IN ('Engineering', 'Finance', 'HR');

-- 6.4 IN – Employees in Mumbai or Delhi
SELECT * FROM employees WHERE city IN ('Mumbai', 'Delhi');

-- 6.5 NOT IN – Employees NOT in Marketing or HR
SELECT * FROM employees WHERE department NOT IN ('Marketing', 'HR');

-- 6.6 LIKE – Employees whose name starts with 'A'
SELECT * FROM employees WHERE emp_name LIKE 'A%';

-- 6.7 LIKE – Employees whose name contains 'ar'
SELECT * FROM employees WHERE emp_name LIKE '%ar%';

-- 6.8 LIKE – Employees whose email ends with '@company.com'
SELECT * FROM employees WHERE email LIKE '%@company.com';

-- 6.9 IS NULL – Employees with no city recorded
SELECT * FROM employees WHERE city IS NULL;

-- 6.10 IS NOT NULL – Employees with a city recorded
SELECT * FROM employees WHERE city IS NOT NULL;


-- ============================================================
-- STAGE 7: ORDER BY
-- ============================================================

-- 7.1 Sort by salary ascending
SELECT * FROM employees ORDER BY salary ASC;

-- 7.2 Sort by salary descending
SELECT * FROM employees ORDER BY salary DESC;

-- 7.3 Sort by age ascending
SELECT * FROM employees ORDER BY age ASC;

-- 7.4 Sort by department alphabetically
SELECT * FROM employees ORDER BY department ASC;

-- 7.5 Sort by department ASC, then salary DESC (multiple columns)
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- 7.6 Sort by city ASC then age DESC
SELECT * FROM employees ORDER BY city ASC, age DESC;


-- ============================================================
-- STAGE 8: Aggregate Functions
-- ============================================================

-- 8.1 COUNT – Total number of employees
SELECT COUNT(*) AS total_employees FROM employees;

-- 8.2 SUM – Total salary paid to all employees
SELECT SUM(salary) AS total_salary FROM employees;

-- 8.3 AVG – Average salary of all employees
SELECT AVG(salary) AS average_salary FROM employees;

-- 8.4 MIN – Lowest salary
SELECT MIN(salary) AS min_salary FROM employees;

-- 8.5 MAX – Highest salary
SELECT MAX(salary) AS max_salary FROM employees;


-- ============================================================
-- STAGE 9: GROUP BY
-- ============================================================

-- 9.1 Count of employees per department
SELECT department, COUNT(*) AS employee_count
FROM employees GROUP BY department;

-- 9.2 Average salary per department
SELECT department, AVG(salary) AS avg_salary
FROM employees GROUP BY department;

-- 9.3 Minimum salary per department
SELECT department, MIN(salary) AS min_salary
FROM employees GROUP BY department;

-- 9.4 Maximum salary per department
SELECT department, MAX(salary) AS max_salary
FROM employees GROUP BY department;

-- 9.5 Total salary per department
SELECT department, SUM(salary) AS total_salary
FROM employees GROUP BY department;

-- 9.6 Count of employees per city
SELECT city, COUNT(*) AS employee_count
FROM employees GROUP BY city;

-- 9.7 Average salary per city
SELECT city, AVG(salary) AS avg_salary
FROM employees GROUP BY city;

-- 9.8 Maximum salary per city
SELECT city, MAX(salary) AS max_salary
FROM employees GROUP BY city;


-- ============================================================
-- STAGE 10: HAVING
-- ============================================================

-- 10.1 Departments with more than 4 employees
SELECT department, COUNT(*) AS employee_count
FROM employees GROUP BY department HAVING COUNT(*) > 4;

-- 10.2 Departments with average salary above 70000
SELECT department, AVG(salary) AS avg_salary
FROM employees GROUP BY department HAVING AVG(salary) > 70000;

-- 10.3 Cities with more than 2 employees
SELECT city, COUNT(*) AS employee_count
FROM employees GROUP BY city HAVING COUNT(*) > 2;

-- 10.4 Departments where maximum salary is above 90000
SELECT department, MAX(salary) AS max_salary
FROM employees GROUP BY department HAVING MAX(salary) > 90000;


-- ============================================================
-- STAGE 11: Challenge Questions
-- ============================================================

-- 11.1 Find the second-highest salary
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- 11.2 Find employees earning above the average salary
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 11.3 Find the employee(s) with the highest salary
SELECT * FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 11.4 Find the employee(s) with the lowest salary
SELECT * FROM employees
WHERE salary = (SELECT MIN(salary) FROM employees);

-- 11.5 Find the department with the highest average salary
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;

-- 11.6 Find the department with the highest number of employees
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC
LIMIT 1;

-- 11.7 Find employees who earn more than the average salary of their department
SELECT e.*
FROM employees e
JOIN (
    SELECT department, AVG(salary) AS dept_avg
    FROM employees
    GROUP BY department
) dept_avg_table
ON e.department = dept_avg_table.department
WHERE e.salary > dept_avg_table.dept_avg;

-- 11.8 Find the second-highest salary in each department
SELECT department, MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary) FROM employees e2
    WHERE e2.department = employees.department
)
GROUP BY department;

-- 11.9 Find cities with the highest number of employees
SELECT city, COUNT(*) AS employee_count
FROM employees
GROUP BY city
ORDER BY employee_count DESC
LIMIT 1;

-- 11.10 Find departments where total salary is greater than 250000
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 250000;

-- ============================================================
-- END OF ASSIGNMENT
-- ============================================================
