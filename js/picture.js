var slides = document.getElementsByClassName('slide');
var currentSlide = 0;

function showSlide(n) {
  slides[currentSlide].classList.remove('active');
  currentSlide = (n + slides.length) % slides.length;
  slides[currentSlide].classList.add('active');
}

// 自动轮播
setInterval(function() {
  showSlide(currentSlide + 1);
}, 3000); // 设置轮播间隔时间，单位为毫秒