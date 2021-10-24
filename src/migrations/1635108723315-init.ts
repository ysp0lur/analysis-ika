import {MigrationInterface, QueryRunner} from "typeorm";

export class init1635108723315 implements MigrationInterface {
    name = 'init1635108723315'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`CREATE TYPE "public"."users_role_enum" AS ENUM('ADMIN', 'USER', 'PUBLIC', 'EDITOR')`);
        await queryRunner.query(`CREATE TABLE "users" ("id" SERIAL NOT NULL, "first_name" character varying(150) NOT NULL, "last_name" character varying(150) NOT NULL, "email" character varying(255) NOT NULL, "role" "public"."users_role_enum" NOT NULL DEFAULT 'USER', "password" character varying(255) NOT NULL, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "updated_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, CONSTRAINT "UQ_97672ac88f789774dd47f7c8be3" UNIQUE ("email"), CONSTRAINT "PK_a3ffb1c0c8416b9fc6f907b7433" PRIMARY KEY ("id"))`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`DROP TABLE "users"`);
        await queryRunner.query(`DROP TYPE "public"."users_role_enum"`);
    }

}
