create table user(
    id integer primary key autoincrement,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    hobbies text,
    active boolean not null default 1
);

create table vehicle(
    id integer primary key autoincrement,
    color varchar(45) not null,
    license_plate varchar(45) not null,
    v_type varchar(45),
    user_id integer not null,
    active boolean default 1,
    foreign key (v_type) references vehicle_type(id),
    foreign key (user_id) references user(id)

);

create table vehicle_type(
    id integer primary key autoincrement,
    description varchar(64)

);

/*Insertar esta info en la base de datos*/

/*USER*/
insert into user(first_name,last_name,hobbies) values ("Jaz","Salas","Read");
insert into user(first_name,last_name,hobbies) values ("Jojo","Zeta","Eat");
insert into user(first_name,last_name,hobbies) values ("Omar","Torres","Sing");
/*VEHICLE_TYPE*/
insert into vehicle_type(description) values ("bicycle");
insert into vehicle_type(description) values ("skateboards");
insert into vehicle_type(description) values ("car");
insert into vehicle_type(description) values ("motorcycle");
/*VEHICLE*/
insert into vehicle(color,license_plate,v_type,user_id) 
values("Gray","Type1",2,1);
insert into vehicle(color,license_plate,v_type,user_id) 
values("Green","Type2",3,2);
insert into vehicle(color,license_plate,v_type,user_id) 
values("Black","Type3",4,3);
insert into vehicle(color,license_plate,v_type,user_id) 
values("Gray","Type4",1,4);

/*CONSULTAS*/
--Mostrar la relacion de los ID de la tablas vehicle y User
select user.last_name,user.first_name,user.hobbies,user.active,
        vehicle.license_plate,vehicle.color,vehicle.v_type as vehicle_type
from user inner join vehicle
on user.id=vehicle.user_id;

--Mostrar la relacion entre las tres tablas
select user.last_name,user.first_name,user.hobbies,user.active,
        vehicle.license_plate,vehicle.color,
        vehicle.v_type as vehicle_type,vehicle_type.description
from user inner join vehicle on user.id=vehicle.user_id 
inner join vehicle_type
on vehicle.v_type = vehicle_type;