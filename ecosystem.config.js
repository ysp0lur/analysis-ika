/* eslint-disable @typescript-eslint/restrict-template-expressions */
/* eslint-disable @typescript-eslint/no-require-imports */
/* eslint-disable @typescript-eslint/no-var-requires */
/* eslint-disable @typescript-eslint/naming-convention */
/* eslint-disable @typescript-eslint/quotes */
/* eslint-disable quote-props */
/* eslint-disable padding-line-between-statements */
/* eslint-disable no-template-curly-in-string */
const pjson = require('./package.json');
module.exports = {
  "apps": [{
    "name": "Analysis-API-v1",
    "script": "dist/main.js",
    "autorestart": true,
    "watch": false,
    "instances": 1,
    "max_memory_restart": "1G",
    "time": true,
    "log_date_format": 'DD-MM HH:mm:ss.SSS',
    "env": {
      "NODE_ENV": "development",
      "APP_ENV":"dev",
      "APP_URL":"http://localhost",
      //# JWT AUTH
      "JWT_SECRET_KEY":"edwheRaulwehhgbTEST",
      "JWT_EXPIRATION_TIME":3600,
      "PORT": 4000,
      "JWT_SUB": "analysis",
      "SSL": false,
      "RELEASE": `analysis@${pjson.version}`,
      // mail
      "BASE_URL": "https://analysis.ika.mx/",

      // # Solo si se usa dentro de carpeta del proyecto
      "SSL_KEY_PATH": "../../../dev-stack/certs/local-key.pem",
      "SSL_CERT_PATH": "../../../dev-stack/certs/local-cert.pem",

      // # Uploads
      "MAX_FILE_SIZE": 100000000,
      "MAX_IMAGE_SIZE": 100000000,
      "UPLOAD_XLSX_FILE": `/data/analysis/xlsx/`,
      "UPLOAD_IMAGE": `/data/analysis/images/`,

      // # DB Local or Docker
      "TYPEORM_CONNECTION": "postgres",
      "TYPEORM_HOST": "localhost",
      "TYPEORM_USERNAME": "mcdm_user",
      "TYPEORM_PASSWORD": "r00t.4321",
      "TYPEORM_DATABASE": "mcdm",
      "TYPEORM_PORT": 5432,
      // # NO MODIFICAR SI NO ESTA SEGURO DE LO QUE HACE
      "TYPEORM_SYNCHRONIZE": false,
      "TYPEORM_LOGGING": true,
      "DB_CONNECTIONLIMIT": 100,
      "DB_CONNECTTIMEOUT": 10000,
      "TYPEORM_ENTITIES": "src/**/*.entity.ts",

      "TYPEORM_MIGRATIONS": "src/database/migration/*.ts",
      "TYPEORM_MIGRATIONS_DIR": "src/database/migration",
      "TYPEORM_MIGRATIONS_TABLE_NAME": "migrations"
    }
  }]
};
