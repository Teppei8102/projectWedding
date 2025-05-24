(function(d) {
    var config = {
        kitId: 'dnx8gax',
        scriptTimeout: 3000,
        async: true
    },
    h=d.documentElement,t=setTimeout(function(){h.className=h.className.replace(/\bwf-loading\b/g,"")+" wf-inactive";},config.scriptTimeout),tk=d.createElement("script"),f=false,s=d.getElementsByTagName("script")[0],a;h.className+=" wf-loading";tk.src='https://use.typekit.net/'+config.kitId+'.js';tk.async=true;tk.onload=tk.onreadystatechange=function(){a=this.readyState;if(f||a&&a!="complete"&&a!="loaded")return;f=true;clearTimeout(t);try{Typekit.load(config)}catch(e){}};s.parentNode.insertBefore(tk,s)
})(document);

const isFirstLoad = sessionStorage.getItem('isFirstLoad');
window.addEventListener('load', function() {
    document.getElementById('content').style.display = 'block';
    if (!isFirstLoad) {
        document.getElementById('message').style.display = 'block';
        document.body.style.overflowY = 'hidden';
        sessionStorage.setItem('isFirstLoad', true);
    } else {
        document.getElementById('message').style.display = 'none';
        document.body.style.overflowY = 'none';
    }
    setTimeout(function() {
        document.getElementById('content').style.opacity = 1;
        document.getElementById('loading').style.display = 'none';
    }, 600); // 少し遅延させてから透明度を変更
});

window.addEventListener('click', function() {
    document.getElementById('message').style.display = 'none';
    document.body.style.overflowY = 'none';
})

window.addEventListener('scroll', function(){
    document.querySelectorAll('.fadein').forEach(function(box) {
        if(window.scrollY + window.innerHeight > box.offsetTop) {
            box.classList.add('is-active');
        }
    });
});