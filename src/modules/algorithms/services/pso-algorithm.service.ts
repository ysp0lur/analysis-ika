import { Injectable } from '@nestjs/common';
import { CreatePsoAlgorithmDto, UpdatePsoAlgorithmDto } from '../dto/create-pso-algorithm.dto';
import { PythonShell } from 'python-shell';
import { Options } from 'python-shell';

@Injectable()
export class PsoAlgorithmService {
  async test(): Promise<any> {
    const options: Options = {
      mode: 'text',
      // pythonPath: 'path/to/python',
      pythonOptions: ['-u'],
      scriptPath: 'src/scripts',
      // args: [code],
   };
     const result = await new Promise((resolve, reject) => {
       PythonShell.run('init.py', options, (err, results) => {
         if (err) return reject(err);
         return resolve(results);
       });
     });
     console.log(result);
     return result[0];
  }

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
       PythonShell.run('functionRandom.py', options, (err, results) => {
         if (err) return reject(err);
         return resolve(results);
       });
     });
     console.log(result);
     return result;
  }
}
