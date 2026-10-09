SELECT ShipCountry, round((SUM(ShippedDate > RequiredDate))*100.0/count(ShippedDate),1) AS Verspaetet_PC FROM Orders
GROUP BY ShipCountry
ORDER BY Verspaetet_PC DESC