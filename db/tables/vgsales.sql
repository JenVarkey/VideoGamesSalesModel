drop table if exists vgsales;
create table vgsales
(
    rank            int,
    name            varchar(512),
    platform        varchar(128),
    Year            int,
    genre           varchar(128),
    publisher       varchar(128),
    na_Sales        decimal,
    eu_Sales        decimal,
    gp_Sales        decimal,
    other_Sales     decimal,
    global_Sales    decimal
)