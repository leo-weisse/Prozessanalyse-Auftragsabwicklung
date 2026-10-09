SELECT OrderID,
       ShipCountry AS Land,
       CompanyName AS Versender,
       strftime('%Y', OrderDate) AS Jahr,
       CAST(ROUND(julianday(ShippedDate) - julianday(Orderdate)) AS INTEGER) AS Durchlaufzeit_Tage,   
       (ShippedDate > RequiredDate) AS Verspaetet                                  
FROM Orders
JOIN Shippers ON ShipVia = ShipperID               
WHERE ShippedDate IS NOT NULL                                                