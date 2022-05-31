## Write your MySQL query statement below
#alter table Employees
#add total_time;

#SELECT event_day AS day        
#FROM Employees;
Select 
    event_day as day,
    emp_id, 
    SUM(out_time - in_time) as total_time
from Employees
Group by emp_id,day;
