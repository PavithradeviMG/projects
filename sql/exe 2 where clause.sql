USE intro_sql;

SELECT product_name AS 'Product',category, units_in_stock AS 'Units' FROM products;

SELECT product_name AS 'Product', category, units_in_stock AS 'Units' FROM products
WHERE (category = 'seafood' AND discontinued <> 1) OR (category = 'Dairy products'AND discontinued <> 1) ;

SELECT product_name AS 'Product', category, units_in_stock AS 'Units' FROM products
WHERE category IN ('Beverages','Dairy Products') AND discontinued <>1;