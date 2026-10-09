SELECT (ShippedDate > RequiredDate) AS Verspaetet,
       COUNT(*) AS Anzahl,
       ROUND(AVG(julianday(RequiredDate) - julianday(OrderDate)), 1) AS Zugesagt_Tage,
       ROUND(AVG(julianday(ShippedDate) - julianday(Orderdate)), 1) AS Tatsaechlich_Tage
FROM Orders
WHERE ShippedDate IS NOT NULL 
GROUP BY Verspaetet