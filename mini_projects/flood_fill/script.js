const ROWS = 10;
const COLS = 10;
let isFilling = false;

const smileyPattern = [
  "WWWWWWWWWW",
  "WWYYYYYYWW",
  "WYYYYYYYYW",
  "WYYBYYBYYW", // Eyes at index 3 and 6
  "WYYYYYYYYW",
  "WYBYYYYBYW", // Smile edges at index 2 and 7
  "WYYBBBBYYW", // Smile bottom at index 3, 4, 5, 6
  "WYYYYYYYYW",
  "WWYYYYYYWW",
  "WWWWWWWWWW",
];

// 2. Map the blueprint letters to actual hex colors
const colorMap = {
  W: "#ffffff", // White
  Y: "#fdd835", // Yellow
  B: "#212121", // Dark Gray/Black
};

const gridElement = document.getElementById("grid");
const colorPicker = document.getElementById("colorPicker");
const resetBtn = document.getElementById("resetBtn");

gridElement.style.gridTemplateColumns = `repeat(${COLS}, 1fr)`;
gridElement.style.gridTemplateRows = `repeat(${ROWS}, 1fr)`;

function createGrid() {
  gridElement.innerHTML = "";
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      const cell = document.createElement("div");
      cell.classList.add("cell");
      cell.dataset.r = r;
      cell.dataset.c = c;

      const colorLetter = smileyPattern[r][c];
      cell.style.backgroundColor = colorMap[colorLetter];

      cell.role = "gridcell";
      cell.tabIndex = 0;
      cell.setAttribute("aria-label", `Row ${r}, Column ${c}`);

      cell.addEventListener("click", () => triggerFloodFill(r, c));
      cell.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          triggerFloodFill(r, c);
        }
      });

      gridElement.appendChild(cell);
    }
  }
}

function getCellColor(r, c) {
  cell = document.querySelector(`.cell[data-r="${r}"][data-c="${c}"]`);
  return cell ? cell.style.backgroundColor : null;
}

function hexToRgb(hex) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return `rgb(${r}, ${g}, ${b})`;
}

async function triggerFloodFill(r, c) {
  if (isFilling) return;

  const newColorHex = colorPicker.value;
  const newColorRgb = hexToRgb(newColorHex);
  const origColor = getCellColor(r, c);

  if (origColor === newColorRgb) return;

  isFilling = true;

  async function dfs(row, col) {
    // Base Case 1: Out of bounds
    if (row < 0 || row >= ROWS || col < 0 || col >= COLS) return;

    const currentCell = document.querySelector(
      `.cell[data-r="${row}"][data-c="${col}"]`,
    );

    // Base Case 2: Color mismatch
    if (currentCell.style.backgroundColor !== origColor) return;

    // The Action: Change color
    currentCell.style.backgroundColor = newColorRgb;

    // Artificial delay: Wait 50ms so we can see the algorithm working
    await new Promise((resolve) => setTimeout(resolve, 50));

    // The Exploration: Await ensures we dive deep before branching
    await dfs(row - 1, col); // Up
    await dfs(row + 1, col); // Down
    await dfs(row, col - 1); // Left
    await dfs(row, col + 1); // Right
  }

  await dfs(r, c);
  isFilling = false;
}

resetBtn.addEventListener("click", () => {
  if (!isFilling) createGrid();
});

createGrid();
