DROP TABLE IF EXISTS registrants;


CREATE TABLE registrants (
	id INTEGER,
	email TEXT NOT NULL,
	sport TEXT NOT NULL,
	PRIMARY KEY(id)
);

