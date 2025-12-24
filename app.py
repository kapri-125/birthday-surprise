from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday Duggu 💗</title>

<style>
body{margin:0;font-family:Georgia,serif;background:linear-gradient(135deg,#ffd1e6,#ff9fcf);
text-align:center;color:#5a0c2c;overflow-x:hidden}
h1{font-size:44px;margin-top:30px;color:#b0004d}
p{font-size:20px}
button{padding:15px 35px;font-size:18px;background:#ff4f9a;border:none;border-radius:40px;color:white;cursor:pointer;margin:10px}
.heart{font-size:80px;animation:beat 1s infinite}
@keyframes beat{50%{transform:scale(1.3)}}
#timerBox{font-size:26px;margin-top:30px}
.hidden{display:none}
.card{background:rgba(255,255,255,.9);margin:30px auto;padding:25px;width:85%;border-radius:30px}

/* SLIDESHOW */
.slideshow{width:260px;height:420px;margin:25px auto;border-radius:40px;overflow:hidden;position:relative}
.slideshow img{width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;opacity:0;transition:opacity 1s}
.slideshow img.active{opacity:1}

#cake{font-size:90px;cursor:pointer}
#cakePhoto{display:none;width:220px;margin:20px auto;border-radius:25px}
#gameArea{position:relative;height:180px}

.love-card{margin:25px auto;padding:22px;width:82%;background:white;border-radius:28px;
font-size:22px;color:#b0004d;transform:scale(.6);opacity:0;transition:.6s}
.love-card.show{transform:scale(1);opacity:1}

/* EFFECTS */
.confetti{position:fixed;width:10px;height:10px;animation:fall 4s linear infinite}
@keyframes fall{to{transform:translateY(100vh) rotate(360deg)}}
.firework{position:fixed;width:6px;height:6px;background:gold;border-radius:50%;animation:explode 1.5s forwards}
@keyframes explode{to{transform:scale(30);opacity:0}}
.balloon{position:fixed;bottom:-60px;font-size:40px;z-index:9999;animation:float 7s linear forwards}
@keyframes float{to{transform:translateY(-120vh) scale(1.2);opacity:0}}
</style>
</head>

<body>
<h1>🎉 Happy Birthday Duggu 🎉</h1>
<div class="heart">❤️</div>
<p>25 December — The most beautiful soul was born 💕</p>

<div id="timerBox">⏳ Surprise unlocks in <span id="countdown"></span></div>

<div id="content" class="hidden">
<audio id="bgMusic" loop><source src="/static/song.mp3" type="audio/mpeg"></audio>
<audio id="popSound"><source src="/static/pop.mp3" type="audio/mpeg"></audio>
<audio id="balloonSound"><source src="/static/balloon.mp3" type="audio/mpeg"></audio>

<div class="card">
<p>
You make everything easy for me, thank you for being my best friend,<br>
my best guider and my soulmate ❤️<br>
I am so grateful to have you in my life 💕<br>
Thank you for everything, I Love You So Much 🥺❤️
</p>
</div>

<h2>📸 Our Memories</h2>
<div class="slideshow">
<img src="/static/photo1.jpg" class="active">
<img src="/static/photo2.jpg"><img src="/static/photo3.jpg"><img src="/static/photo4.jpg">
<img src="/static/photo5.jpg"><img src="/static/photo6.jpg"><img src="/static/photo7.jpg">
<img src="/static/photo8.jpg"><img src="/static/photo9.jpg"><img src="/static/photo10.jpg">
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
💖 Mujhe toh pata hi tha 😘<br>Tum meri hi ho ❤️<br>I Love You Forever 💕
</div>
</div>

<script>
/* MIDNIGHT LOCK */
const unlockTime=new Date("December 25, 2025 00:00:00").getTime();
let unlocked=false;
function tick(){
 const now=Date.now(),d=unlockTime-now;
 if(d<=0 && !unlocked){
  unlocked=true;
  timerBox.style.display="none";
  content.classList.remove("hidden");
  bgMusic.play();
  startSlideshow();
  return;
 }
 if(d>0){
  const D=Math.floor(d/86400000),
        H=Math.floor((d%86400000)/3600000),
        M=Math.floor((d%3600000)/60000),
        S=Math.floor((d%60000)/1000);
  countdown.innerHTML=`${D}d ${H}h ${M}m ${S}s`;
 }
}
setInterval(tick,1000); tick();

/* SLIDESHOW */
let started=false,idx=0;
function startSlideshow(){
 if(started) return; started=true;
 const s=document.querySelectorAll(".slideshow img");
 setInterval(()=>{s[idx].classList.remove("active");idx=(idx+1)%s.length;s[idx].classList.add("active")},3000);
}

/* CAKE */
function cutCake(){cake.innerText="🍰";cakePhoto.style.display="block";firework()}

/* GAME */
let n=0;
function moveNo(){
 n++; const b=noBtn;
 b.style.position="relative";
 b.style.left=Math.random()*180-90+"px";
 b.style.top=Math.random()*120-60+"px";
 if(n>=6){b.innerText="YES 💕";b.onclick=yesClicked;b.onmouseover=null}
}

/* YES */
function yesClicked(){
 loveMessage.classList.remove("hidden");
 setTimeout(()=>loveMessage.classList.add("show"),50);
 loveMessage.scrollIntoView({behavior:"smooth",block:"center"});
 firework(); balloons();
 popSound.play(); balloonSound.play();
 if(navigator.vibrate) navigator.vibrate([200,100,200]);
}

/* EFFECTS */
function firework(){for(let i=0;i<8;i++){const f=document.createElement("div");
 f.className="firework";f.style.left=Math.random()*innerWidth+"px";
 f.style.top=Math.random()*innerHeight+"px";document.body.appendChild(f);
 setTimeout(()=>f.remove(),1500)}}
function balloons(){
 const r=gameArea.getBoundingClientRect();
 ["💖","D","U","G","G","U"].forEach((c,i)=>{
  const b=document.createElement("div");b.className="balloon";b.innerText=c;
  b.style.left=(r.left+(i+1)*r.width/7)+"px";document.body.appendChild(b);
  setTimeout(()=>b.remove(),7000)
 })
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
