from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday Babby ❤️</title>

<style>
body {
    background: linear-gradient(to right, #ff9a9e, #fad0c4);
    font-family: Arial;
    text-align: center;
    color: white;
    margin: 0;
    overflow-x: hidden;
}

h1 { font-size: 50px; margin-top: 30px; }
p { font-size: 22px; width: 80%; margin: auto; }

button {
    padding: 15px 30px;
    font-size: 18px;
    background: #ff4b5c;
    border: none;
    border-radius: 30px;
    color: white;
    cursor: pointer;
    margin: 10px;
}

.gallery img {
    width: 220px;
    margin: 10px;
    border-radius: 20px;
    box-shadow: 0 0 10px white;
}

.heart {
    font-size: 80px;
    animation: beat 1s infinite;
}

@keyframes beat {
    50% { transform: scale(1.3); }
}

#letter {
    display: none;
    font-size: 24px;
    margin-top: 20px;
}

/* FIREWORKS */
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

/* CONFETTI */
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

<h1>🎉 Happy Birthday Babby 🎉</h1>
<div class="heart">❤️</div>

<p>25 December — The most beautiful soul was born 💕</p>

<h2 id="countdown"></h2>

<button onclick="showLetter()">💌 Open Love Letter</button>

<div id="letter">
You make everything easy for me, thank you for being my best friend,  
my best guider and my soulmate ❤️  
I am so grateful to have you in my life 💕
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

// COUNTDOWN + MIDNIGHT SURPRISE
setInterval(() => {
    const now = new Date().getTime();
    const diff = birthday - now;

    if (diff <= 0) {
        document.getElementById("countdown").innerHTML =
            "🎂 It's Your Birthday Babby 🎂";
        document.getElementById("midnight").innerHTML =
            "✨ Happy Birthday My Love 💕 You are my forever ❤️";
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

// LOVE LETTER
function showLetter() {
    document.getElementById("letter").style.display = "block";
}

// FIREWORKS
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

// CONFETTI
function launchConfetti() {
    for (let i = 0; i < 200; i++) {
        const c = document.createElement("div");
        c.className = "confetti";
        c.style.left = Math.random() * window.innerWidth + "px";
        c.style.background =
            "hsl(" + Math.random() * 360 + ",100%,50%)";
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
