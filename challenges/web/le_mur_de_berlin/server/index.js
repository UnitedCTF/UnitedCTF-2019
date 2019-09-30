const WebSocket = require('ws');
 
const port = 6969;
const wss = new WebSocket.Server({ port });
const flag = "FLAG-FR33D0M4TL4ST"

const id = (() => {
    let currentId = 0;
    const map = new WeakMap();

    return (object) => {
        if (!map.has(object)) {
            map.set(object, ++currentId);
        }

        return map.get(object);
    };
})();

const players = {}
 
wss.on('connection', function connection(ws) {
  Object.values(players).forEach(player => {
    ws.send(JSON.stringify(player))
  })
  ws.on('message', function incoming(data) {
      try {
        json = JSON.parse(data)
        keys = Object.keys(json)
        if (keys.length === 2 && keys.includes('x') && keys.includes('y')) {
          json.id = id(ws)
          players[json.id] = json
          wss.clients.forEach(function each(client) {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
              client.send(JSON.stringify(json))
            }
          });
          if (json.x === 8 && json.y === 4) {
            ws.send(flag)
          }
        } else {
          // ignoring invalid payload
        }
      } catch (err) {
        console.error(err)
      }
  });
  ws.on('close', function close() {
    const playerId = id(ws)
    delete players[playerId]
    wss.clients.forEach(function each(client) {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify({
          id: playerId,
          delete: true
        }))
      }
    })
  })
});

console.log("Listening on " + port)
