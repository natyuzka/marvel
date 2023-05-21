CREATE PROCEDURE dbo.added_characters
	   @name varchar(20),
	   @description varchar(255),
	   @modified varchar(255),
	   @thumbnail varchar(255)
AS
BEGIN
INSERT INTO [character]  (
	   name,
	   description,
	   modified,
	   thumbnail
	   )
    VALUES (
	   @name,
	   @description,
	   @modified,
	   @thumbnail
	   )
END