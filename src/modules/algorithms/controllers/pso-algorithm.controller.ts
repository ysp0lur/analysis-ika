import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { ApiOperation, ApiTags } from '@nestjs/swagger';
import { PsoAlgorithmService } from '../services/pso-algorithm.service';
import { CreatePsoAlgorithmDto, UpdatePsoAlgorithmDto } from '../dto/create-pso-algorithm.dto';
import { classToPlain } from 'class-transformer';

@Controller('algorithm/pso')
@ApiTags('PSO Algorithm')
export class PsoAlgorithmController {
  constructor(private readonly algorithmsService: PsoAlgorithmService) {}
  @Post('random')
  @ApiOperation({ summary: `Calculate PSO (Random)` })
  async create(@Body() createAlgorithmDto: CreatePsoAlgorithmDto) {
    const result = await this.algorithmsService.calculatePSORandom(createAlgorithmDto);
    return {
      error: false,
      data: classToPlain(result[0]),
      message: 'Calculated Succesfully'
    };
  }
}
