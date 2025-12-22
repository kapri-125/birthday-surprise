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

h1 { font-size: 44px; color: #b0004d; margin-top: 20px; }
p { font-size: 20px; }

/* Timer */
#timerBox { font-size: 26px; margin: 20px; }

/* Hidden */
.hidden { display: none; }

/* Card */
.card {
    background: rgba(255,255,255,0.9);
    margin: 25px auto;
    padding: 25px;
    width: 85%;
    border-radius: 30px;
    animation: pop 0.8s;
}
@keyframes pop {
    from { transform: scale(0.7); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

/* SLIDESHOW FIXED */
.slideshow {
    width: 230px;
    height: 360px;
    margin: 20px auto;
    position: relative;
    overflow: hidden;
    border-radius: 25px;
}
.slideshow img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    opacity: 0;
    transition: opacity 1s ease-in-out;
}
.slideshow img.active { opacity: 1; }

/* Cake */
#cake {
    font-size: 90px;
    cursor: pointer;
}
#cakePhoto {
    display: none;
    width: 220px;
    margin: 20px auto;
    border-radius: 25px;
}

/* GAME AREA */
#gameArea {
    position: relative;
    height: 200px;
}

/* Buttons */
button {
    padding: 15px 30px;
    font-size: 18px;
    background: #ff4f9a;
    border: none;
    border-radius: 40px;
    color: white;
    cursor: pointer;
    margin: 10px;
}

/* NO button */
#noBtn {
    position: absolute;
}

/* Love Message */
.love-card {
    margin: 20px auto;
    padding: 20px;
    width: 80%;
    background: rgba(255,255,255,0.9);
    border-radius: 25px;
    font-size: 22px;
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
</style>
</head>

<body>

<h1>🎉 Happy Birthday Duggu 🎉</h1>
<p>25 December — The most beautiful soul was born 💕</p>

<div id="timerBox">⏳ Unlocking in <span id="count">10</span> seconds...</div>

<div id="content" class="hidden">

<audio autoplay loop>
<source src="/static/song.mp3" type="audio/mpeg">
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
<p>Will You Marry me..? 💖</p>

<div id="gameArea">
<button onclick="yesClicked()">YES 💕</button>
<button id="noBtn" onmouseover="moveNo()">NO 😜</button>
</div>

<div id="loveMessage" class="love-card hidden">
💖 Mujhe toh pata hi tha 😘  
<br> Tum meri hi ho ❤️  
<br> I Love You Forever 💕
</div>

</div>

<script>
/* Timer */
let time = 10;
const t = setInterval(() => {
    time--;
    document.getElementById("count").innerText = time;
    if (time === 0) {
        clearInterval(t);
        document.getElementById("timerBox").style.display = "none";
        document.getElementById("content").classList.remove("hidden");
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
    launchConfetti();
}

/* MINI GAME FIXED */
let noCount = 0;
function moveNo() {
    noCount++;
    const btn = document.getElementById("noBtn");
    btn.style.left = Math.random() * 180 + "px";
    btn.style.top = Math.random() * 120 + "px";

    if (noCount >= 6) {
        btn.innerText = "YES 💕";
        btn.onclick = yesClicked;
        btn.onmouseover = null;
    }
}

function yesClicked() {
    document.getElementById("loveMessage").classList.remove("hidden");
    launchConfetti();
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
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
