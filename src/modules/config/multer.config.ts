import { extname } from 'path';
import { existsSync, mkdirSync } from 'fs';
import { diskStorage } from 'multer';
import { v4 as uuid } from 'uuid';
import { HttpException, HttpStatus } from '@nestjs/common';
import { MAX_IMAGE_SIZE, UPLOAD_IMAGE } from '../config/constants';

// Multer configuration
export const multerConfig = {
  destImage: UPLOAD_IMAGE
};

// Multer upload options
export const optionsUploadImage = {
  // Enable file size limits
  limits: {
    fileSize: +MAX_IMAGE_SIZE
  },
  // Check the mimetypes to allow for upload
  fileFilter: (req: any, file: any, cb: any) => {
    if (file.mimetype.match(/\/(jpg|jpeg|png|gif)$/)) {
      // Allow storage of file
      cb(null, true);
    } else {
      // Reject file
      cb(new HttpException(`Unsupported file type ${extname(file.originalname)}`, HttpStatus.BAD_REQUEST), false);
    }
  },

  // Storage properties
  storage: diskStorage({
    // Destination storage path details
    destination: (req: any, file: any, cb: any) => {
      const uploadPath = multerConfig.destImage;
      // Create folder if doesn't exist
      if (!existsSync(uploadPath)) {
        mkdirSync(uploadPath, { recursive: true });
      }
      cb(null, uploadPath);
    },
    // File modification details
    filename: (req: any, file: any, cb: any) => {
      // Calling the callback passing the random name generated with the original extension name
      cb(null, `${uuid()}${extname(file.originalname)}`);
    }
  })
};
