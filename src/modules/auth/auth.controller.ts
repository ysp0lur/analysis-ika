import { Body, Controller, Get, Post, UseGuards } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { ApiBearerAuth, ApiResponse, ApiTags } from '@nestjs/swagger';
import { classToPlain } from 'class-transformer';
import { AuthService, LoginPayload, RegisterPayload } from './';
import { CurrentUser } from './../common/decorator/current-user.decorator';
import { UserEntity, UsersService } from './../user';

@Controller('auth')
@ApiTags('authentication')
export class AuthController {
  constructor(
    private readonly authService: AuthService,
    private readonly userService: UsersService,
  ) {}

  @Post('login')
  @ApiResponse({ status: 201, description: 'Successful Login' })
  @ApiResponse({ status: 400, description: 'Bad Request' })
  @ApiResponse({ status: 401, description: 'Unauthorized' })
  async login(@Body() payload: LoginPayload): Promise<any> {
    const user = await this.authService.validateUser(payload);
    const data = await this.authService.createToken(user);
    return {
      error: false,
      data: classToPlain(data),
      message: 'Login'
    };
  }

  @Post('register')
  @ApiResponse({ status: 201, description: 'Successful Registration' })
  @ApiResponse({ status: 400, description: 'Bad Request' })
  @ApiResponse({ status: 401, description: 'Unauthorized' })
  async register(@Body() payload: RegisterPayload): Promise<any> {
    const user = await this.userService.create(payload);
    const data = await this.authService.createToken(user);
    return {
      error: false,
      data: classToPlain(data),
      message: 'Registered user'
    };
  }

  @ApiBearerAuth()
  @UseGuards(AuthGuard())
  @Get('me')
  @ApiResponse({ status: 200, description: 'Successful Response' })
  @ApiResponse({ status: 401, description: 'Unauthorized' })
  async getLoggedInUser(@CurrentUser() user: UserEntity): Promise<UserEntity> {
    return user;
  }
}
