import { Injectable, NotAcceptableException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

import { UserEntity, UserFillableFields } from './user.entity';

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(UserEntity)
    private readonly userRepository: Repository<UserEntity>,
  ) {}

  async get(id: number) {
    return this.userRepository.findOne({ id });
  }

  async getByEmail(email: string) {
    return await this.userRepository.findOne({ email });
  }

  async create(payload: any, file: any) {
    let data: UserFillableFields = {
      firstName: payload.firstName,
      lastName: payload.lastName,
      email: payload.email,
      password: payload.password,
      selectedActivity: payload.selectedActivity,
      systemTypeUse: payload.systemTypeUse,
      institution: payload.institution,
      orcid: payload.orcid,
      userName: payload.userName,
      signatureFilename: file.originalname,
      signaturePath: file.filename,
    }
    if (payload.role) {
      data.role = payload.role;
    }
    
    const user = await this.getByEmail(payload.email);

    if (user) {
      throw new NotAcceptableException(
        'User with provided email already created.',
      );
    }

    return await this.userRepository.save(data);
  }
}
