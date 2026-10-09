SELECT CompanyName, round((SUM(ShippedDate > RequiredDate))*100.0/count(ShippedDate),1) AS Verspaetet_Prozent FROM Orders
JOIN Shippers on ShipVia = ShipperID
GROUP BY CompanyName
ORDER BY Verspaetet_Prozent DESC
