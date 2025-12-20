from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday Laatu 💗</title>

<style>
body {
    margin: 0;
    font-family: "Georgia", serif;
    text-align: center;
    color: #5a0c2c;
    background:
        radial-gradient(circle at top left, rgba(255,120,170,0.35), transparent 45%),
        radial-gradient(circle at bottom right, rgba(255,170,210,0.35), transparent 45%),
        linear-gradient(135deg, #ffd1e6, #ff9fcf);
    overflow-x: hidden;
}

h1 {
    font-size: 52px;
    margin-top: 30px;
    color: #b0004d;
    text-shadow: 0 0 20px rgba(255,105,180,0.6);
}

p {
    font-size: 22px;
    width: 80%;
    margin: auto;
    line-height: 1.6;
}

button {
    padding: 16px 38px;
    font-size: 18px;
    background: linear-gradient(135deg, #ff4f9a, #ff8fc7);
    border: none;
    border-radius: 40px;
    color: white;
    cursor: pointer;
    margin: 15px;
    box-shadow: 0 10px 30px rgba(255,105,180,0.6);
}

button:hover {
    transform: scale(1.05);
}

.gallery {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
}

.gallery img {
    width: 220px;
    border-radius: 24px;
    box-shadow: 0 15px 35px rgba(255,105,180,0.6);
}

.heart {
    font-size: 85px;
    color: #ff2f92;
    animation: beat 1.2s infinite;
}

@keyframes beat {
    50% { transform: scale(1.4); }
}

#letter {
    display: none;
    font-size: 24px;
    margin: 30px auto;
    padding: 30px;
    width: 80%;
    background: rgba(255,255,255,0.65);
    border-radius: 30px;
    box-shadow: 0 20px 45px rgba(255,105,180,0.5);
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

<!-- 🎶 MUSIC -->
<audio autoplay loop controls>
<source src="/static/song.mp3" type="audio/mpeg">
</audio>

<h1>🎉 Happy Birthday Duggu 🎉</h1>
<div class="heart">❤️</div>

<p>25 December — The most beautiful soul was born 💕</p>

<h2 id="countdown"></h2>

<button onclick="showLetter()">💌 Open Love Letter</button>

<div id="letter">
You make everything easy for me, thank you for being my best friend,  
my best guider and my soulmate ❤️  
I am so grateful to have you in my life 💕
Nakh m dum krti h but pyar bhi bhut krti h thank you for everything I Love You So much
</div>

<h2>📸 Our Memories</h2>
<div class="gallery">
<img src="/static/photo1.jpg">
<img src="/static/photo2.jpg">
<img src="/static/photo3.jpg">
</div>

<h2 id="midnight"></h2>

<script>
const birthday = new Date("December 25, 2025 00:00:00").getTime();

setInterval(() => {
    const now = new Date().getTime();
    const diff = birthday - now;

    if (diff <= 0) {
        document.getElementById("countdown").innerHTML =
            "🎂 It's Your Birthday Baby 🎂";
        document.getElementById("midnight").innerHTML =
            "💖 Happy Birthday My Love 💖 You are my forever 💕 Moteee";
        launchFireworks();
        launchConfetti();
    } else {
        const d = Math.floor(diff / (1000 * 60 * 60 * 24));
        const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const s = Math.floor((diff % (1000 * 60)) / 1000);

        document.getElementById("countdown").innerHTML =
            `🎂 Countdown: ${d}d ${h}h ${m}m ${s}s`;
    }
}, 1000);

function showLetter() {
    document.getElementById("letter").style.display = "block";
}

function launchFireworks() {
    setInterval(() => {
        const f = document.createElement("div");
        f.className = "firework";
        f.style.left = Math.random() * window.innerWidth + "px";
        f.style.top = Math.random() * window.innerHeight + "px";
        document.body.appendChild(f);
        setTimeout(() => f.remove(), 1000);
    }, 300);
}

function launchConfetti() {
    for (let i = 0; i < 200; i++) {
        const c = document.createElement("div");
        c.className = "confetti";
        c.style.left = Math.random() * window.innerWidth + "px";
        c.style.background =
            "hsl(" + Math.random() * 360 + ",100%,75%)";
        c.style.animationDuration =
            (Math.random() * 3 + 2) + "s";
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 6000);
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
