import {MigrationInterface, QueryRunner} from "typeorm";

export class fulluser1658009271657 implements MigrationInterface {
    name = 'fulluser1658009271657'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "users" ADD "selected_activity" character varying(150) NOT NULL`);
        await queryRunner.query(`ALTER TABLE "users" ADD "system_type_use" character varying(150) NOT NULL`);
        await queryRunner.query(`ALTER TABLE "users" ADD "institution" character varying(150) NOT NULL`);
        await queryRunner.query(`ALTER TABLE "users" ADD "orcid" character varying(150) NOT NULL`);
        await queryRunner.query(`ALTER TABLE "users" ADD "username" character varying(150) NOT NULL`);
        await queryRunner.query(`ALTER TABLE "users" ADD "signature_filename" character varying(50) NOT NULL`);
        await queryRunner.query(`ALTER TABLE "users" ADD "signature_path" character varying(250) NOT NULL`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "users" DROP COLUMN "signature_path"`);
        await queryRunner.query(`ALTER TABLE "users" DROP COLUMN "signature_filename"`);
        await queryRunner.query(`ALTER TABLE "users" DROP COLUMN "username"`);
        await queryRunner.query(`ALTER TABLE "users" DROP COLUMN "orcid"`);
        await queryRunner.query(`ALTER TABLE "users" DROP COLUMN "institution"`);
        await queryRunner.query(`ALTER TABLE "users" DROP COLUMN "system_type_use"`);
        await queryRunner.query(`ALTER TABLE "users" DROP COLUMN "selected_activity"`);
    }

}
