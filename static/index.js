(function (document) {
    // 头像阴影根据太阳东升西落自西向东
    let headPortrait = document.getElementById('head_portrait');
    let time = new Date();
    console.log(time);
    let hours = time.getHours();
    let shadowX = 0;
    let shadowY = -4;
    if (hours >= 6 && hours <= 18) {
        shadowX = hours - 2 * (hours - 6)
    } else {
        shadowX = 0;
        shadowY = 0;
    }
    console.log(shadowX, shadowY);
    headPortrait.style.boxShadowX = `${shadowX}px ${shadowY}px 12px #cccccc`;
})(document);
