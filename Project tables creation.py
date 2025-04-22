import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='sqllog', database='DC')
c = conn.cursor()

c.execute('''
CREATE TABLE CUSTOMERS (
    Cust_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Contact_No VARCHAR(15) NOT NULL,
    Email VARCHAR(100),
    Address VARCHAR(500)
)
''')

c.execute('''
CREATE TABLE COMPANIES (
    Company_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    Contact_No VARCHAR(15),
    Email VARCHAR(100)
)
''')

c.execute('''
CREATE TABLE DELIVERY_PERSONNEL (
    Personnel_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Contact_No VARCHAR(15) NOT NULL,
    Vehicle_No VARCHAR(20)
)
''')

c.execute('''
CREATE TABLE ORDERS (
    Order_ID INT AUTO_INCREMENT PRIMARY KEY,
    Cust_ID INT NOT NULL,
    Personnel_ID INT,
    Order_Date DATE NOT NULL,
    Total_Amount DECIMAL(10, 2) NOT NULL,
    Delivery_Status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (Cust_ID) REFERENCES CUSTOMERS(Cust_ID)
)
''')

c.execute('''
CREATE TABLE ADMINS (
    Name VARCHAR(20),
    Pwd VARCHAR(100)
)
''')

conn.commit()

c.execute('''
INSERT INTO CUSTOMERS (Name, Contact_No, Email, Address) VALUES
('Arjun Sharma', '9876543210', 'arjun.sharma@gmail.com', '123 MG Road, Mumbai, Maharashtra'),
('Meera Patel', '9876512345', 'meera.patel@yahoo.com', '45 Ring Road, Ahmedabad, Gujarat'),
('Ravi Kumar', '9876509876', 'ravi.kumar@hotmail.com', '89 GT Road, Varanasi, Uttar Pradesh'),
('Anjali Gupta', '9876587654', 'anjali.gupta@rediffmail.com', '221B Baker Street, Bengaluru, Karnataka'),
('Mohan Das', '9876598765', 'mohan.das@gmail.com', '12 Civil Lines, Jaipur, Rajasthan'),
('Sneha Iyer', '9876565432', 'sneha.iyer@gmail.com', '56 MG Road, Chennai, Tamil Nadu'),
('Ramesh Singh', '9876554321', 'ramesh.singh@yahoo.com', '32 Lajpat Nagar, Delhi'),
('Kavya Menon', '9876578901', 'kavya.menon@live.com', '76 Hill View Colony, Kochi, Kerala'),
('Rohit Mehta', '9876548765', 'rohit.mehta@gmail.com', '54 Palm Beach Road, Navi Mumbai, Maharashtra'),
('Pooja Verma', '9876523456', 'pooja.verma@gmail.com', '11 Rose Garden, Chandigarh'),
('Amit Jain', '9876590123', 'amit.jain@yahoo.com', '23 Nariman Point, Mumbai, Maharashtra'),
('Neha Kapoor', '9876589012', 'neha.kapoor@rediffmail.com', '75 Anna Salai, Chennai, Tamil Nadu'),
('Varun Bhardwaj', '9876567890', 'varun.bhardwaj@gmail.com', '98 Rajpur Road, Dehradun, Uttarakhand'),
('Priya Reddy', '9876540123', 'priya.reddy@yahoo.com', '45 Jubilee Hills, Hyderabad, Telangana');
''')

