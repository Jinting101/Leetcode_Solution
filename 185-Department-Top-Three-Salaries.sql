# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, salary AS Salary
FROM Department AS d JOIN (
    SELECT name,salary, departmentId, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS row_num
    FROM Employee
) AS e on d.id = e.departmentId
WHERE e.row_num < 4