// Create button dynamically
const btn = document.createElement("div");
btn.className = "ai-button";
btn.innerHTML = "🤖";
btn.onclick = function () {
  alert("AI Chat Open!");
};

// Add CSS
const style = document.createElement("style");
style.innerHTML = `
.ai-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #4CAF50;
  color: white;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 28px;
  cursor: pointer;
  box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}
.ai-button:hover {
  background-color: #45a049;
}
`;

document.head.appendChild(style);
document.body.appendChild(btn);