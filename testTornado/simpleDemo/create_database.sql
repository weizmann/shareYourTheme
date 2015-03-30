create database share_theme;
use share_theme;

create table share_theme_account (
		account_id 		varchar(128),
		email 			varchar(128),
		auth_token		varchar(128),
		gender			tinyint(4),
		register_time	bigint(20),
		primary key 	(account_id),
);

create table theme_upload_op 
(
		op_id			bigint(20) auto_increment,
		foreign key		(account_id) 	references share_theme_account(account_id),
		op_time			bigint(20),
		file_path		varchar(128),
		primary key		op_id,
);

create table theme_download_op 
(
		op_id			bigint(20) auto_increment,
		foreign key		(account_id)	references share_theme_account(account_id),
		op_time			bigint(20),
		source_op_id	bigint(20),
		primary key		op_id,
);
