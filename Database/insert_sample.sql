-- Insert data into Users
INSERT INTO Users (Name) VALUES 
('Alice'),
('Bob'),
('Charlie');

-- Insert data into Blacklist
INSERT INTO Blacklist (b_id, u_id, date) VALUES 
(1, 2, '2024-12-01'),
(2, 3, '2024-11-28');

-- Insert data into Area
INSERT INTO Area (a_id, a_name) VALUES 
(101, 'Downtown'),
(102, 'Uptown'),
(103, 'Suburbs');

-- Insert data into Restaurant
INSERT INTO Restaurant (r_id, r_name, a_id) VALUES 
('100A', 'Pizza Palace', 101),
('100B', 'Sushi World', 102),
('100C', 'Burger Haven', 103);

-- Insert data into Type
INSERT INTO Type (t_id, t_name) VALUES 
(1001, 'Italian'),
(1002, 'Japanese'),
(1003, 'Fast Food');

-- Insert data into Restaurant_Types
INSERT INTO Restaurant_Types (r_id, t_id) VALUES 
('100A', 1001),
('100B', 1002),
('100C', 1003);

-- Insert data into History
INSERT INTO History (h_id, u_id, r_id, Rate, Reviews, Date) VALUES 
(1, 1, '100A', 4.5, 'Great pizza!', '2024-12-01'),
(2, 1, '100B', 5.0, 'Amazing sushi!', '2024-12-02'),
(3, 2, '100C', 3.0, 'Mediocre burgers.', '2024-12-03');



INSERT INTO Restaurant (r_id, r_name, a_id) VALUES
('100D', 'KFC', 102);

INSERT INTO Restaurant_Types (r_id, t_id) VALUES
('100D', 1001);
