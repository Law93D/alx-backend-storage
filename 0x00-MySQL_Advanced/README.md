# MySQL Advanced Project

This project contains SQL scripts for various tasks related to advanced MySQL operations.

## Project Overview

This repository includes scripts tailored for Ubuntu 18.04 LTS and MySQL 5.7.30. Each SQL file addresses specific tasks with detailed comments and adheres to formatting guidelines.

## Project Structure

- `0-create_users_table.sql`: Creates a 'users' table with primary key.
- `1-insert_data.sql`: Inserts sample data into the 'users' table.
- `2-query_users.sql`: Retrieves user information from the 'users' table.

## Execution Instructions

To execute these scripts:

1. Ensure MySQL 5.7.30 is installed and running on Ubuntu 18.04 LTS.
2. Clone this repository and navigate to the project directory.
3. Execute each SQL file using the MySQL command line interface:
   
   ```bash
   mysql -u username -p < filename.sql
### Final Notes

- Replace `username` in the execution command with your MySQL username.
- Customize the sample data and queries as per your specific requirements.
- Ensure all scripts are saved with appropriate filenames and adhere to the outlined structure.
