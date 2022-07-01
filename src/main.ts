import { ClassSerializerInterceptor, ValidationPipe } from '@nestjs/common';
import { NestFactory, Reflector } from '@nestjs/core';
import { useContainer } from 'class-validator';
import { TrimStringsPipe } from './modules/common/transformer/trim-strings.pipe';
import { AppModule } from './modules/main/app.module';
import { setupSwagger } from './swagger';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  setupSwagger(app);
  app.setGlobalPrefix('api/v1');
  app.enableCors();
  /**
  * Guardas globales
  */
  app.useGlobalPipes(new TrimStringsPipe(), new ValidationPipe({
    transform: true,
    whitelist: true,
    // disableErrorMessages: true,
    transformOptions: {
      enableImplicitConversion: true
    }
  }));
  
  app.useGlobalInterceptors(new ClassSerializerInterceptor(app.get(Reflector)));
  useContainer(app.select(AppModule), { fallbackOnErrors: true });
  await app.listen(4000);
}
bootstrap();
