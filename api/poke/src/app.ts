import { Hono } from "hono";
import { logger } from "hono/logger";

const app = new Hono().basePath("/api/poke");

app.use(logger());

app.get("/", (c) => {
  return c.json({ message: "Hello World!" });
});

app.get("/status", (c) => {
  return c.json({ message: "OK" });
});

export default app;
