import { HttpModule, Module } from "@nestjs/common";
import { ConfigModule, ConfigService } from "@nestjs/config";
import { ProcessingService } from "./processing.service";

@Module({
  imports: [
    HttpModule.registerAsync({
      imports: [ConfigModule],
      useFactory: (configService: ConfigService) => ({
        baseURL: `http://${configService.get<string>(
          "processingService.host",
        )}:${configService.get<string>("processingService.port")}`,
      }),
      inject: [ConfigService],
    }),
  ],
  providers: [ProcessingService],
  exports: [ProcessingService],
})
export class ProcessingModule {}
