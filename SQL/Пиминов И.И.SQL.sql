Задание 1

WITH ProjectSalary AS (
  SELECT
   	p.project_name,
    t.titel_name,
    AVG(pos.salary) AS average_salary
  FROM positions AS pos
  JOIN employees AS emp
    ON pos.employee_id = emp.employee_id
  JOIN projects AS p
    ON pos.project_id = p.project_id
  JOIN titles AS t
    ON pos.title_id = t.Id
  WHERE
    t.titel_name = 'qa engineer' AND (
      p.project_name = 'ПУМЧД' OR p.project_name = 'ГИС КАП'
    )
  GROUP BY
    p.project_name,
    t.titel_name
)
SELECT
  project_name AS "проект",
  titel_name AS "должность",
  average_salary AS "средняя заработная плата"
FROM ProjectSalary
ORDER BY
  project_name,
  titel_name;

----------------

Задание 2

SELECT 
    p.project_name AS "Проект", 
    COUNT(DISTINCT pos.employee_id) AS "Количество сотрудников"
FROM projects AS p
JOIN positions AS pos
    ON p.project_id = pos.project_id
GROUP BY
    p.project_name
HAVING 
    COUNT(DISTINCT pos.employee_id) > 10
ORDER BY
    p.project_name;
