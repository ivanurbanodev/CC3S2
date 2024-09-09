const request = require('supertest');
const app = require('../src/app');

describe('GET /', () => {
  let server;

  beforeAll(() => {
    server = app.listen(0); // Usar 0 permite que el sistema asigne un puerto libre
  });

  afterAll((done) => {
    server.close(done); // Cierra el servidor después de las pruebas
  });

  it('should return Hello, World!', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.text).toBe('Hello, World!');
  });
});

