Drop table if exists female_boston ; 
Drop table if exists male_boston ; 


create table female_boston(
	
	Year int,
	Athlete varchar(30) not null,
	Country VARCHAR(30) not null,
	Time Time not null 
)
	
create table male_boston(
    id int primary key ,
	Year int,
	Athlete varchar(30) not null,
	Country VARCHAR(30) not null,
	Time Time not null 
)

select * from female_boston
select * from male_boston

-- complete 