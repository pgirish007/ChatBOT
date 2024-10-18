const jsonServer = require('json-server');
const server = jsonServer.create();
const router = jsonServer.router('db.json');
const middlewares = jsonServer.defaults();

server.use(middlewares);

// Custom middleware to set a custom ID field
server.use(jsonServer.rewriter({
  '/:resource/:customId': '/:resource?id=:customId'
}));

server.use(router);

server.listen(5001, () => {
  console.log('JSON Server is running on port 3000');
});
