from flask import Flask, render_template_string

app = Flask(__name__)

HOME = """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday Laatu 💗</title>
<style>
body {
    font-family: Georgia;
    background: linear-gradient(135deg, #ffd1e6, #ff9fcf);
    text-align: center;
    color: #5a0c2c;
}
button {
    padding: 15px 35px;
    font-size: 18px;
    background: #ff4f9a;
    border: none;
    border-radius: 40px;
    color: white;
    cursor: pointer;
}
.heart {
    font-size: 80px;
    animation: beat 1s infinite;
}
@keyframes beat { 50% { transform: scale(1.3); } }
</style>
</head>
<body>

<h1>🎉 Happy Birthday Duggu 🎉</h1>
<div class="heart">❤️</div>
<p>25 December — The most beautiful soul was born 💕</p>

<a href="/letter"><button>💌 Open Love Letter</button></a>

</body>
</html>
"""

LETTER = """
<!DOCTYPE html>
<html>
<head>
<title>Love Letter 💌</title>
<style>
body {
    font-family: Georgia;
    background: linear-gradient(135deg, #ff9fcf, #ffd1e6);
    text-align: center;
    color: #5a0c2c;
    overflow-x: hidden;
}
.hidden { display: none; }

#banner {
    font-size: 42px;
    margin: 20px;
    color: #b0004d;
    animation: glow 1.5s infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 10px #ff4f9a; }
    to { text-shadow: 0 0 30px #ff2f92; }
}

.card {
    background: rgba(255,255,255,0.75);
    margin: 30px auto;
    padding: 25px;
    width: 80%;
    border-radius: 30px;
}

.gallery img {
    width: 200px;
    margin: 10px;
    border-radius: 20px;
}

button {
    padding: 15px 30px;
    font-size: 18px;
    background: #ff4f9a;
    border: none;
    border-radius: 40px;
    color: white;
    cursor: pointer;
    margin: 10px;
    position: relative;
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

/* Fireworks */
.firework {
    position: fixed;
    width: 6px;
    height: 6px;
    background: white;
    border-radius: 50%;
    animation: explode 1s linear;
}
@keyframes explode {
    to { transform: scale(25); opacity: 0; }
}

/* Balloons */
.balloon {
    position: fixed;
    bottom: -100px;
    font-size: 40px;
    animation: floatUp 6s linear infinite;
}
@keyframes floatUp {
    to { transform: translateY(-120vh); }
}

/* Cake */
#cake {
    font-size: 80px;
    cursor: pointer;
    animation: bounce 1s infinite;
}
@keyframes bounce {
    50% { transform: scale(1.1); }
}
</style>
</head>

<body>

<h2 id="timer">⏳ Surprise unlocking in <span id="count">5</span> seconds...</h2>

<div id="content" class="hidden">

<h1 id="banner">🎉 Happy Birthday Moteee 💖🎂</h1>

<audio id="music" loop>
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

<h2>🎂 Cut the Cake</h2>
<div id="cake" onclick="cutCake()">🎂</div>

<h2>📸 Our Memories</h2>
<div class="gallery">
<img src="/static/photo1.jpg">
<img src="/static/photo2.jpg">
<img src="/static/photo3.jpg">
</div>

<h2>🎮 Mini Game 😍</h2>
<p>Do you love me forever? 💖</p>

<button id="yesBtn" onclick="yesClicked()">YES 💕</button>
<button id="noBtn" onmouseover="moveNo()">NO 😜</button>

</div>

<script>
let countdown = 5;
let noCount = 0;

const timer = setInterval(() => {
    countdown--;
    document.getElementById("count").innerText = countdown;
    if (countdown === 0) {
        clearInterval(timer);
        document.getElementById("timer").classList.add("hidden");
        document.getElementById("content").classList.remove("hidden");
        document.getElementById("music").play();
        launchConfetti();
        launchFireworks();
        launchBalloons();
    }
}, 1000);

function moveNo() {
    noCount++;
    const btn = document.getElementById("noBtn");
    if (noCount < 3) {
        btn.style.left = Math.random()*200 - 100 + "px";
        btn.style.top = Math.random()*200 - 100 + "px";
    } else {
        btn.innerText = "YES 💕";
        btn.onclick = yesClicked;
    }
}

function yesClicked() {
    if (navigator.vibrate) {
        navigator.vibrate([200,100,200]);
    }
    launchConfetti();
}

function cutCake() {
    document.getElementById("cake").innerText = "🍰";
    launchConfetti();
}

/* Effects */
function launchConfetti() {
    for (let i = 0; i < 120; i++) {
        const c = document.createElement("div");
        c.className = "confetti";
        c.style.left = Math.random()*window.innerWidth + "px";
        c.style.background = "hsl(" + Math.random()*360 + ",100%,70%)";
        c.style.animationDuration = Math.random()*3 + 2 + "s";
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 5000);
    }
}

function launchFireworks() {
    setInterval(() => {
        const f = document.createElement("div");
        f.className = "firework";
        f.style.left = Math.random()*window.innerWidth + "px";
        f.style.top = Math.random()*window.innerHeight + "px";
        document.body.appendChild(f);
        setTimeout(() => f.remove(), 1000);
    }, 400);
}

function launchBalloons() {
    setInterval(() => {
        const b = document.createElement("div");
        b.className = "balloon";
        b.innerText = "🎈";
        b.style.left = Math.random()*window.innerWidth + "px";
        document.body.appendChild(b);
        setTimeout(() => b.remove(), 6000);
    }, 800);
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME)

@app.route("/letter")
def letter():
    return render_template_string(LETTER)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
