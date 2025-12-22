from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday Duggu 💗</title>

<style>
body {
    margin: 0;
    font-family: Georgia, serif;
    background: linear-gradient(135deg, #ffd1e6, #ff9fcf);
    text-align: center;
    color: #5a0c2c;
    overflow-x: hidden;
}

h1 { font-size: 44px; margin-top: 20px; color: #b0004d; }
p { font-size: 20px; }

button {
    padding: 15px 35px;
    font-size: 18px;
    background: #ff4f9a;
    border: none;
    border-radius: 40px;
    color: white;
    cursor: pointer;
    margin: 10px;
}

.heart {
    font-size: 80px;
    animation: beat 1s infinite;
}
@keyframes beat { 50% { transform: scale(1.3); } }

/* Time */
#clock {
    font-size: 22px;
    margin-top: 10px;
    color: #8b0038;
}

/* Timer */
#timerBox {
    font-size: 26px;
    margin-top: 20px;
}

/* Hidden */
.hidden { display: none; }

/* Pop animation */
@keyframes pop {
    from { transform: scale(0.6); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

.card {
    background: rgba(255,255,255,0.9);
    margin: 30px auto;
    padding: 25px;
    width: 85%;
    border-radius: 30px;
    animation: pop 0.8s;
}

/* Slideshow */
.slideshow {
    width: 260px;
    height: 360px;
    margin: 25px auto;
    border-radius: 30px;
    background: rgba(255,255,255,0.4);
    overflow: hidden;
    position: relative;
}
.slideshow img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    position: absolute;
    opacity: 0;
    transition: opacity 1s;
}
.slideshow img.active { opacity: 1; }

/* Cake */
#cake {
    font-size: 90px;
    cursor: pointer;
    animation: bounce 1s infinite;
}
@keyframes bounce { 50% { transform: scale(1.1); } }
#cakePhoto {
    display: none;
    width: 220px;
    margin: 20px auto;
    border-radius: 25px;
}

/* Love message */
.love-card {
    margin: 25px auto;
    padding: 20px;
    width: 80%;
    background: rgba(255,255,255,0.9);
    border-radius: 25px;
    font-size: 22px;
    color: #b0004d;
    animation: pop 0.8s;
}

/* Confetti */
.confetti {
    position: fixed;
    width: 10px;
    height: 10px;
    animation: fall 4s linear infinite;
}
@keyframes fall {
    to { transform: translateY(100vh) rotate(360deg); }
}

/* Floating hearts */
.floating-heart {
    position: fixed;
    bottom: 0;
    font-size: 26px;
    animation: floatUp 4s ease-in forwards;
}
@keyframes floatUp {
    to { transform: translateY(-100vh); opacity: 0; }
}
</style>
</head>

<body>

<h1>🎉 Happy Birthday Duggu 🎉</h1>
<div class="heart">❤️</div>
<p>25 December — The most beautiful soul was born 💕</p>

<div id="clock"></div>

<div id="timerBox">
⏳ Surprise unlocks in <span id="count">10</span> seconds...
</div>

<div id="content" class="hidden">

<audio id="bgMusic" autoplay loop>
<source src="/static/song.mp3" type="audio/mpeg">
</audio>

<audio id="cakeSound">
<source src="/static/cake.mp3" type="audio/mpeg">
</audio>

<div class="card">
<p>
You make everything easy for me, thank you for being my best friend,<br>
my best guider and my soulmate ❤️<br>
I am so grateful to have you in my life 💕<br>
Nakh m dum krti h but pyar bhi bhut krti h 💖<br>
Thank you for everything, I Love You So Much 🥺❤️
</p>
</div>

<h2>📸 Our Memories</h2>
<div class="slideshow">
<img src="/static/photo1.jpg" class="active">
<img src="/static/photo2.jpg">
<img src="/static/photo3.jpg">
</div>

<h2>🎂 Cut the Cake</h2>
<div id="cake" onclick="cutCake()">🎂</div>
<img id="cakePhoto" src="/static/cake_photo.jpg">

<h2>🎮 Mini Game 😍</h2>
<p>Do you love me forever? 💖</p>

<button onclick="yesClicked()">YES 💕</button>
<button id="noBtn" onmouseover="moveNo()">NO 😜</button>

<div id="loveMessage" class="love-card hidden">
💖 Mujhe toh pata hi tha 😘  
<br> Tum meri hi ho ❤️  
<br> I Love You Forever 💕
</div>

</div>

<script>
/* Live Clock */
setInterval(() => {
    const now = new Date();
    document.getElementById("clock").innerText =
        "⏰ Time: " + now.toLocaleTimeString();
}, 1000);

/* Timer */
let time = 10;
const t = setInterval(() => {
    time--;
    document.getElementById("count").innerText = time;
    if (time === 0) {
        clearInterval(t);
        document.getElementById("timerBox").style.display = "none";
        document.getElementById("content").classList.remove("hidden");
        launchConfetti();
    }
}, 1000);

/* Slideshow */
let slides = document.querySelectorAll(".slideshow img");
let index = 0;
setInterval(() => {
    slides[index].classList.remove("active");
    index = (index + 1) % slides.length;
    slides[index].classList.add("active");
}, 3000);

/* Cake */
function cutCake() {
    document.getElementById("cake").innerText = "🍰";
    document.getElementById("cakePhoto").style.display = "block";
    document.getElementById("cakeSound").play();
    launchConfetti();
}

/* Mini game */
let noCount = 0;
function moveNo() {
    noCount++;
    const btn = document.getElementById("noBtn");
    btn.style.left = Math.random()*200 - 100 + "px";
    btn.style.top = Math.random()*200 - 100 + "px";
    if (noCount > 2) {
        btn.innerText = "YES 💕";
        btn.onclick = yesClicked;
    }
}

function yesClicked() {
    document.getElementById("loveMessage").classList.remove("hidden");
    launchConfetti();
    launchHearts();
}

/* Confetti */
function launchConfetti() {
    for (let i = 0; i < 80; i++) {
        const c = document.createElement("div");
        c.className = "confetti";
        c.style.left = Math.random()*window.innerWidth + "px";
        c.style.background = "hsl(" + Math.random()*360 + ",100%,70%)";
        c.style.animationDuration = Math.random()*3 + 2 + "s";
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 5000);
    }
}

/* Floating hearts */
function launchHearts() {
    for (let i = 0; i < 20; i++) {
        const h = document.createElement("div");
        h.className = "floating-heart";
        h.innerText = "❤️";
        h.style.left = Math.random()*window.innerWidth + "px";
        document.body.appendChild(h);
        setTimeout(() => h.remove(), 4000);
    }
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
