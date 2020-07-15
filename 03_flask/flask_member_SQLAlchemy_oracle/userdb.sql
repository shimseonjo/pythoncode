create sequence seq_users;

create table users (
  userid varchar2(50) not null,
  userpw varchar2(50) not null,
  username varchar2(50) not null,
  userage number(5,0) ,
  usermail varchar2(50), 
  useradd varchar(50),
  usergender varchar(20),
  usertel varchar(20)
);

alter table users add constraint pk_users 
primary key (userid);


insert into users values(
'hong',
'1234',
'홍길동',
23,
'hong@gmail.com',
'부산시 동구 수정동',
'male',
'010-1234-1234');

select * from users;