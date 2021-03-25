import { readFileSync } from "fs";

export default () => {
  let jwtKey = process.env.JWT_KEY;

  if (process.env.JWT_KEY_FILE) {
    const contents = readFileSync(process.env.JWT_KEY_FILE, "utf8");
    jwtKey = contents.split(/\r?\n/)[0];
  }

  return {
    port: parseInt(process.env.PORT, 10) || 3000,
    auth: {
      jwtKey,
    },
    processingService: {
      host: process.env.PROCESSING_SERVICE_HOST || "localhost",
      port: process.env.PROCESSING_SERVICE_PORT || 5000,
    },
  };
};
