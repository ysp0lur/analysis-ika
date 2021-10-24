const dotenv = require('dotenv');

dotenv.config();

const {
  TYPEORM_CONNECTION,
  TYPEORM_HOST,
  TYPEORM_USERNAME,
  TYPEORM_PASSWORD,
  TYPEORM_PORT,
  TYPEORM_DATABASE,
} = process.env;

module.exports = {
  type: TYPEORM_CONNECTION,
  host: TYPEORM_HOST,
  port: TYPEORM_PORT,
  username: TYPEORM_USERNAME,
  password: TYPEORM_PASSWORD,
  database: TYPEORM_DATABASE,
  migrations: [__dirname + '/src/migrations/*{.ts,.js}'],
  entities: [__dirname + '/src/**/*.entity.{ts,js}'],
};
