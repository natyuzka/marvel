CREATE PROCEDURE dbo.added_comics
	   @digitalId int,
	   @title varchar(255),
	   @issueNumber int,
	   @variantDescription varchar(255),
	   @description varchar(255),
	   @modified varchar(255),
	   @isbn varchar(255),
	   @upc varchar(255),
	   @diamondCode varchar(255),	   
	   @ean varchar(255),
	   @issn varchar(255), 
	   @format varchar(255),
	   @pageCount int,
	   @textObjects varchar(255)
	 
AS
BEGIN
INSERT INTO [comics] (
	   	digitalid,
	   	title,
	   	issueNumber,
	   	variantDescription,
	 	description,
	 	modified,	   
		isbn,
	 	upc,
	 	diamondCode,
	 	ean,
	 	issn,	   
	 	format, 	
		pagecount,
	 	textObjects
	   )
    VALUES (
	 @digitalId,
	 @title,
	 @issueNumber,
	 @variantDescription,
	 @description,
	 @modified,	   
	 @isbn,
	 @upc,
	 @diamondCode,	   
	 @ean,
	 @issn,	   
	 @format,
	 @pageCount,
	 @textObjects
	   )
END