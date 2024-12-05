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
INSERT INTO Area (a_name) VALUES 
('Downtown'),
('Uptown'),
('Suburbs');

-- Insert data into Restaurant
INSERT INTO Restaurant (r_name, a_id) VALUES 
('Pizza Palace', 1),
('Sushi World', 2),
('Burger Haven', 3);

-- Insert data into Type
INSERT INTO Type (t_name) VALUES 
('Italian'),
('Japanese'),
('Fast Food');

-- Insert data into Restaurant_Types
INSERT INTO Restaurant_Types (r_id, t_id) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insert data into History
INSERT INTO History (h_id, u_id, r_id, Rate, Reviews, Date) VALUES 
(1, 1, 1, 4.5, 'Great pizza!', '2024-12-01'),
(2, 1, 2, 5.0, 'Amazing sushi!', '2024-12-02'),
(3, 2, 3, 3.0, 'Mediocre burgers.', '2024-12-03');



INSERT INTO Restaurant (r_name, a_id) VALUES
('KFC', 2);

INSERT INTO Restaurant_Types (r_id, t_id) VALUES
(4, 3);
