const API = "http://localhost:8000";

// protect math operations page
if (window.location.pathname.endsWith("index.html") && !localStorage.getItem("authenticated")) {
  window.location.href = "auth.html";
}

const signUpForm = document.getElementById("signUpForm");
if (signUpForm) {
  signUpForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(signUpForm));

    const res = await fetch(`${API}/sign-up`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await res.json();
    document.getElementById("signUpResponse").textContent = result.message || result.error;

    if (res.ok) {
      localStorage.setItem("authenticated", "true");
      setTimeout(() => (window.location.href = "index.html"), 1000);
}
  });
}

const authForm = document.getElementById("authForm");
if (authForm) {
  authForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(authForm));

    const res = await fetch(`${API}/auth`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await res.json();
    document.getElementById("authResponse").textContent = result.message || result.error;

    if (res.ok) {
      localStorage.setItem("authenticated", "true");
      setTimeout(() => (window.location.href = "index.html"), 1000);
    }
  });
}

const mathForm = document.getElementById("mathForm");
if (mathForm) {
  const operationSelect = document.getElementById("operation");
  const powerField = document.getElementById("powerInput");
  const responseBox = document.getElementById("mathResponse");

  operationSelect.addEventListener("change", () => {
    powerField.style.display = operationSelect.value === "power" ? "block" : "none";
  });

  mathForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(mathForm);
    const operation = formData.get("operation");
    
    let payload;

    if (operation === "power") {
      payload = {
        base: Number(formData.get("number")),
        exponent: Number(formData.get("power"))
      };
    } else {
      payload = { number: Number(formData.get("number")) };
    }

    const res = await fetch(`${API}/compute/${operation}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const result = await res.json();
    responseBox.textContent = result.result !== undefined
      ? `Result: ${result.result}`
      : `Error: ${result.error || "Invalid input"}`;
  });
}

function logout() {
  localStorage.removeItem("authenticated");
  window.location.href = "auth.html";
}