c.execute('''
INSERT INTO COMPANIES (Name, Address, Contact_No, Email) VALUES
('Reliance Retail Ltd', 'Mumbai, Maharashtra', '02212345678', 'contact@reliance.com'),
('Future Group', 'Bengaluru, Karnataka', '08012345678', 'info@futuregroup.com'),
('Tata Consumer Products', 'Kolkata, West Bengal', '03312345678', 'support@tataconsumer.com'),
('HUL Limited', 'Chennai, Tamil Nadu', '04412345678', 'helpdesk@hul.com'),
('Aditya Birla Retail', 'Pune, Maharashtra', '02012345678', 'connect@abrl.com'),
('BigBasket Pvt Ltd', 'Hyderabad, Telangana', '04012345678', 'hello@bigbasket.com'),
('Zomato Delivery', 'Gurgaon, Haryana', '01241234567', 'care@zomato.com'),
('Swiggy', 'Bengaluru, Karnataka', '08087654321', 'support@swiggy.com'),
('Flipkart Pvt Ltd', 'Bengaluru, Karnataka', '08065432178', 'help@flipkart.com'),
('Amazon India', 'Hyderabad, Telangana', '04065432189', 'support@amazon.in'),
('ITC Foods', 'Kolkata, West Bengal', '03376543210', 'care@itcfoods.com'),
('DMart', 'Mumbai, Maharashtra', '02276543211', 'contact@dmartindia.com'),
('Spencer''s Retail', 'Kolkata, West Bengal', '03365498765', 'info@spencers.in'),
('Grofers India', 'Delhi, NCR', '01154321098', 'hello@grofers.com');
''')

c.execute('''
INSERT INTO DELIVERY_PERSONNEL (Name, Contact_No, Vehicle_No) VALUES
('Rakesh Yadav', '9876543210', 'MH12AB1234'),
('Sunil Sharma', '9876512345', 'KA03XY5678'),
('Priya Nair', '9876509876', 'TN09AC3456'),
('Ajay Gupta', '9876587654', 'AP31RT6789'),
('Vikas Verma', '9876598765', 'RJ27UV2345'),
('Sheetal Jain', '9876565432', 'WB02BA6789'),
('Rahul Mishra', '9876554321', 'UP32CD1234'),
('Pankaj Singh', '9876578901', 'TS08XY5678'),
('Ankit Sahu', '9876548765', 'DL4SU8901'),
('Sneha Reddy', '9876523456', 'HR26XX5678'),
('Manoj Iyer', '9876590123', 'GJ01AD3456'),
('Anjali Das', '9876589012', 'MP09CD5678'),
('Tarun Menon', '9876567890', 'CG07RT2345'),
('Deepak Jain', '9876540123', 'PB10XY6789');
''')

c.execute('''
INSERT INTO ADMINS (Name, Pwd) VALUES
('admin1', '1234abcd'),
('admin2', 'securePwd@5678'),
('admin3', 'Admin@2024'),
('admin4', 'password123'),
('admin5', 'admin!4567'),
('admin6', 'rootAccess#1'),
('admin7', 'pass@Admin'),
('admin8', 'secure@key'),
('admin9', 'qwerty@2024'),
('admin10', 'passcode#789'),
('admin11', 'superUser!123'),
('admin12', 'tempPass2024'),
('admin13', 'login@secure'),
('admin14', 'defaultAdmin');
''')

c.execute('''
INSERT INTO ORDERS (Cust_ID, Personnel_ID, Order_Date, Total_Amount, Delivery_Status) VALUES
(1, 1, '2024-11-01', 1500.00, 'Delivered'),
(2, 2, '2024-11-02', 2000.00, 'Pending'),
(3, 3, '2024-11-03', 750.50, 'Shipped'),
(4, 4, '2024-11-04', 999.99, 'Cancelled'),
(5, 5, '2024-11-05', 3000.00, 'Pending'),
(6, 6, '2024-11-06', 4500.75, 'Delivered'),
(7, 7, '2024-11-07', 800.00, 'Shipped'),
(8, 8, '2024-11-08', 2200.00, 'Delivered'),
(9, 9, '2024-11-09', 670.25, 'Pending'),
(10, 10, '2024-11-10', 1200.00, 'Shipped'),
(11, 11, '2024-11-11', 1800.00, 'Delivered'),
(12, 12, '2024-11-12', 2400.50, 'Shipped'),
(13, 13, '2024-11-13', 950.75, 'Pending'),
(14, 14, '2024-11-14', 3999.99, 'Delivered');
''')

conn.commit()
