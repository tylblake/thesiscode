document.getElementById("outfit-form").addEventListener("submit", function(event) {
    event.preventDefault();

    let occasion = document.getElementById("occasion").value;
    let weather = document.getElementById("weather").value;
    let preferences = document.getElementById("style").value;
    let size = document.getElementById("size").value;

    fetch("/get_outfit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        occasion: occasion,
        weather: weather,
        preferences: preferences,
        size: size
      })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById("outfit-suggestion").innerText = data.outfit;
    });
});
