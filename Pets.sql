
ALTER TABLE Pets
ADD [Missingid] int


SELECT * FROM Pets

INSERT INTO Pets 
([id], [Name], [Age], [Picture], [Status], [Species])
VALUES
(1, 'Snowfall', 11, null, 'missing', 'Dog'),
(2, 'Halo', 6, null, 'lost', 'Dog')

UPDATE Pets
SET [Status] = 'Missing'
Where [id] = '2'

