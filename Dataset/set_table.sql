DROP SCHEMA IF EXISTS `Tire_Company` ;
CREATE SCHEMA IF NOT EXISTS `Tire_Company` DEFAULT CHARACTER SET utf8mb4 ;
USE `Tire_Company` ;

CREATE TABLE Manufacturer (
	manu_ID INT,
    manu_name VARCHAR(45),
    manufacturer_info VARCHAR(45),
    manu_phone_num VARCHAR(45),
    manu_addr VARCHAR(45),
    PRIMARY KEY (manu_ID)
);

CREATE TABLE Team (
	team_ID INT,
    team_name VARCHAR(45),
    leader VARCHAR(45),
    members_info VARCHAR(45),
    PRIMARY KEY (team_ID)
);

CREATE TABLE Customer (
	Customer_ID INT,
    customer_name VARCHAR(45),
    customer_phone_number VARCHAR(45),
    PRIMARY KEY (Customer_ID)
);

CREATE TABLE Tire_Information (
	tire_ID INT,
    tire_size VARCHAR(45),
    tire_inch VARCHAR(45),
    tire_pattern VARCHAR(45),
    tire_max_container_capacity INT,
    tire_price INT,
    PRIMARY KEY (tire_ID)
);

CREATE TABLE Warehouse (
	warehouse_ID INT,
    warehouse_addr VARCHAR(45),
    capacity INT,
    PRIMARY KEY (warehouse_ID)
);

CREATE TABLE Shipyard (
	shipyard_ID INT,
    transport_price INT,
    PRIMARY KEY (shipyard_ID)
);

CREATE TABLE Employee (
	employee_ID INT,
    employee_name VARCHAR(45),
    team_ID INT,
    PRIMARY KEY (employee_ID, team_ID),
    FOREIGN KEY (team_ID) REFERENCES Team(team_ID)
);

CREATE TABLE Transport_order (
	transport_order_ID INT,
    shipyard_ID INT,
    team_ID INT,
    transport_date DATETIME,
    departure_addr VARCHAR(45),
    destination_addr VARCHAR(45),
    transport_cost FLOAT,
    PRIMARY KEY (transport_order_ID, shipyard_ID),
    FOREIGN KEY (shipyard_ID) REFERENCES Shipyard(shipyard_ID),
    FOREIGN KEY (team_ID) REFERENCES Team(team_ID)
);

CREATE TABLE Selling_Order (
	Selling_Order_ID INT,
    customer_ID INT,
    team_ID INT,
    `date` DATETIME,
    Shipping_address VARCHAR(45),
    money_amount INT,
    order_status VARCHAR(45),
    PRIMARY KEY (Selling_Order_ID),
    FOREIGN KEY (customer_ID) REFERENCES Customer(customer_ID),
    FOREIGN KEY (team_ID) REFERENCES Team(team_ID)
);

CREATE TABLE Selling_Order_Detail (
	Selling_Order_ID INT,
    Selling_Order_Detail_ID VARCHAR(45),
    buying_number INT,
    tire_ID INT,
    PRIMARY KEY (Selling_Order_ID, Selling_Order_Detail_ID),
    FOREIGN KEY (tire_ID) REFERENCES Tire_Information(tire_ID),
    FOREIGN KEY (Selling_Order_ID) REFERENCES Selling_Order(Selling_Order_ID)
);

CREATE TABLE Manufacturer_Detail (
	manu_detail_ID INT,
	manu_ID INT,
    tire_ID INT,
    manu_amount INT,
    PRIMARY KEY (manu_detail_ID),
    FOREIGN KEY (tire_ID) REFERENCES Tire_Information(tire_ID),
    FOREIGN KEY (manu_ID) REFERENCES Manufacturer(manu_ID)
);

CREATE TABLE Manu_Order (
	manu_order_ID INT,
    team_ID INT,
    manu_ID INT,
    `date` DATETIME,
    total_cost INT,
    PRIMARY KEY (manu_order_id),
    FOREIGN KEY (team_ID) REFERENCES Team(team_ID),
    FOREIGN KEY (manu_ID) REFERENCES Manufacturer(manu_ID)
);

CREATE TABLE Manu_Order_Detail (
	manu_order_detail_ID INT,
    manu_order_ID INT,
    tire_ID INT,
    manu_amount INT,
    PRIMARY KEY (manu_order_ID, manu_order_detail_ID),
    FOREIGN KEY (tire_ID) REFERENCES Tire_Information(tire_ID),
    FOREIGN KEY (manu_order_ID) REFERENCES Manu_Order(manu_order_ID)
);

CREATE TABLE Inventory (
	tire_ID INT,
    warehouse_ID INT,
    tire_storage_number INT,
    PRIMARY KEY (tire_ID, warehouse_ID),
    FOREIGN KEY (tire_ID) REFERENCES Tire_Information(tire_ID),
    FOREIGN KEY (warehouse_ID) REFERENCES Warehouse(warehouse_ID)
);

CREATE TABLE Transport_Order_Detail (
	transport_order_detail_id INT,
    transport_order_ID INT,
    warehouse_ID INT,
    tire_ID INT,
    selling_order_ID INT,
    transport_tire_num INT,
    PRIMARY KEY (transport_order_detail_id, transport_order_ID),
    FOREIGN KEY (transport_order_ID) REFERENCES Transport_order(transport_Order_ID),
    FOREIGN KEY (warehouse_ID) REFERENCES Warehouse(warehouse_ID),
    FOREIGN KEY (tire_ID) REFERENCES Tire_Information(tire_ID),
    FOREIGN KEY (selling_order_ID) REFERENCES Selling_Order(selling_order_ID)
);