SELECT CompanyName,  Round(AVG(julianday(ShippedDate) - julianday(Orderdate)),1) AS AVG_DL , count(*) AS Anzahl FROM Orders 
JOIN Shippers on ShipVia = ShipperID
WHERE ShippedDate IS NOT NULL
GROUP BY CompanyName
