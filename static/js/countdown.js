const date = document.getElementById("date");
const hour = document.getElementById("hour");
const min = document.getElementById("min");
const sec = document.getElementById("sec");

function countdown() {
    const now = new Date(); // 現在時刻を取得
    const ontheday = new Date(2025,8,20);
    const diffTime = ontheday.getTime() - now.getTime(); // 時間の差を取得（ミリ秒）

  // ミリ秒から単位を修正
    const calcDate = Math.floor(diffTime / 1000 / 60 / 60 / 24);
    const calcHour = Math.floor(diffTime / 1000 / 60 / 60) % 24;
    const calcMin = Math.floor(diffTime / 1000 / 60) % 60;
    const calcSec = Math.floor(diffTime / 1000) % 60;

  // 取得した時間を表示（2桁表示）
    date.innerHTML = calcDate;
    hour.innerHTML = String(calcHour).padStart(2, '0');
    min.innerHTML = String(calcMin).padStart(2, '0');
    sec.innerHTML = String(calcSec).padStart(2, '0');
}
countdown();
setInterval(countdown,1000);