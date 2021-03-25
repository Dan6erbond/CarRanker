import { HttpService, Injectable } from "@nestjs/common";
import { Car } from "../cars/entities/car.entity";

@Injectable()
export class ProcessingService {
  constructor(private httpService: HttpService) {}

  async scrapeCar(url: string) {
    try {
      const {
        data: { id },
      } = await this.httpService
        .post<Partial<Car>>("/api/v1/cars", { url })
        .toPromise();
      return id;
    } catch (error) {
      if (error.response) {
        throw new Error(error.response.data.message);
      } else if (error.request) {
        throw new Error(error.request);
      } else {
        throw new Error(error.message);
      }
    }
  }
}
