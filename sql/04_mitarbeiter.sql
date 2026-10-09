SELECT FirstName, LastName,  Round(AVG(julianday(ShippedDate) - julianday(Orderdate)),1) AS AVG_DL , count(*) AS Anzahl, Orders.EmployeeID AS Employeenumber FROM Orders 
JOIN Employees on Employees.EmployeeID= Orders.EmployeeID
WHERE ShippedDate IS NOT NULL
GROUP BY Orders.EmployeeID
ORDER BY AVG_DL DESC