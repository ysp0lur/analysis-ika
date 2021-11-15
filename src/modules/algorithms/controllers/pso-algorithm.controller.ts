import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { ApiOperation, ApiTags } from '@nestjs/swagger';
import { PsoAlgorithmService } from '../services/pso-algorithm.service';
import { CreatePsoAlgorithmDto, UpdatePsoAlgorithmDto } from '../dto/create-pso-algorithm.dto';
import { classToPlain } from 'class-transformer';
import { CreateADPsoAlgorithmDto } from '../dto/create-ad-pso-algorithm.dto';

@Controller('algorithm/pso')
@ApiTags('PSO Algorithm')
export class PsoAlgorithmController {
  constructor(private readonly algorithmsService: PsoAlgorithmService) {}
  @Post('random')
  @ApiOperation({ summary: `Calculate PSO (Random)` })
  async createPSO(@Body() createAlgorithmDto: CreatePsoAlgorithmDto) {
    const result = await this.algorithmsService.calculatePSORandom(createAlgorithmDto);
    return {
      error: false,
      data: classToPlain(result[0]),
      message: 'PSO Calculated Succesfully'
    };
  }
  
  @Post('ad')
  @ApiOperation({ summary: `Calculate AD-PSO` })
  async createADPSO(@Body() createAlgorithmDto: CreateADPsoAlgorithmDto) {
    const result = await this.algorithmsService.calculateAD_PSO(createAlgorithmDto);
    return {
      error: false,
      data: classToPlain(result),
      message: 'AD-PSO Calculated Succesfully'
    };
  }
}
