import { Module } from '@nestjs/common';
import { PsoAlgorithmService } from './services/pso-algorithm.service';
import { PsoAlgorithmController } from './controllers/pso-algorithm.controller';

@Module({
  controllers: [PsoAlgorithmController],
  providers: [PsoAlgorithmService]
})
export class AlgorithmsModule {}
