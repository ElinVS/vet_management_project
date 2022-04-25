DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    speciality VARCHAR(255) NOT NULL
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone_number VARCHAR(255) NOT NULL,
    adress VARCHAR(255) NOT NULL,
    postcode VARCHAR (255) NOT NULL,
    registered BOOLEAN
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    species VARCHAR(255) NOT NULL,
    dob VARCHAR(255) NOT NULL,
    treatment_notes TEXT,
    owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT NOT NULL REFERENCES vets(id)

);

