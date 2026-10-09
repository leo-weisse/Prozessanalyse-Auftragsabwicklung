SELECT CompanyName, round(sum(UnitPrice*Quantity*(1-Discount)),2) AS umsatz FROM "Order Details"
JOIN Orders
ON "Order Details".OrderID = Orders.OrderID
JOIN Customers
ON Orders.CustomerID = Customers.CustomerID 
GROUP BY Customers.CustomerID
Order By umsatz DESC;