// Initialize map and setup variables
let map, userMarker, mapCanvas;
const pieces = []; // To hold puzzle pieces
const correctPositions = []; // To verify correct placements
let pieceSize; // Dynamic piece size based on raster dimensions

document.addEventListener("DOMContentLoaded", () => {
    initializeMap();
    initializeButtons();
});

// Initialize the map with Leaflet.js
function initializeMap() {
    map = L.map('map').setView([51.505, -0.09], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    map.on("moveend", updateMapCanvas);
}

// Initialize buttons
function initializeButtons() {
    document.getElementById("myLocationBtn").addEventListener("click", locateUser);
    document.getElementById("downloadMapBtn").addEventListener("click", downloadMapAsImage);
}

// Locate user and update the map
function locateUser() {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const { latitude, longitude } = position.coords;
                map.setView([latitude, longitude], 13);
                if (userMarker) {
                    map.removeLayer(userMarker);
                }
                userMarker = L.marker([latitude, longitude]).addTo(map)
                    .bindPopup("You are here!")
                    .openPopup();
            },
            error => {
                alert("Unable to retrieve your location.");
            }
        );
    } else {
        alert("Geolocation is not supported.");
    }
}

// Use leaflet-image to capture map and initialize puzzle pieces
function downloadMapAsImage() {
    leafletImage(map, function (err, canvas) {
        if (err) {
            alert("Failed to capture the map image.");
            return;
        }
        mapCanvas = canvas;
        createPuzzlePieces();
    });
}

// Generate puzzle pieces
function createPuzzlePieces() {
    const puzzlePiecesContainer = document.getElementById("puzzlePieces");
    const puzzleBoard = document.getElementById("puzzleBoard");
    puzzlePiecesContainer.innerHTML = '';
    puzzleBoard.innerHTML = '';
    pieces.length = 0;
    correctPositions.length = 0;

    const imgWidth = mapCanvas.width;
    const imgHeight = mapCanvas.height;

    // Set puzzle board dimensions to match the map canvas
    puzzleBoard.style.width = imgWidth; //+ "px"; // Set width to match map width
    puzzleBoard.style.height = imgHeight;// + "px"; // Set height to match map height

    // Set puzzle pieces container to match the size of the map
    puzzlePiecesContainer.style.width = imgWidth; //+ "px";
    puzzlePiecesContainer.style.height = imgHeight;// + "px";

    // Set piece size to divide the image into equal parts
    const rows = 4; // Adjustable number of rows
    const cols = 4; // Adjustable number of columns
    pieceSize = imgWidth / cols;

    for (let y = 0; y < rows; y++) {
        for (let x = 0; x < cols; x++) {
            const piece = document.createElement("div");
            piece.className = "puzzle-piece";

            // Set the background image and crop it for the piece
            piece.style.backgroundImage = `url(${mapCanvas.toDataURL()})`;
            piece.style.backgroundSize = `${imgWidth}px ${imgHeight}px`;
            piece.style.backgroundPosition = `-${x * pieceSize}px -${y * pieceSize}px`;

            // Set dimensions and position
            piece.style.width = pieceSize + "px"; // Full size for each puzzle piece
            piece.style.height = pieceSize + "px"; // Full size for each puzzle piece

            // Initial position in the puzzle pieces container
            piece.style.position = "absolute";
            piece.style.left = `${x * pieceSize}px`;
            piece.style.top = `${y * pieceSize}px`;

            piece.draggable = true;
            piece.setAttribute("data-index", y * cols + x);

            // Event listeners for drag-and-drop
            piece.addEventListener("dragstart", onDragStart);
            piece.addEventListener("dragend", onDragEnd);

            puzzlePiecesContainer.appendChild(piece);
            pieces.push(piece);

            // Record correct positions
            correctPositions.push({ left: x * pieceSize, top: y * pieceSize });
        }
    }
}

// Handle the drag start event
function onDragStart(event) {
    event.dataTransfer.setData("text/plain", event.target.dataset.index);
    event.target.style.opacity = 0.5;
}

// Handle the drag end event
function onDragEnd(event) {
    event.target.style.opacity = 1;
}

// Enable drop functionality on the puzzle board
const puzzleBoard = document.getElementById("puzzleBoard");
puzzleBoard.addEventListener("dragover", (event) => {
    event.preventDefault();
});

puzzleBoard.addEventListener("drop", (event) => {
    event.preventDefault();
    const pieceIndex = event.dataTransfer.getData("text/plain");
    const piece = pieces[pieceIndex];

    // Calculate drop position relative to the board
    const rect = puzzleBoard.getBoundingClientRect();
    const left = event.clientX - rect.left - (pieceSize / 2);
    const top = event.clientY - rect.top - (pieceSize / 2);

    // Snap to grid
    piece.style.left = Math.round(left / pieceSize) * pieceSize + "px";
    piece.style.top = Math.round(top / pieceSize) * pieceSize + "px";

    checkCompletion();
});

// Check if all pieces are in the correct positions
function checkCompletion() {
    let completed = true;

    for (let i = 0; i < pieces.length; i++) {
        const piece = pieces[i];
        const left = parseInt(piece.style.left, 10);
        const top = parseInt(piece.style.top, 10);

        if (left !== correctPositions[i].left || top !== correctPositions[i].top) {
            completed = false;
            break;
        }
    }

    if (completed) {
        alert("Congratulations! You completed the puzzle!");
    }
}

// Update map canvas on map movement
function updateMapCanvas() {
    leafletImage(map, function (err, canvas) {
        if (!err && canvas) {
            mapCanvas = canvas;
        }
    });
}
