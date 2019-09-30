const MAP_WIDTH = 10; // in tiles
const MAP_HEIGHT = 10; // in tiles
const TILE_SIZE = 32;

const assets = getAssets()

const objects = {
    "grass": {
        id: 0,
        name: "nothing",
        asset: assets["grass"]
    }, 
    "wall": {
        id: 1,
        name: "wall",
        asset: assets["wall"]
    },
    "player": {
        id: 2,
        name: "player",
        asset: assets["player"]
    },
    "dirt": {
        id: 3,
        name: "dirt",
        asset: assets["dirt"]
    }, 
    "flag": {
        id: 4,
        name: "flag",
        asset: assets["flag"]
    }
}

const map = initMap()

let playerPos = {
    x: 1,
    y: Math.floor(MAP_HEIGHT / 2) - 1
}

let otherPlayers = {}

const socket = new WebSocket("ws://localhost:6969")

socket.addEventListener('open', function (event) {
    console.log('Connexion established');
    socket.send(JSON.stringify(playerPos))
});

// Listen for messages
socket.addEventListener('message', function (event) {
    try {
        const otherPlayer = JSON.parse(event.data)
        if (otherPlayer.delete) {
            delete otherPlayers[otherPlayer.id]
        } else {
            otherPlayers[otherPlayer.id] = otherPlayer
        }
        redraw()
    } catch (err) {
        console.warn("Received something unusual... " + event.data)
    }
});

function idToObject(id) {
    const objectValues = Object.values(objects)
    for (let i = 0; i<objectValues.length; i++) {
        const object = objectValues[i]
        if (object.id == id) {
            return object
        }
    }
    throw new Error(`Object with id ${id} not found`)
}

function initMap() {
    const map = []
    for (let i = 0; i<MAP_HEIGHT; i++) {
        const row = Array(MAP_WIDTH)
        for (let j = 0; j<MAP_WIDTH; j++) {
            if (j < MAP_WIDTH / 2) {
                row[j] = objects["dirt"].id
            } else {
                row[j] = objects["grass"].id
            }
        }
        map.push(row)
    }

    for (let i = 0; i<MAP_HEIGHT; i++) {
        const center = Math.floor(MAP_WIDTH / 2)
        map[i][center] = objects["wall"].id
    }

    map[MAP_HEIGHT/2-1][MAP_WIDTH-2] = objects["flag"].id

    return map
}

function getAssets() {
    const wall = new Image()
    wall.src = "img/wall.png"
    const grass = new Image()
    grass.src = "img/grass.jpg"
    const dirt = new Image()
    dirt.src = "img/dirt.jpg"
    const player = new Image()
    player.src = "img/player.png"
    const flag = new Image()
    flag.src = "img/flag.png"

    return {
        wall,
        grass,
        player,
        dirt,
        flag
    }
}

function drawMap(ctx) {
    for (let i = 0; i<MAP_HEIGHT; i++) {
        for (let j = 0; j<MAP_WIDTH; j++) {
            const objectId = map[i][j]
            const object = idToObject(objectId)
            if (object.asset) {
                position_y = i * TILE_SIZE
                position_x = j * TILE_SIZE
                ctx.drawImage(object.asset, position_x, position_y, TILE_SIZE, TILE_SIZE)
            }
        }
    }
}
function drawPlayer(ctx) {
    position_x = playerPos.x * TILE_SIZE
    position_y = playerPos.y * TILE_SIZE
    ctx.drawImage(objects.player.asset, position_x, position_y, TILE_SIZE, TILE_SIZE)
}

function drawOtherPlayer(ctx) {
    Object.values(otherPlayers).forEach(player => {
        position_x = player.x * TILE_SIZE
        position_y = player.y * TILE_SIZE
        ctx.drawImage(objects.player.asset, position_x, position_y, TILE_SIZE, TILE_SIZE)
    })
}



function initKeyboardListener() {
    document.addEventListener('keydown', handleKeyDown)
}

function handleKeyDown(event) {
    let direction = { dx: 0, dy: 0}
    const eventCodeToDirection = {
        "ArrowDown": { dx:0, dy: 1},
        "ArrowUp": { dx:0, dy: -1},
        "ArrowLeft": { dx: -1, dy: 0},
        "ArrowRight": { dx: 1, dy: 0}
    };
    if (eventCodeToDirection[event.code]) {
        direction = eventCodeToDirection[event.code]
    } else {
        return
    }
    const targetPosition = {
        x: playerPos.x + direction.dx,
        y: playerPos.y + direction.dy
    }
    if (targetPosition.x < 0 || targetPosition.y < 0) {
        return
    }
    if (targetPosition.x >= MAP_WIDTH || targetPosition.y >= MAP_HEIGHT) {
        return
    }
    const objectAtTargetPosition = map[targetPosition.y][targetPosition.x]
    if (objectAtTargetPosition === objects.wall.id) {
        return
    }
    playerPos = targetPosition
    redraw()
    socket.send(JSON.stringify(playerPos))
}

function redraw() {
    const canvas = document.getElementById('canvas')
    const ctx = canvas.getContext('2d')
    drawMap(ctx)
    drawOtherPlayer(ctx)
    drawPlayer(ctx)
}

window.onload = function() {
    const canvas = document.getElementById('canvas')
    canvas.width = TILE_SIZE * MAP_WIDTH
    canvas.height = TILE_SIZE * MAP_HEIGHT
    redraw()
    initKeyboardListener()
}
