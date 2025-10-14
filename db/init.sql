create database db_poo;

use db_poo;

CREATE TABLE empleado (
  id int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  telefono varchar(50) NOT NULL,
  email varchar(50) NOT NULL,
  direccion varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into empleado(nombre,telefono,email, direccion)
values ('Elias Año Mendoza','999888777','elias@abc.com', 'Av. Aviacion 2345');
