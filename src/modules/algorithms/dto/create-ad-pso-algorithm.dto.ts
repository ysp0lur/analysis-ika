import { ApiProperty, PartialType } from "@nestjs/swagger";
import { IsPositive, IsNotEmpty, Max, IsArray, IsString, MaxLength, Min } from "class-validator";

type rRandom = 'a' | 'b' | 'c'
/**
 * @ysp0lur
 * @author Raul E. Aguirre H.
 *
 */
 export class CreateADPsoAlgorithmDto {
  
  @Max(100000)
  @Min(0)
  @ApiProperty({ description: 'E' })
  readonly e: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'W' })
  readonly w: number;

 }

export class UpdatePsoAlgorithmDto extends PartialType(CreateADPsoAlgorithmDto) {}