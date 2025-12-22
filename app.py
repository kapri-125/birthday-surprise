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

h1 {
    font-size: 44px;
    margin-top: 30px;
    color: #b0004d;
}

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

#timerBox {
    font-size: 26px;
    margin-top: 30px;
    animation: pop 1s;
}

.hidden { display: none; }

/* POP animation */
@keyframes pop {
    from { transform: scale(0.6); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

.card {
    background: rgba(255,255,255,0.85);
    margin: 30px auto;
    padding: 25px;
    width: 85%;
    border-radius: 30px;
    animation: pop 1s;
}

/* SLIDESHOW (UNCHANGED – PHOTO SAFE) */
.slideshow {
    width: 260px;         
    height: 420px;        
    margin: 25px auto ;
    border-radius: 40px;
    overflow: hidden;
    position: relative;
}
.slideshow img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    position: absolute ;
    opacity: 0;
    transition: opacity 1s ease-in-out;
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

/* GAME AREA */
#gameArea {
    position: relative;
    height: 180px;
}

/* Love message POP-OUT */
.love-card {
    margin: 25px auto;
    padding: 22px;
    width: 82%;
    background: rgba(255,255,255,0.95);
    border-radius: 28px;
    font-size: 22px;
    color: #b0004d;
    box-shadow: 0 18px 45px rgba(255,105,180,0.55);
    transform: scale(0.6);
    opacity: 0;
    transition: all 0.6s ease;
}
.love-card.show {
    transform: scale(1);
    opacity: 1;
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
<div class="heart">❤️</div>
<p>25 December — The most beautiful soul was born 💕</p>

<div id="timerBox">
⏳ Surprise unlocks in <span id="count">10</span> seconds...
</div>

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
<p>Will you marry me ? 💖</p>

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
/* TIMER */
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

let slideshowInterval;

function startSlideshow() {
    const slides = document.querySelectorAll(".slideshow img");
    let index = 0;

    if (slides.length > 1) {
        slideshowInterval = setInterval(() => {
            slides[index].classList.remove("active");
            index = (index + 1) % slides.length;
            slides[index].classList.add("active");
        }, 3000);
    }
}


/* CAKE */
function cutCake() {
    document.getElementById("cake").innerText = "🍰";
    document.getElementById("cakePhoto").style.display = "block";
    launchConfetti();
}

/* MINI GAME – NO runs 6 times */
let noCount = 0;
function moveNo() {
    noCount++;
    const btn = document.getElementById("noBtn");
    btn.style.position = "relative";
    btn.style.left = Math.random()*180 - 90 + "px";
    btn.style.top = Math.random()*120 - 60 + "px";

    if (noCount >= 6) {
        btn.innerText = "YES 💕";
        btn.onclick = yesClicked;
        btn.onmouseover = null;
    }
}

/* YES CLICK */
function yesClicked() {
    const msg = document.getElementById("loveMessage");
    msg.classList.remove("hidden");
    setTimeout(() => msg.classList.add("show"), 50);
    launchConfetti();
}

/* CONFETTI */
function launchConfetti() {
    for (let i = 0; i < 100; i++) {
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








