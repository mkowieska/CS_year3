create table musicalbum
(
    id      integer not null
        constraint musicalbum_pk
            primary key autoincrement,
    subject text not null,
    content text not null
);
