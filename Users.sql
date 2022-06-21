CREATE TABLE Users (
    [id] int,
    [Username] varchar(255),
    [Password] varchar(255)

);

SELECT * FROM Users

-- INSERT INTO Users 
-- ([email])
-- VALUES
-- (1, 'Landon', 'generate_password_hash("HelloWorld,01")'),
-- (2, 'Kristina', 'generate_password_hash("HelloWorld,01")')

-- ALTER TABLE Users
-- Set [Password] = generate_password_hash('HelloWorld,01')
-- WHERE [id] = 1

UPDATE Users
SET [Location] = 'Istanbul, Turkey'
WHERE [id] = 2