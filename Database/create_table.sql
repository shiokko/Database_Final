-- Create Users table
CREATE TABLE Users (
    u_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);

-- Create Blacklist table
CREATE TABLE Blacklist (
    b_id INTEGER NOT NULL,
    u_id INTEGER NOT NULL,
    date DATETIME NOT NULL,
    PRIMARY KEY (b_id, u_id),
    FOREIGN KEY (u_id) REFERENCES Users (u_id)
);

-- Create Area table
CREATE TABLE Area (
    a_id INTEGER PRIMARY KEY AUTOINCREMENT,
    a_name TEXT NOT NULL
);

-- Create Restaurant table
CREATE TABLE Restaurant (
    r_id TEXT PRIMARY KEY,
    r_name TEXT NOT NULL,
    a_id INTEGER NOT NULL,
    FOREIGN KEY (a_id) REFERENCES Area (a_id)
);

-- Create Type table
CREATE TABLE Type (
    t_id INTEGER PRIMARY KEY,
    t_name TEXT NOT NULL
);

-- Create Restaurant_Types table
CREATE TABLE Restaurant_Types (
    r_id TEXT NOT NULL,
    t_id INTEGER NOT NULL,
    PRIMARY KEY (r_id, t_id),
    FOREIGN KEY (r_id) REFERENCES Restaurant (r_id),
    FOREIGN KEY (t_id) REFERENCES Type (t_id)
);

-- Create History table
CREATE TABLE History (
    h_id INTEGER NOT NULL,
    u_id INTEGER NOT NULL,
    r_id TEXT NOT NULL,
    Rate REAL NOT NULL,
    Reviews TEXT,
    Date DATETIME NOT NULL,
    PRIMARY KEY (h_id, u_id),
    FOREIGN KEY (u_id) REFERENCES Users (u_id),
    FOREIGN KEY (r_id) REFERENCES Restaurant (r_id)
);

