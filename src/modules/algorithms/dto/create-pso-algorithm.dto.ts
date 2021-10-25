import { ApiProperty, PartialType } from "@nestjs/swagger";
import { IsPositive, IsNotEmpty, Max, IsArray, IsString, MaxLength, Min } from "class-validator";

type rRandom = 'a' | 'b' | 'c'
/**
 * @ysp0lur
 * @author Raul E. Aguirre H.
 *
 */
 export class CreatePsoAlgorithmDto {
  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'N' })
  readonly n: number;

  @Max(100000)
  @Min(0)
  @ApiProperty({ description: 'E' })
  readonly e: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'W' })
  readonly w: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C1' })
  readonly c1: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C2' })
  readonly c2: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C3' })
  readonly c3: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C4' })
  readonly c4: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C5' })
  readonly c5: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C6' })
  readonly c6: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C7' })
  readonly c7: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C8' })
  readonly c8: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'C9' })
  readonly c9: number;

  @IsNotEmpty()
  @Min(0)
  @Max(100000)
  @ApiProperty({ description: 'CC' })
  readonly CC: number;

  @IsNotEmpty()
  @ApiProperty({ description: 'RR' })
  readonly RR: rRandom;

 }

export class UpdatePsoAlgorithmDto extends PartialType(CreatePsoAlgorithmDto) {}