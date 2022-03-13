create table user(
    id integer primary key autoincrement,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    hobbies text,
    active boolean not null default 1
);

/*Insertar esta info en la base de datos*/
insert into user(first_name,last_name,hobbies) values ("Jaz","Salas","Read");
insert into user(first_name,last_name,hobbies) values ("Jojo","Zeta","Eat");
insert into user(first_name,last_name,hobbies) values ("Omar","Torres","Sing");


