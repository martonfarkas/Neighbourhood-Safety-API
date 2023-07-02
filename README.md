# MartonFarkas_T2A2

[Github](https://github.com/martonfarkas/Neighbourhood-Safety-API)

[Trello](https://trello.com/b/r7kmcGjk/neighbourhood-safety-api)

# App Install and Setup

- Connect to a PostgreSQL database from the Flask application. Run the PostgreSQL prompt in the terminal: psql

- Create the database: create database nsafety;

- Connect to the database: \c nsafety;

- Create user and set a temporary password as: create user nsafety_dev with password 'abcd1234';

- Grant user priviliges: grant all privileges on database nsafety to nsafety_dev;

- In WSL command line create a virtual environment:
    python3 -m venv .venv
    source .venv/bin/activate

- Install dependant packages: pip3 install -r requirements.txt

- python3 -m flask db create

- python3 -m flask db seed

- python3 -m flask run

- Rename the .env.sample to .env and set the database connection stream and the JWT secret key: 
DB_URI=postgresql+psycopg2://api_dev:password123@127.0.0.1:8000/coder_academy_db
JWT_KEY=Example Key

# Neighbourhood Safety API

## Planning:

### R1 Identification of the problem you are trying to solve by building this particular app

- The neighborhood safety app addresses the challenge of keeping residents informed in matters of safety within their community. By providing a user-friendly platform, the app aims to enable residents to report safety incidents, access relevant information, and receive alerts.

The app seeks to create a sense of security by allowing users to report incidents they encounter. This reporting feature helps create a comprehensive database of incidents specific to the neighborhood, contributing to a better understanding of safety patterns and trends.

Through the app, residents can access valuable information about incidents that have occurred in their vicinity. By visualizing incident locations on a map and providing details such as incident descriptions and dates, users gain awareness of the safety landscape in their neighborhood.

Furthermore, the app facilitates communication by sending alerts to users regarding significant safety incidents or developments.

The app encourages residents to actively engage in reporting incidents and sharing information. This active involvement contributes to a stronger sense of community, as neighbours work together to create a safer living environment.

### R2 Why is it a problem that needs solving?

- The lack of information can create a sense of uncertainty and vulnerability among residents. Without access to real-time updates and incident reports, residents may be unaware of potential risks or ongoing safety issues in their neighborhood.

This problem becomes particularly significant when it comes to personal safety and the protection of property. Residents need to be informed about incidents such as burglaries, assaults, or other criminal activities that may pose a threat to their well-being. Timely information allows residents to take necessary precautions, such as avoiding certain areas or increasing security measures.

### R3 Why have you chosen this database system. What are the drawbacks compared to others?

- PostgreSQL is a popular database system due to its robustness, scalability, and extensive feature set. 

PostgreSQL enforces strong data integrity through constraints, foreign key relationships, and transactional support.
It supports a wide range of data types, including JSON, arrays, and custom types. It also offers advanced features such as stored procedures and user-defined functions, allowing for complex data processing and manipulation.
It allows developers to create custom extensions and integrate them seamlessly into the database. This enables additional functionality and customization specific to the application's needs.
It has optimizations for query execution and indexing, allowing for efficient retrieval and manipulation of data. It also supports parallel query execution and provides various performance tuning options.
It is the most common open source database system which tell us it's very reliable.
Once you  get the grasp of it it's really easy to use especially combined with Python. 
PostgreSQL can manage large data and queries which suits for this application.

![psql](/docs/psql1.png)

PostgreSQL have some drawbacks compared to other database systems:

It can be more complex to set up and configure compared to simpler databases like SQLite or MySQL. It may require more expertise to optimize performance and manage advanced features.
Memory usage can be higher compared to some other databases, especially when handling large datasets. This may require careful resource management.
If developers are more familiar with other databases like MySQL, they may need to learn the specific syntax and features of PostgreSQL.
While PostgreSQL offers replication and sharding capabilities, they might not be as straightforward to set up and manage compared to some dedicated distributed databases. Although it has some drawback the pros are outweigh the negatives. I choose this as it's easy to use robust and reliable and it is very compatible with Python which makes developing my API easier.

[Reference](https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/)

[Reference2](https://cloudinfrastructureservices.co.uk/mysql-vs-postgresql/)

[Reference3](https://www.percona.com/blog/why-postgresql-is-a-top-choice-for-enterprise-level-databases/#:~:text=PostgreSQL%20uses%20a%20multi%2Dversion,without%20downtime%20or%20data%20loss.)

### R4 Identify and discuss the key functionalities and benefits of an ORM

- An Object-Relational Mapping (ORM) is a technique that allows developers to interact with a relational database using object-oriented programming principles. It provides a way to map database tables to classes, database records to objects, and database queries to object-oriented queries. 

- ORM frameworks simplify database interaction by abstracting low-level database operations, such as SQL queries and result set handling. Developers can work with higher-level abstractions like objects, classes, and methods, reducing the need for writing repetitive and error-prone SQL code.

- The main functionality of an ORM is to map database tables to classes and database records to objects. This allows developers to leverage familiar object-oriented concepts and techniques like inheritance, polymorphism, and encapsulation in their database operations.

- ORM frameworks provide a level of database abstraction, enabling developers to write database-independent code. Switching between different database systems (e.g., PostgreSQL, MySQL, SQLite) becomes easier as the ORM handles the database-specific operations and translates them accordingly.

- ORMs often include built-in data validation mechanisms to ensure data integrity and consistency when saving or retrieving from the database. They also offer type safety, allowing developers to work with strongly typed objects and reducing the chances of runtime errors.

- ORMs offer query building capabilities, allowing developers to construct complex database queries using a fluent interface or an object-oriented syntax. ORM frameworks often incorporate query optimization techniques, such as lazy loading and eager loading, to minimize the number of database queries and enhance performance.
Automatic Schema Generation and Migration: ORMs can automatically generate database schemas based on class structures, eliminating the need for manual schema creation. They also support database schema migration, enabling seamless changes to the database schema as the application evolves.

- ORMs provide mechanisms for defining and managing relationships between objects and database tables, such as one-to-one, one-to-many, many-to-one, and many-to-many relationships. This simplifies handling complex data relationships and eliminates the need for manual JOIN operations.

- By abstracting database operations, handling repetitive tasks, and offering higher-level abstractions, ORMs significantly increase developer productivity. Developers can focus more on application logic and business requirements rather than dealing with low-level database interactions.

- ORM frameworks promote code reusability by encapsulating database-related code within models or entities. These reusable components can be utilized across different parts of the application, making it easier to maintain and modify the codebase.

- ORMs facilitate unit testing and debugging by allowing developers to work with in-memory databases or mock data sources. This enables easier testing of database-related functionality and reduces dependencies on the actual database during development and testing.

- By abstracting database operations and providing built-in security features, ORM frameworks enhance the overall security of an application and reduce the risk of data breaches or unauthorized access.

- However, ORM also has some limitations, particularly in handling complex queries and aggregations that require high performance and flexibility. One of the drawbacks of using ORM is that it may generate inefficient or suboptimal SQL queries. These queries can result in poor performance, excessive memory usage, or unexpected errors. For instance, ORM might execute multiple queries instead of using a single join, retrieve more data than necessary, or utilize inappropriate indexes or functions.

Another limitation of ORM is that it can restrict your control and customization over SQL queries and operations. This limitation makes it challenging to optimize queries for specific scenarios or requirements. Certain advanced features or functions of the database, such as stored procedures, triggers, or views, may not be fully supported by the ORM. Using these features might require additional code or configuration.

It's important to be aware of these limitations when using ORM and consider them when dealing with complex or performance-critical database operations. In some cases, directly writing SQL queries or utilizing other database-specific tools may be more suitable to achieve optimal performance and flexibility.


[Reference](https://dev.to/tinazhouhui/introduction-to-object-relational-mapping-the-what-why-when-and-how-of-orm-nb2)

[Reference](https://www.fullstackpython.com/object-relational-mappers-orms.html)

### R5 Document all endpoints for your API

- All data is in Json format

1. Alerts:

- Method [GET]
- /alerts
- get all alerts

![alerts](/docs/alerts.png)

- Method [GET]
- alert_id
- get one alert

![one_alert](/docs/alerts%3A1.png)

2. Locations:

- Method [GET]
- /locations
- get locations

![locations](/docs/locations.png)

- Method [GET]
- location_id
- get one location

![one_location](/docs/locations%3A1.png)

Incidents:

- Method [GET]
- /incidents
- get all incidents

![incidents](/docs/incidents.png)

- Method [GET]
- incident_id
- get one incident

![one_incident](/docs/incidents%3A1.png)

- Method [POST]
- user_id
- Authentication: @jwt_required()
- create incident

![create_incident](/docs/create_incident.png)

- Method [PUT,PATCH]
- user_id
- Authentication: @jwt_required()
- update incident

![update_incident](/docs/update_incident.png)

- Method [DELETE]
- user_id
- Authentication: @jwt_required()
- delete incident

![delete_incident](/docs/delete_incident.png)

Users:

- Method [GET]
- /auth/users
- get all users

![users](/docs/auth%3Ausers%20first.png)

- Method [GET]
- user_id
- get one user

![one_user](/docs/auth%3Ausers%3A1%20first%20half.png)

- Method [POST]
- Identifier: none
- Authentication: Password Hashed with the use of Bcrypt
- register new user

![register_user](/docs/register_user.png)

![new_user](/docs/newuser.png)

- Method [POST]
- Identifier: email
- Authentication: email and password
- Token: generated with JWT
- login user

![login_user](/docs/login_succes.png)

![login_token](/docs/login_success_token.png)

### R6 An ERD for your app

![ERD](/docs/ERD.png)

### R7 Detail any third party services that your app will use

- Flask-JWT-Extended: Flask-JWT-Extended is an extension that enhances JWT (JSON Web Token) support in Flask applications. JWT is a popular standard for representing claims between two parties, commonly used for authentication and authorization purposes. Flask-JWT-Extended simplifies the creation, validation, and management of JWTs in Flask applications. It provides decorators for protecting routes with JWT-based authentication, allows the configuration of various token options, and integrates well with Flask's request handling.

- Flask-Bcrypt: Flask-Bcrypt is an extension that integrates the bcrypt hashing algorithm with Flask. Bcrypt is a widely used and secure algorithm for hashing passwords. With Flask-Bcrypt, you can easily hash passwords and verify them during user authentication. It provides a simple interface for generating secure password hashes and comparing them with stored hashes, protecting user passwords from unauthorized access.

- Flask-SQLAlchemy: Flask-SQLAlchemy is an extension that provides integration between Flask and SQLAlchemy, a powerful Object-Relational Mapping (ORM) library. SQLAlchemy abstracts the database operations and allows you to interact with databases using Python objects and methods, rather than writing raw SQL queries. Flask-SQLAlchemy simplifies the setup and configuration of SQLAlchemy within a Flask application and provides convenient features for database access and management.

- Flask-Marshmallow: Flask-Marshmallow is an extension that integrates Marshmallow with Flask. Marshmallow is a library for object serialization and deserialization, commonly used for validating and transforming data between different formats, such as JSON and Python objects. With Flask-Marshmallow, you can define schemas to serialize and deserialize objects, validate input data, and control the output format of responses.

- Python dotenv: Python dotenv is a Python library that allows you to manage environment variables in your Python applications by loading them from a .env file. An environment variable is a key-value pair that holds configuration settings or sensitive information needed by your application, such as database credentials, API keys, or other configuration parameters.

- Psycopg2 is a PostgreSQL adapter for the Python programming language. It provides a Python interface to interact with PostgreSQL databases, allowing you to perform various database operations such as connecting to a database, executing SQL queries, and handling query results.

### R8 Describe your projects models in terms of the relationships they have with each other

- In my application, I have several models representing different entities

- User and Incident Relationship:
In the User model, there is a one-to-many relationship with the Incident model. This is represented by the incidents relationship field.
The User model has a foreign key user_id in the Incident model, which establishes the relationship between the two models.
The relationship is defined using db.relationship('Incident', back_populates='user') in the User model.
The corresponding relationship is defined in the Incident model as user = db.relationship('User', back_populates='incidents').
Each User can have multiple Incidents associated with them. The User model keeps track of these incidents through a field called "incidents. For example, you can retrieve all incidents for a specific user or add new incidents to a user.

- User and Location Relationship:
In the User model, there is a one-to-one relationship with the Location model. This is represented by the location relationship field.
The User model has a foreign key user_id in the Location model, which establishes the relationship between the two models.
The relationship is defined using db.relationship('Location', back_populates='user', uselist=False) in the User model.
The corresponding relationship is defined in the Location model as user = db.relationship('User', back_populates='location', uselist=False).
This means that each user can have only one associated location, and the User model keeps track of this location through a field called "location. For example, you can retrieve the location of a user or assign a location to a user.

- User and Alert Relationship:
In the User model, there is a one-to-many relationship with the Alert model. This is represented by the alerts relationship field.
The User model has a foreign key user_id in the Alert model, which establishes the relationship between the two models.
The relationship is defined using db.relationship('Alert', back_populates='user') in the User model.
The corresponding relationship is defined in the Alert model as user = db.relationship('User', back_populates='alerts').
Each User can have multiple Alerts associated with them. The User model keeps track of these alerts through a field called "alerts. For example, you can retrieve all alerts for a specific user or create new alerts for a user.

- Location and Incident Relationship:
In the Location model, there is a one-to-many relationship with the Incident model. This is represented by the incidents relationship field.
The Location model has a foreign key location_id in the Incident model, which establishes the relationship between the two models.
The relationship is defined using db.relationship('Incident', back_populates='location') in the Location model.
The corresponding relationship is defined in the Incident model as location = db.relationship('Location', back_populates='incidents').
Each Location can have multiple Incidents associated with it. The Location model keeps track of these incidents through a field called incidents. For example, you can retrieve all incidents for a specific location or add new incidents to a location.

- Alert and Incident Relationship:
In the Alert model, there is a one-to-many relationship with the Incident model. This is represented by the incidents relationship field.
The Alert model has a foreign key alert_id in the Incident model, which establishes the relationship between the two models.
The relationship is defined using db.relationship('Incident', back_populates='alert', cascade='all, delete') in the Alert model.
The corresponding relationship is defined in the Incident model as alert = db.relationship('Alert', back_populates='incidents').
Each Alert can be associated with multiple Incidents. The Alert model keeps track of these incidents through a field called "incidents. For example, you can retrieve all incidents related to a specific alert or assign incidents to an alert.

- These relationships define the associations between the models in the database schema. They allow you to navigate between related objects and perform queries involving multiple models. The relationship fields provide convenient access to related data and enable the ORM to manage the database relationships effectively.

![User](/docs/userrel.png)

![Location](/docs/locationrel.png)

![Incident](/docs/incidentrel.png)

![Alert](/docs/alertrel.png)

### R9 Discuss the database relations to be implemented in your application

- My API has a database called nsafety which has 4 tables(user, location, incident, alert).

- User table:

The User model represents a user of the system.

Each item from the table represents a column.
Each user has a unique ID, which is important for authorization purposes.
The user's name represents their full name.
The email column serves as the unique identifier for each user. It must be unique and cannot be null.
The city column represents the city where the user is located.
The address column stores the user's specific address within the city.
The password column stores the encrypted and hashed password. It cannot be null.
Upon login with a valid email and password, a token is generated for the user, and the user's ID is stored in memory for data manipulation purposes, such as reporting incidents.
Each user has a single location associated with them, storing their city and address information.
The User model has a one-to-many relationship with the Incident model, allowing a user to have multiple incidents associated with their ID.
The User model also has a one-to-many relationship with the Alert model, enabling a user to receive multiple alerts associated with their ID.

- Location table:

The Location table represents the location information associated with a user.

The table has the following columns:
id: An integer column representing the unique ID of the location.
city: A string column representing the city where the location is situated.
address: A string column representing the specific address within the city.
Relationships:
Many-to-One with User: Each location belongs to a single user.
One-to-Many with Incident: Each location can have multiple incidents associated with it.

- Incident table:

The Incident table represents an incident reported by a user.

The table has the following columns:
id: An integer column representing the unique ID of the incident.
description: A text column containing the description of the incident.
date_time: A datetime column representing the date and time when the incident occurred.
Relationships:
An incident is associated with one user, one location, and one alert (optional).
The Incident model has a many-to-one relationship with the User model, as a user can have multiple incidents.
It also has a many-to-one relationship with the Location model, as multiple incidents can occur at the same location.
Additionally, it has a many-to-one relationship with the Alert model, as an incident can be associated with an alert.

- Alert table:

The Alert table represents an alert generated in the system.

The table has the following columns:
id: An integer column representing the unique ID of the alert.
alert_message: A string column containing the message of the alert.
Relationships:
The Alert model represents an alert associated with a user.
Each item from the table represents a column.
Each alert has a unique ID and an alert message.
An alert is associated with one user.
The Alert model has a many-to-one relationship with the User model, as a user can have multiple alerts.
It also has a one-to-many relationship with the Incident model, as multiple incidents can be associated with the same alert.

- These models and their relationships allow for the representation of users, incidents, locations, and alerts in the system, providing the necessary associations between them.

### R10 Describe the way tasks are allocated and tracked in your project

- A to do list in trello whit due dates helped me a lot. Once I clicked on it and could see it straight away if something was overdue or something was done.

![trello1](/docs/trello1.png)

![trello2](/docs/trello2.png)

![trello3](/docs/trello3.png)

![trello4](/docs/trello4.png)

![trello5](/docs/trello5.png)

 - Daily stand-ups helped me a lot to track my progress because before writing it I had to think it through what I had done and what was my struggle and also plans for the next day. What I learnt that day motivated me that I either learnt or solved something beacuse I belive that is the best way to learn and improve my skills in the future and develop a problem solving thinking.

 ![stand-up](/docs/standup.png)

#### User stories:

User story 1:

- As a user, I want to report an incident with detailed information, so that it can be recorded accurately:

Description: As a user, I should be able to provide a detailed description of the incident, including relevant information such as the type of incident, date and time, and any additional details.

Acceptance criteria: The app should have a form or interface where I can input the incident details. It should validate the required fields and allow me to submit the report.

User story 2:

- As a user, I want to receive alerts about incidents in my area, so that I can stay informed and take necessary precautions:

Description: As a user, I should be able to subscribe to alerts based on my location. Whenever there is an incident reported in my area, I want to receive notifications or alerts on my preferred communication channel (e.g., email, mobile app push notification).

Acceptance criteria: The app should allow me to set my preferred location or use my current location to receive relevant alerts. It should have a mechanism to send notifications or display alerts in real-time whenever a new incident is reported in my subscribed area.

User story 3:

- As a user, I want to view the incident history and details, so that I can have access to the information for reference or awareness:

Description: As a user, I should be able to access a list or map view of past incidents, along with their details such as description, date and time, and location. This will allow me to browse through the incident history and gather information about previous incidents.

Acceptance criteria: The app should provide a user-friendly interface where I can navigate through the incident history. It should display relevant information about each incident, such as description, date and time, and location. Additionally, it should allow me to search or filter incidents based on specific criteria if needed.

![userstory1](/docs/userstory1.png)

![userstory2](/docs/userstory2.png)

![userstory3](/docs/userstory3.png)