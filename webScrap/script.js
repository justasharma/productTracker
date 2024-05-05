document.addEventListener('mousemove', (event) => {
    const eye = document.querySelector('.eye');
    const eyeBall = document.querySelector('.eye-ball');

    const eyeRect = eye.getBoundingClientRect();
    const eyeBallRect = eyeBall.getBoundingClientRect();

    const eyeCenterX = eyeRect.left + eyeRect.width / 2;
    const eyeCenterY = eyeRect.top + eyeRect.height / 2;

    const mouseX = event.clientX;
    const mouseY = event.clientY;

    const angle = Math.atan2(mouseY - eyeCenterY, mouseX - eyeCenterX);
    const distance = Math.min(eyeRect.width / 2, eyeRect.height / 2) - eyeBallRect.width / 2;

    const offsetX = distance * Math.cos(angle);
    const offsetY = distance * Math.sin(angle);

    eyeBall.style.transform = `translate(${offsetX}px, ${offsetY}px)`;
});
