create table post
(
    id    integer not null
        primary key,
    text  text    not null,
    topic text
);

alter table post
    owner to karpov;

grant select on post to "robot-redash";

grant select on post to "robot-startml-ro";

