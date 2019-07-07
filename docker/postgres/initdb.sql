CREATE USER velo_core_user WITH password 'velo_core_pass';
CREATE DATABASE velo_core_db;
GRANT ALL PRIVILEGES ON DATABASE velo_core_db TO velo_core_user;