import { Injectable } from '@nestjs/common';
import { CreatePsoAlgorithmDto, UpdatePsoAlgorithmDto } from '../dto/create-pso-algorithm.dto';
import { PythonShell } from 'python-shell';
import { Options } from 'python-shell';
import { CreateADPsoAlgorithmDto } from '../dto/create-ad-pso-algorithm.dto';

@Injectable()
export class PsoAlgorithmService {

  async calculatePSORandom(createAlgorithmDto: CreatePsoAlgorithmDto): Promise<any> {
    console.log(createAlgorithmDto);
    
    const options: Options = {
      mode: 'json',
      // pythonPath: 'path/to/python',
      pythonOptions: ['-u'],
      scriptPath: 'src/scripts',
      args: [
        createAlgorithmDto.n.toString(),
        createAlgorithmDto.e.toString(),
        createAlgorithmDto.w.toString(),
        createAlgorithmDto.c1.toString(),
        createAlgorithmDto.c2.toString(),
        createAlgorithmDto.c3.toString(),
        createAlgorithmDto.c4.toString(),
        createAlgorithmDto.c5.toString(),
        createAlgorithmDto.c6.toString(),
        createAlgorithmDto.c7.toString(),
        createAlgorithmDto.c8.toString(),
        createAlgorithmDto.c9.toString(),
        createAlgorithmDto.CC.toString(),
        createAlgorithmDto.RR,
      ],
   };
     const result = await new Promise((resolve, reject) => {
       PythonShell.run('PSO.py', options, (err, results) => {
         if (err) return reject(err);
         return resolve(results);
       });
     });
     console.log(result);
     return result;
  }
 
  async calculateAD_PSO(createAlgorithmAD_PSO_Dto: CreateADPsoAlgorithmDto): Promise<any> {
    console.log(createAlgorithmAD_PSO_Dto);
    
    const options: Options = {
      mode: 'json',
      // pythonPath: 'path/to/python',
      pythonOptions: ['-u'],
      scriptPath: 'src/scripts',
      args: [
        createAlgorithmAD_PSO_Dto.e.toString(),
        createAlgorithmAD_PSO_Dto.w.toString()
      ],
   };
     const result = await new Promise((resolve, reject) => {
       PythonShell.run('AD-PSO.py', options, (err, results) => {
         if (err) return reject(err);
         return resolve(results);
       });
     });
     return result;
  }
}
