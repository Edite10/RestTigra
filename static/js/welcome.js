let currentSlide = 0;

function moveSlide(direction) {
    const track = document.getElementById('testimonialTrack');
    const totalSlides = track.children.length;
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
    track.style.transform = `translateX(-${currentSlide * 100}%)`;
}
