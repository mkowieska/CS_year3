let map, mapCanvas;
const pieceSize = 75;  // Size of each puzzle piece (75x75px)
const pieces = [];      // To store puzzle pieces
const correctPositions = []; // To check if the puzzle is correctly placed

document.addEventListener("DOMContentLoaded", () => {
    initializeMap();
    initializeButtons();
    requestPermissions();
});

// Initialize the map with Leaflet.js
function initializeMap() {
    map = L.map('map').setView([51.505, -0.09], 13);  // Center on London initially
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // Event to update the canvas when the map view changes
    map.on("moveend", updateMapCanvas);
}

// Initialize buttons
function initializeButtons() {
    document.getElementById("myLocationBtn").addEventListener("click", locateUser);
    document.getElementById("downloadMapBtn").addEventListener("click", downloadMapAsImage);
}

// Request geolocation and notification permissions
function requestPermissions() {
    // Geolocation permission
    if ("geolocation" in navigator) {
        console.log("Geolocation is supported.");
    } else {
        alert("Geolocation is not available.");
    }

    // Notification permission for Edge
    if (window.Notification && Notification.permission !== "granted") {
        Notification.requestPermission().then(permission => {
            console.log("Notification permission:", permission);
        });
    }
}

// Locate user and update the map
function locateUser() {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const { latitude, longitude } = position.coords;
                console.log("User location:", latitude, longitude); // Debugging
                map.setView([latitude, longitude], 13);
            },
            error => {
                console.error("Geolocation error:", error); // Debugging
                alert("Unable to retrieve your location. Please check your settings.");
            }
        );
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

// Download map as an image and initialize puzzle pieces
function downloadMapAsImage() {
    setTimeout(() => {
        // Using leafletImage instead of html2canvas
        leafletImage(map, (err, canvas) => {
            if (err) {
                console.error("Error capturing the map:", err);
                alert("Failed to capture the map. Please try again.");
                return;
            }
            mapCanvas = canvas;
            createPuzzlePieces(); // Create puzzle pieces from the map image
        });
    }, 1000); // Delay to ensure the map is fully loaded before capturing
}

// Generate puzzle pieces
function createPuzzlePieces() {
    const piecesContainer = document.getElementById("puzzlePieces");
    piecesContainer.innerHTML = '';  // Clear any existing pieces
    correctPositions.length = 0; // Reset correct positions array

    // Calculate positions for 16 puzzle pieces (4x4 grid)
    for (let i = 0; i < 16; i++) {
        const piece = document.createElement("div");
        piece.className = "puzzle-piece";

        // Set the background image of the piece
        piece.style.backgroundImage = `url(${mapCanvas.toDataURL()})`;

        // Set the background position for each piece to crop the map image
        const x = (i % 4) * pieceSize;
        const y = Math.floor(i / 4) * pieceSize;
        piece.style.backgroundPosition = `-${x}px -${y}px`;

        // Set dimensions for the piece
        piece.style.width = pieceSize + 'px';
        piece.style.height = pieceSize + 'px';

        // Ensure positioning is absolute for proper drag-and-drop functionality
        piece.style.position = 'absolute';
        piece.style.left = `${Math.random() * 200}px`; // Randomize initial position
        piece.style.top = `${Math.random() * 200}px`;

        piece.setAttribute("data-index", i);
        piece.draggable = true;

        // Add event listeners for drag-and-drop
        piece.addEventListener("dragstart", onDragStart);
        piece.addEventListener("dragend", onDragEnd);
        piecesContainer.appendChild(piece);
        pieces.push(piece);
        correctPositions.push({ left: (i % 4) * pieceSize, top: Math.floor(i / 4) * pieceSize });
    }
}

// Handle the drag start event
function onDragStart(event) {
    event.dataTransfer.setData("text/plain", event.target.dataset.index);
    event.target.style.opacity = 0.5; // Dim the piece being dragged
}

// Handle the drag end event
function onDragEnd(event) {
    event.target.style.opacity = 1; // Reset opacity
}

// Enable drop functionality on the puzzle board
const puzzleBoard = document.getElementById("puzzleBoard");
puzzleBoard.addEventListener("dragover", (event) => {
    event.preventDefault(); // Allow drop
});

puzzleBoard.addEventListener("drop", (event) => {
    event.preventDefault();
    const pieceIndex = event.dataTransfer.getData("text/plain");
    const piece = pieces[pieceIndex];

    // Calculate the drop position on the board
    const rect = puzzleBoard.getBoundingClientRect();
    const left = event.clientX - rect.left - (pieceSize / 2);
    const top = event.clientY - rect.top - (pieceSize / 2);

    // Snap to grid
    piece.style.left = Math.round(left / pieceSize) * pieceSize + "px";
    piece.style.top = Math.round(top / pieceSize) * pieceSize + "px";

    checkCompletion();
});

// Enable drop functionality on the puzzle pieces container (left side)
const puzzlePiecesContainer = document.getElementById("puzzlePieces");
puzzlePiecesContainer.addEventListener("dragover", (event) => {
    event.preventDefault(); // Allow drop
});

puzzlePiecesContainer.addEventListener("drop", (event) => {
    event.preventDefault();
    const pieceIndex = event.dataTransfer.getData("text/plain");
    const piece = pieces[pieceIndex];

    // Calculate the drop position in the left container (puzzle pieces area)
    const rect = puzzlePiecesContainer.getBoundingClientRect();
    const left = event.clientX - rect.left - (pieceSize / 2);
    const top = event.clientY - rect.top - (pieceSize / 2);

    // Snap to grid
    piece.style.left = Math.round(left / pieceSize) * pieceSize + "px";
    piece.style.top = Math.round(top / pieceSize) * pieceSize + "px";
});

// Check if all pieces are in the correct positions
function checkCompletion() {
    let completed = true;

    for (let i = 0; i < pieces.length; i++) {
        const piece = pieces[i];
        const left = parseInt(piece.style.left);
        const top = parseInt(piece.style.top);
        if (left !== correctPositions[i].left || top !== correctPositions[i].top) {
            completed = false;
            break;
        }
    }

    if (completed) {
        alert("Congratulations! All pieces are in the correct position!");
        // Optionally, send a system notification
        if (Notification.permission === "granted") {
            new Notification("Puzzle Complete!", { body: "You have successfully completed the puzzle!" });
        }
    }
}

// Update map canvas when the map is moved
function updateMapCanvas() {
    leafletImage(map, (err, canvas) => {
        if (err) {
            console.error("Error capturing the map:", err);
            return;
        }
        mapCanvas = canvas;
    });
}
