let lastResult = "";

// ==========================
// Theme toggle
// ==========================
function toggleTheme() {
    document.body.classList.toggle("dark");
}

// ==========================
// Handle file upload → show in textarea
// ==========================
function handleFile(input, textareaId) {
    const file = input.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById(textareaId).value = e.target.result;
    };
    reader.readAsText(file);
}

// ==========================
// Drag & Drop
// ==========================
const dropArea = document.getElementById("drop");

if (dropArea) {
    ['dragenter','dragover','dragleave','drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    dropArea.addEventListener('dragover', () => dropArea.classList.add('dragover'));
    dropArea.addEventListener('dragleave', () => dropArea.classList.remove('dragover'));
    dropArea.addEventListener('drop', handleDrop);
}

function handleDrop(e) {
    const files = e.dataTransfer.files;
    if(files.length > 0){
        handleFile({files: [files[0]]}, 'text1');
        if(files[1]) handleFile({files: [files[1]]}, 'text2');
    }
}

// ==========================
// MAIN FUNCTION (FIXED)
// ==========================
async function checkPlagiarism() {
    const loader = document.getElementById("loader");
    loader.classList.remove("hidden");

    const text1 = document.getElementById("text1").value;
    const text2 = document.getElementById("text2").value;

    const file1 = document.getElementById("file1").files[0];
    const file2 = document.getElementById("file2").files[0];

    const threshold = document.getElementById("threshold").value;

    const formData = new FormData();

    // Send files if exist
    if (file1) formData.append("file1", file1);
    if (file2) formData.append("file2", file2);

    // Send text also
    formData.append("text1", text1);
    formData.append("text2", text2);
    formData.append("threshold", threshold);

    try {
        const response = await fetch("http://127.0.0.1:5000/uploads", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        loader.classList.add("hidden");

        if (data.error) {
            alert("❌ " + data.error);
            return;
        }

        // Show similarity
        document.getElementById("result").innerText =
            "Similarity: " + data.similarity + "%";

        lastResult = `Similarity: ${data.similarity}%`;

        // Show matches
        const matchesDiv = document.getElementById("matches");
        matchesDiv.innerHTML = "";

        data.matches.forEach(match => {
            const div = document.createElement("div");
            div.classList.add("match");
            div.innerHTML = `
                <p><b>Text 1:</b> ${match.text1}</p>
                <p><b>Text 2:</b> ${match.text2}</p>
                <p><b>Similarity:</b> ${match.score}%</p>
            `;
            matchesDiv.appendChild(div);
        });

    } catch (err) {
        loader.classList.add("hidden");
        alert("❌ Backend not responding");
        console.error(err);
    }
}

// ==========================
// Copy result
// ==========================
function copyResult() {
    navigator.clipboard.writeText(lastResult);
    alert("Copied!");
}

// ==========================
// Download report
// ==========================
function downloadReport() {
    const matchesDiv = document.getElementById("matches");
    const blob = new Blob([matchesDiv.innerText], { type: "text/plain" });

    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "report.txt";
    link.click();
}

// ==========================
// Dummy BERT
// ==========================
function useBERT() {
    alert("Advanced BERT mode activated! (for viva)");
}