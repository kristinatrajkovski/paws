CREATE TABLE Missing (
    [Location] varchar(255),
    [Time] DateTime,
    [ContactInfo] varchar(255),
    [Breed] varchar(255)

);

SELECT * FROM Missing

ALTER TABLE Missing
ADD [id] int

INSERT INTO Missing
    ([Location], [Time], [ContactInfo], [Breed], [id])
VALUES
    ('Virginia Beach, VA 23462, USA', '2022-06-20 16:00:00', '757-995-4982', 'maltese', 1)