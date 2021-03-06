import { Injectable } from '@nestjs/common';
import { ConfigService } from './../config';

@Injectable()
export class AppService {
  constructor(private config: ConfigService) {}

  root(): string {
    return `Welcome to Analysis Server`;
  }
}
