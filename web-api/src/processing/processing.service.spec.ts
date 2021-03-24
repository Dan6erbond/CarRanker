import { Test, TestingModule } from '@nestjs/testing';
import { ProcessingService } from './processing.service';

describe('ProcessingService', () => {
  let service: ProcessingService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [ProcessingService],
    }).compile();

    service = module.get<ProcessingService>(ProcessingService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
