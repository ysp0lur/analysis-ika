import { Body, Controller, Get, Post, UploadedFile, UseGuards, UseInterceptors, Request, HttpException, HttpStatus, Param, Res } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { FileInterceptor } from '@nestjs/platform-express';
import { ApiBearerAuth, ApiBody, ApiConsumes, ApiResponse, ApiTags } from '@nestjs/swagger';
import { classToPlain } from 'class-transformer';
import { AuthService, LoginPayload, RegisterPayload } from './';
import { CurrentUser } from './../common/decorator/current-user.decorator';
import { UserEntity, UsersService } from './../user';
import { optionsUploadImage } from '../config/multer.config'

@Controller('auth')
@ApiTags('Authentication')
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

  @Post('signup')
  @ApiResponse({ status: 201, description: 'Successful Registration' })
  @ApiResponse({ status: 400, description: 'Bad Request' })
  @ApiResponse({ status: 401, description: 'Unauthorized' })
  @ApiConsumes('multipart/form-data')
  @ApiBody({
    schema: {
      type: 'object',
      properties: {
        firstName: { type: 'string' },
        lastName: { type: 'string' },
        email: { type: 'string' },
        role: { type: 'string' },
        password: { type: 'string' },
        passwordConfirmation: { type: 'string' },
        selectedActivity: { type: 'string' },
        systemTypeUse: { type: 'string' },
        institution: { type: 'string' },
        orcid: { type: 'string' },
        userName: { type: 'string' },
        signature: {
          type: 'string',
          format: 'binary',
        },
      },
    },
  })
  @UseInterceptors(FileInterceptor('signature', optionsUploadImage))
  async create(@Request() req, @UploadedFile() file: Express.Multer.File) {
    const user = await this.userService.create(req.body, file);
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

  @ApiBearerAuth()
  @UseGuards(AuthGuard())
  @Get('me/signature/:imageId')
  async serveImage(@Param('imageId') imageId: string, @Res() res): Promise<any> {
    res.sendFile(imageId, { root: 'uploads/images'});
  }
}
