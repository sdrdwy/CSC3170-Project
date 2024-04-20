LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Manufacturers.csv'
INTO TABLE Manufacturer
FIELDS TERMINATED BY ','  -- 字段分隔符，适应您的CSV格式
-- ENCLOSED BY '"'           -- 如果字段被引号包围，适应您的CSV格式
LINES TERMINATED BY '\n'  -- 行分隔符
IGNORE 1 LINES;           -- 如果CSV文件包含列标题，忽略第一行

LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Teams.csv'
INTO TABLE Team
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;       
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Customers.csv'
INTO TABLE Customer
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;        
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Tire Information.csv'
INTO TABLE Tire_Information
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;        
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Warehouses.csv'
INTO TABLE Warehouse
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;        
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Shipyards.csv'
INTO TABLE Shipyard
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;        
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Employees.csv'
INTO TABLE Employee
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;        
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Transport orders.csv'
INTO TABLE Transport_order
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;        
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Selling Orders.csv'
INTO TABLE Selling_Order
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;                
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Selling Order Details.csv'
INTO TABLE Selling_Order_Detail
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;           
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Manufacturer Detail.csv'
INTO TABLE Manufacturer_Detail
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;           
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Manu Orders.csv'
INTO TABLE Manu_Order
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;           
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Manu Order Details.csv'
INTO TABLE Manu_Order_Detail
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;               
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Inventory.csv'
INTO TABLE Inventory
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;               
    
LOAD DATA INFILE 'D:/Study materials/csc/CSC3170/Project/Dataset/data/Transport Order Details.csv'
INTO TABLE Transport_Order_Detail
FIELDS TERMINATED BY ','          
LINES TERMINATED BY '\n'  
IGNORE 1 LINES;