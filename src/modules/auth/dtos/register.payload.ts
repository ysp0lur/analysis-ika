import { ApiProperty } from '@nestjs/swagger';
import { IsEmail, IsNotEmpty, IsOptional, IsString, MaxLength, MinLength } from 'class-validator';
import { Roles } from 'modules/user/enums/roles.enum';
import { Unique } from '@src/modules/common';
import { SameAs } from '@src/modules/common/validator/same-as.validator';
import { UserEntity } from '@src/modules/user';

export class RegisterPayload {
  @ApiProperty({
    required: true,
  })
  @IsEmail()
  @Unique([UserEntity])
  email: string;

  @ApiProperty({
    required: true,
  })
  @IsNotEmpty()
  @MaxLength(150)
  firstName: string;

  @ApiProperty({
    required: true,
  })
  @IsNotEmpty()
  @MaxLength(150)
  lastName: string;

  @IsString()
  @IsOptional()
  @ApiProperty()
  readonly role: Roles;

  @ApiProperty({
    required: true,
  })
  @IsNotEmpty()
  @MinLength(5)
  password: string;

  @ApiProperty({ required: true })
  @SameAs('password')
  passwordConfirmation: string;
}
