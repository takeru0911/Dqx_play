# --- Created by Ebean DDL
# To stop Ebean DDL generation, remove this comment and start using Evolutions

# --- !Ups

create table category (
  id                        bigint auto_increment not null,
  category_name             varchar(255),
  constraint pk_category primary key (id))
;

create table item (
  id                        bigint auto_increment not null,
  name                      varchar(255),
  design_id                 bigint,
  category_id               bigint,
  url                       varchar(255),
  constraint pk_item primary key (id))
;







