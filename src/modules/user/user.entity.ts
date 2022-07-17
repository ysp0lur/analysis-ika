import { Exclude } from 'class-transformer';
import {
  Entity,
  Column,
  PrimaryGeneratedColumn,
  CreateDateColumn,
  UpdateDateColumn,
  DeleteDateColumn,
  OneToMany,
} from 'typeorm';
import { Roles } from './enums/roles.enum';
import { PasswordTransformer } from './helpers/password.transformer';

@Entity({
  name: 'users',
})
export class UserEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ name: 'first_name', type: 'varchar', length: '150', nullable: false })
  firstName: string;

  @Column({ name: 'last_name', type: 'varchar', length: '150', nullable: false })
  lastName: string;

  @Column({ type: 'varchar', length: '255', unique: true, nullable: false })
  email: string;

  @Column({
    name: 'role',
    type: 'enum',
    enum: Roles,
    nullable: false,
    default: Roles.USER,
  })
  role: Roles;

  @Exclude()
  @Column({
    name: 'password',
    length: 255,
    transformer: new PasswordTransformer(),
  })
  password: string;

  @Column({ name: 'selected_activity', type: 'varchar', length: '150', nullable: false })
  selectedActivity: string;

  @Column({ name: 'system_type_use', type: 'varchar', length: '150', nullable: false })
  systemTypeUse: string;

  @Column({ type: 'varchar', length: '150', nullable: false })
  institution: string;

  @Column({ type: 'varchar', length: '150', nullable: false })
  orcid: string;

  @Column({ name: 'username', type: 'varchar', length: '150', nullable: false })
  userName: string;

  @Column({ name: 'signature_filename', type: 'varchar', length: '50', nullable: false })
  signatureFilename: string;

  @Column({ name: 'signature_path', type: 'varchar', length: '250', nullable: false })
  signaturePath: string;

  // Control fields
  @Exclude()
  @CreateDateColumn({ name: 'created_at', type: 'timestamptz', default: () => { return 'CURRENT_TIMESTAMP'; } })
  createdAt: Date;

  @Exclude()
  @UpdateDateColumn({ name: 'updated_at', type: 'timestamptz', default: () => { return 'CURRENT_TIMESTAMP'; } })
  updatedAt: Date;

  @Exclude()
  @DeleteDateColumn({ name: 'deleted_at', type: 'timestamptz' })
  deletedAt: Date;

  toJSON() {
    const { password, ...self } = this;
    return self;
  }
}

export class UserFillableFields {
  email: string;
  firstName: string;
  lastName: string;
  password: string;
  role?: Roles;
  selectedActivity: string;
  systemTypeUse: string;
  institution: string;
  orcid: string;
  userName: string;
  signatureFilename: string;
  signaturePath: string;
}
