import app from "./app";

const server = Bun.serve({
  fetch(req) {
    return app.fetch(req);
  },
});

console.log("Server started at http://localhost:" + server.port);
