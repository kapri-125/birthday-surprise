from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday Duggu 💗</title>

<style>
body{
    margin:0;
    font-family:Georgia,serif;
    background:linear-gradient(135deg,#ffd1e6,#ff9fcf);
    text-align:center;
    color:#5a0c2c;
    overflow-x:hidden;
}

h1{font-size:44px;margin-top:30px;color:#b0004d;}
p{font-size:20px;}

button{
    padding:15px 35px;
    font-size:18px;
    background:#ff4f9a;
    border:none;
    border-radius:40px;
    color:white;
    cursor:pointer;
    margin:10px;
}

.heart{
    font-size:80px;
    animation:beat 1s infinite;
}
@keyframes beat{50%{transform:scale(1.3);}}

#timerBox{
    font-size:26px;
    margin-top:30px;
    animation:pop 1s;
}

.hidden{display:none;}

@keyframes pop{
    from{transform:scale(0.6);opacity:0;}
    to{transform:scale(1);opacity:1;}
}

.card{
    background:rgba(255,255,255,0.85);
    margin:30px auto;
    padding:25px;
    width:85%;
    border-radius:30px;
    animation:pop 1s;
}

/* SLIDESHOW – FIXED */
.slideshow{
    width:260px;
    height:420px;
    margin:25px auto;
    border-radius:40px;
    overflow:hidden;
    position:relative;
}
.slideshow img{
    width:100%;
    height:100%;
    object-fit:cover;
    object-position:center;
    position:absolute;
    top:0;
    left:0;
    opacity:0;
    transition:opacity 1s ease-in-out;
}
.slideshow img.active{opacity:1;}

#cake{
    font-size:90px;
    cursor:pointer;
    animation:bounce 1s infinite;
}
@keyframes bounce{50%{transform:scale(1.1);}}

#cakePhoto{
    display:none;
    width:220px;
    margin:20px auto;
    border-radius:25px;
}

#gameArea{position:relative;height:180px;}

.love-card{
    margin:25px auto;
    padding:22px;
    width:82%;
    background:rgba(255,255,255,0.95);
    border-radius:28px;
    font-size:22px;
    color:#b0004d;
    box-shadow:0 18px 45px rgba(255,105,180,0.55);
    transform:scale(0.6);
    opacity:0;
    transition:all .6s ease;
}
.love-card.show{
    transform:scale(1);
    opacity:1;
}

/* CONFETTI */
.confetti{
    position:fixed;
    width:10px;
    height:10px;
    animation:fall 4s linear infinite;
}
@keyframes fall{
    to{transform:translateY(100vh) rotate(360deg);}
}

/* FIREWORK */
.firework{
    position:fixed;
    width:6px;
    height:6px;
    background:gold;
    border-radius:50%;
    animation:explode 1.5s ease-out forwards;
}
@keyframes explode{
    to{transform:scale(30);opacity:0;}
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

<audio id="bgMusic" loop>
<source src="/static/song.mp3" type="audio/mpeg">
</audio>

<audio id="popSound">
<source src="/static/pop.mp3" type="audio/mpeg">
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
💖 Mujhe toh pata hi tha 😘<br>
Tum meri hi ho ❤️<br>
I Love You Forever 💕
</div>

</div>

<script>
/* TIMER */
let time=10;
let timer=setInterval(()=>{
    time--;
    document.getElementById("count").innerText=time;
    if(time===0){
        clearInterval(timer);
        document.getElementById("timerBox").style.display="none";
        document.getElementById("content").classList.remove("hidden");
        document.getElementById("bgMusic").play();
        startSlideshow();
    }
},1000);

/* SLIDESHOW – STABLE */
let slideshowStarted=false;
let slideIndex=0;
function startSlideshow(){
    if(slideshowStarted)return;
    slideshowStarted=true;
    const slides=document.querySelectorAll(".slideshow img");
    setInterval(()=>{
        slides[slideIndex].classList.remove("active");
        slideIndex=(slideIndex+1)%slides.length;
        slides[slideIndex].classList.add("active");
    },3000);
}

/* CAKE */
function cutCake(){
    document.getElementById("cake").innerText="🍰";
    document.getElementById("cakePhoto").style.display="block";
    fireworkBurst();
}

/* GAME */
let noCount=0;
function moveNo(){
    noCount++;
    const btn=document.getElementById("noBtn");
    btn.style.position="relative";
    btn.style.left=Math.random()*180-90+"px";
    btn.style.top=Math.random()*120-60+"px";
    if(noCount>=6){
        btn.innerText="YES 💕";
        btn.onclick=yesClicked;
        btn.onmouseover=null;
    }
}

/* YES */
function yesClicked(){
    const msg=document.getElementById("loveMessage");
    msg.classList.remove("hidden");
    setTimeout(()=>msg.classList.add("show"),50);
    msg.scrollIntoView({behavior:"smooth",block:"center"});
    fireworkBurst();
    document.getElementById("popSound").play();
    if(navigator.vibrate){navigator.vibrate([200,100,200]);}
}

/* FIREWORKS */
function fireworkBurst(){
    for(let i=0;i<8;i++){
        const f=document.createElement("div");
        f.className="firework";
        f.style.left=Math.random()*window.innerWidth+"px";
        f.style.top=Math.random()*window.innerHeight+"px";
        document.body.appendChild(f);
        setTimeout(()=>f.remove(),1500);
    }
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
