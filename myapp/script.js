function generateFace() {
  const name = document.getElementById("nameInput").value || "Anonymous";
  fetch(`/generate?name=${name}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("faceImage").src = data.image;
      document.getElementById("desc").innerText = data.description;
    });
}